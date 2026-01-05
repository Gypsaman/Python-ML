"""
gastos_app.py

Simple expense tracker with:
- JSON persistence
- Tkinter GUI (add/view/delete + total)

Data format (gastos.json):
[
  {"concepto": "Comida", "monto": 250.0},
  {"concepto": "Gasolina", "monto": 45.25}
]
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

import tkinter as tk
from tkinter import ttk, messagebox


# ----------------------------
# Domain Model
# ----------------------------

@dataclass(frozen=True)
class Gasto:
    concepto: str
    monto: float

    def validate(self) -> None:
        if not self.concepto or not self.concepto.strip():
            raise ValueError("El concepto no puede estar vacío.")
        if not isinstance(self.monto, (int, float)):
            raise ValueError("El monto debe ser numérico.")
        if self.monto < 0:
            raise ValueError("El monto no puede ser negativo.")


# ----------------------------
# Persistence Layer (JSON)
# ----------------------------

class GastosRepository:
    def __init__(self, filename: str = "gastos.json") -> None:
        self.filename = filename

    def load(self) -> List[Gasto]:
        if not os.path.exists(self.filename):
            # No file yet -> empty list
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("El archivo JSON no tiene el formato esperado (lista).")

            gastos: List[Gasto] = []
            for item in data:
                if not isinstance(item, dict):
                    continue
                concepto = str(item.get("concepto", "")).strip()
                monto_raw = item.get("monto", 0.0)
                try:
                    monto = float(monto_raw)
                except (TypeError, ValueError):
                    continue

                g = Gasto(concepto=concepto, monto=monto)
                # Skip invalid entries gracefully
                try:
                    g.validate()
                    gastos.append(g)
                except ValueError:
                    continue

            return gastos

        except json.JSONDecodeError:
            # Corrupt JSON
            messagebox.showwarning(
                "Advertencia",
                "El archivo JSON está corrupto o vacío. Se iniciará con una lista vacía."
            )
            return []
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
            return []

    def save(self, gastos: List[Gasto]) -> None:
        data = [asdict(g) for g in gastos]
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")


# ----------------------------
# Application / Controller
# ----------------------------

class GastosApp:
    def __init__(self, root: tk.Tk, repo: Optional[GastosRepository] = None) -> None:
        self.root = root
        self.root.title("Gestor de Gastos (JSON)")
        self.root.minsize(720, 420)

        self.repo = repo or GastosRepository("gastos.json")
        self.gastos: List[Gasto] = self.repo.load()

        self._build_ui()
        self._refresh_table()

        # Save on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def _build_ui(self) -> None:
        # Main layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        header = ttk.Frame(self.root, padding=(12, 12, 12, 6))
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(1, weight=1)

        title = ttk.Label(header, text="Gestor de gastos", font=("TkDefaultFont", 14, "bold"))
        title.grid(row=0, column=0, sticky="w")

        self.total_var = tk.StringVar(value="Total gastado: 0.00")
        total_label = ttk.Label(header, textvariable=self.total_var)
        total_label.grid(row=0, column=1, sticky="e")

        # Content frame
        content = ttk.Frame(self.root, padding=(12, 6, 12, 12))
        content.grid(row=1, column=0, sticky="nsew")
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        # Table (Treeview)
        self.tree = ttk.Treeview(
            content,
            columns=("concepto", "monto"),
            show="headings",
            selectmode="browse",
            height=12,
        )
        self.tree.heading("concepto", text="Concepto")
        self.tree.heading("monto", text="Monto")
        self.tree.column("concepto", width=420, anchor="w")
        self.tree.column("monto", width=160, anchor="e")

        vsb = ttk.Scrollbar(content, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        # Controls
        controls = ttk.Frame(content, padding=(0, 10, 0, 0))
        controls.grid(row=1, column=0, columnspan=2, sticky="ew")
        controls.columnconfigure(1, weight=1)

        ttk.Label(controls, text="Concepto:").grid(row=0, column=0, sticky="w")
        self.concepto_entry = ttk.Entry(controls)
        self.concepto_entry.grid(row=0, column=1, sticky="ew", padx=(8, 8))

        ttk.Label(controls, text="Monto:").grid(row=0, column=2, sticky="w")
        self.monto_entry = ttk.Entry(controls, width=14)
        self.monto_entry.grid(row=0, column=3, sticky="w", padx=(8, 0))

        add_btn = ttk.Button(controls, text="Agregar", command=self.add_gasto)
        add_btn.grid(row=0, column=4, sticky="e", padx=(12, 0))

        delete_btn = ttk.Button(controls, text="Eliminar seleccionado", command=self.delete_selected)
        delete_btn.grid(row=1, column=4, sticky="e", padx=(12, 0), pady=(10, 0))

        save_btn = ttk.Button(controls, text="Guardar", command=self.save_now)
        save_btn.grid(row=1, column=3, sticky="w", pady=(10, 0))

        # Hint row
        hint = ttk.Label(
            controls,
            text="Consejo: puedes escribir el monto como 12.50. Se guardará automáticamente al cerrar.",
            foreground="#555",
        )
        hint.grid(row=1, column=0, columnspan=3, sticky="w", pady=(10, 0))

        # Bind Enter to add
        self.root.bind("<Return>", lambda _e: self.add_gasto())

    def _refresh_table(self) -> None:
        # Clear
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fill
        total = 0.0
        for idx, g in enumerate(self.gastos, start=1):
            self.tree.insert("", "end", iid=str(idx), values=(g.concepto, f"{g.monto:.2f}"))
            total += g.monto

        self.total_var.set(f"Total gastado: {total:.2f}")

    def add_gasto(self) -> None:
        concepto = self.concepto_entry.get().strip()
        monto_str = self.monto_entry.get().strip()

        if not concepto:
            messagebox.showwarning("Validación", "El concepto no puede estar vacío.")
            return

        try:
            monto = float(monto_str)
        except ValueError:
            messagebox.showwarning("Validación", "Monto inválido. Usa un número, por ejemplo 12.50.")
            return

        g = Gasto(concepto=concepto, monto=monto)
        try:
            g.validate()
        except ValueError as e:
            messagebox.showwarning("Validación", str(e))
            return

        self.gastos.append(g)
        self._refresh_table()

        # Clear inputs
        self.concepto_entry.delete(0, tk.END)
        self.monto_entry.delete(0, tk.END)
        self.concepto_entry.focus_set()

    def delete_selected(self) -> None:
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Eliminar", "Selecciona un gasto para eliminar.")
            return

        iid = selected[0]
        # iid is 1-based index string; map back to list index
        try:
            list_index = int(iid) - 1
        except ValueError:
            return

        if list_index < 0 or list_index >= len(self.gastos):
            return

        g = self.gastos[list_index]
        if not messagebox.askyesno("Confirmar", f"¿Eliminar '{g.concepto}' por {g.monto:.2f}?"):
            return

        del self.gastos[list_index]
        self._refresh_table()

    def save_now(self) -> None:
        self.repo.save(self.gastos)
        messagebox.showinfo("Guardar", "Gastos guardados correctamente.")

    def on_close(self) -> None:
        # Save on exit (quietly)
        try:
            self.repo.save(self.gastos)
        finally:
            self.root.destroy()


def main() -> None:
    root = tk.Tk()
    # Use ttk themed widgets
    try:
        style = ttk.Style()
        # "clam" tends to look decent across platforms
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except Exception:
        pass

    app = GastosApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
