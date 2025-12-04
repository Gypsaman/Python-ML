import sys
import os

def create_toc(directory: str) -> None:
    toc = []
    for file in os.listdir(directory):
        if file.endswith('.md'):
            toc.append(f'# {file}\n')
            with open(os.path.join(directory, file), 'r') as f:
                lines = f.readlines()
            for line in lines:
                if line.startswith('# '):
                    toc.append('- '+line[1:])
    with open(os.path.join(directory,'TOC.md'), 'w') as f:
        f.writelines(toc)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python image_paths.py markdown_file')
        sys.exit(1)

    markdown_dir = sys.argv[1]
    create_toc(markdown_dir) 

