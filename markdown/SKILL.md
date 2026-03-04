---
name: research-report
description: 
  Use this skill when the user asks to research a topic and produce a structured
  written report, white paper, briefing document, or literature summary. Triggers
  include: "write a report on...", "summarize the research on...", "give me a
  briefing about...", "compile findings on...". Do NOT use for casual Q&A,
  single-fact lookups, or tasks where the deliverable is code or a spreadsheet.
license: MIT
---

# Research Report Skill

## Overview

This skill guides you through producing a well-structured, cited research report.
You will search for sources, synthesize findings, and produce a polished document.

---

## Step 1: Clarify the Request

Before searching, identify:

- **Topic**: What is the core subject?
- **Scope**: How broad or narrow?
- **Audience**: Technical expert, executive, general public?
- **Length**: Executive summary (1 page) vs. deep-dive report (5–10 pages)?
- **Format**: Should the output be a `.docx`, `.pdf`, or Markdown?

If any of these are ambiguous, ask the user one clarifying question before proceeding.

---

## Step 2: Research Strategy

1. Start with 2–3 broad queries to map the landscape
2. Identify key subtopics from results
3. Run targeted follow-up queries for each subtopic
4. Fetch full pages for the 3–5 most relevant sources (not just snippets)
5. Prioritize: peer-reviewed papers > government/institutional reports > reputable journalism > blogs

**Minimum sources**: 5 for a short report, 10+ for a deep-dive.

### Source Quality Tiers

| Tier | Examples | Trust Level |
|------|----------|-------------|
| Primary | PubMed, arXiv, SEC filings, gov data | High |
| Secondary | NYT, Reuters, Nature News | Medium-High |
| Tertiary | Industry blogs, LinkedIn articles | Use with caution |
| Avoid | Anonymous forums, SEO content farms | Do not cite |

---

## Step 3: Synthesis Rules

- **Always paraphrase** — never reproduce more than 14 words verbatim
- **Attribute every claim** — "According to [Source], ..."
- **Triangulate**: If only one source makes a claim, flag it as unverified
- **Surface disagreement**: If sources conflict, present both views and note the tension

---

## Step 4: Report Structure

```
1. Executive Summary       (150–200 words, no jargon)
2. Background & Context
3. Key Findings            (3–5 major themes)
4. Analysis
5. Open Questions
6. Conclusion
7. References
```

---

## Step 5: Quality Checklist

Before delivering the report, verify:

- [ ] All claims are attributed to a source
- [ ] No section is copy-pasted from a source
- [ ] Executive Summary can stand alone (no undefined terms)
- [ ] References section is complete with URLs where possible
- [ ] Report length matches the requested scope
- [ ] Tone matches the stated audience

---

## Known Failure Modes

| Failure | How to Avoid |
|---------|-------------|
| Hallucinating citations | Only cite sources actually retrieved via search |
| Over-summarizing | Fetch full pages, not just snippets |
| Scope creep | Re-read the user's original request before writing |
| False balance | Don't manufacture controversy where consensus exists |
| Recency bias | Check publication dates; prefer recent but note foundational older sources |

---

## Output Format

- **Markdown** — default
- **`.docx`** — if user mentions "Word", "document", or "downloadable"
- **`.pdf`** — if user mentions "PDF" or "printable"

---

## Metadata

```json
{
  "name": "research-report",
  "version": "1.2.0",
  "tools_required": ["web_search", "web_fetch"],
  "tools_optional": ["file_create"],
  "avg_token_cost": 4000,
  "max_recommended_depth": "10 sources",
  "compatible_models": ["claude-sonnet-4-20250514", "claude-opus-4-5"]
}
```
