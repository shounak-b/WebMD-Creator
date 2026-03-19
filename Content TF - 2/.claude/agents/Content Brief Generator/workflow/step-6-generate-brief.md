# Step 6: Generate Content Brief

Synthesize research into a content brief with headlines, internal links, word count, content goal, and meta description.

**Output Format:** [output-structure.md](output-structure.md)

---

## Contents

- [Workflow Checklist](#workflow-checklist)
- [Required Inputs](#required-inputs)
- [Instructions](#instructions)
- [Quality Checks](#quality-checks)

---

## Workflow Checklist

Copy and track progress:

```
Step 6 Progress:
- [ ] A. Generate headline structure (H1/H2/H3)
- [ ] A1. Write H1 intro text (page-type specific)
- [ ] B. Integrate internal links from Step 3
- [ ] C. Apply brand guidelines (scan for prohibited terms)
- [ ] D. Set target word count from Step 2
- [ ] E. Write content goal (2-3 sentences)
- [ ] F. Generate page title (50-60 chars)
- [ ] G. Generate meta description (150-160 chars)
- [ ] H. Define URL structure
- [ ] I. Specify tone of voice
- [ ] J. Format output per output-structure.md
- [ ] K. Run quality checklist
```

---

## Required Inputs

From previous steps:
- **Step 1:** Page Name, Primary Keyword, Secondary Keywords, Client Name, Domains
- **Step 2:** Recommended Word Count Range
- **Step 3:** Internal Linking Opportunities
- **Step 4:** Existing Page Headlines (if applicable)
- **Step 5:** Competitor Headlines

---

## Instructions

### A. Generate Headline Structure

Create SEO-optimized headlines:
- **1 H1** — Include Primary Keyword, ≤60 chars
- **H2s** — Major sections, subtopics of H1
- **H3s** — Subtopics under parent H2 only
- **All headlines** — ≤60 characters

See [headline-strategy.md](headline-strategy.md) for patterns and examples.

---

### A1. Write H1 Intro Text

Write one introductory paragraph placed immediately after the H1. Vary content and length based on page type:

**Blog / Pillar page — 50–75 words**
- Open with the core challenge the reader is facing
- Briefly introduce the solution approach
- State what the article will cover or help the reader accomplish
- Tone: educational, empathetic

**Landing page / Service page — 15–20 words (1–2 sentences)**
- Concisely answer the "how" behind the H1
- Lead with key differentiators or value props
- Optionally frame as: pain point → solution
- Tone: practical, outcome-focused

**Category page — 15–20 words (1–2 sentences)**
- Highlight key differentiators or value props for that specific category
- Tone: informative, direct

**Rules for all page types:**
- Apply brand guidelines — no prohibited terms
- Do not repeat the H1 verbatim
- Write as a complete, standalone sentence or short paragraph (no bullet points)
- Frame from the reader's perspective

---

### B. Integrate Internal Links

From Step 3, specify for each link:
- Anchor text
- URL
- Placement (which H2/H3 section)

Distribute across multiple sections.

---

### C. Apply Brand Guidelines

**CRITICAL:** Scan all headlines for prohibited terms.

Reference: [../brand-guidelines.md](../brand-guidelines.md)

**Prohibited:**
- Absolutes: ensure, guarantee, always, all, any, 100%, seamless, effortless
- Superlatives: best, most powerful, revolutionary, unique, perfect
- Vague: powerful, smart, robust (without specifics)

**Replacements:**
- "Ensure" → "Helps ensure", "Supports"
- "Best" → "Among the leading options"
- "Eliminate" → "Reduce", "Minimize"

Check all tense variations (ensure/ensures/ensured/ensuring).

---

### D. Set Target Word Count

Use range from Step 2.
- Floor: 500 words
- Ceiling: varies by page type (see Step 2)

---

### E. Write Content Goal

2-3 sentences describing what the page will accomplish.

Base on:
- Generated headlines
- Target audience (ICP)
- Primary Keyword intent

Frame from reader's perspective.

---

### F. Generate Page Title

- Format: `{Primary Keyword} | Visual Planning`
- Length: 50-60 characters

---

### G. Generate Meta Description

- Length: 150-160 characters
- Include Primary Keyword naturally
- Action-oriented, complete sentences
- Follow brand guidelines

---

### H. Define URL Structure

- Format: `https://www.visual-planning.com/en/[path]/`
- Lowercase, hyphens for spaces
- Include Primary Keyword when possible

---

### I. Specify Tone of Voice

Options: "Informative and professional", "Educational and empathetic", "Practical and outcome-focused"

---

## Output Format

Follow [output-structure.md](output-structure.md) exactly.

Sections in order:
1. Title header with date
2. Goal of Content
3. Keyword Research
4. Page Title
5. Meta Description
6. URL Structure
7. Target Word Count
8. Target Keywords
9. Headings/Sections (NO writing instructions)
10. Tone of Voice
11. Internal Links
12. Premium Assets

**Do NOT add writing instructions under headlines.** Those are added in Step 8.

---

## Quality Checks

Use checklist from [output-structure.md](output-structure.md#quality-checklist).

Quick verification:
- [ ] All sections from output-structure.md included
- [ ] 1 H1 with Primary Keyword
- [ ] Intro text present after H1, matches page-type length and focus
- [ ] All headlines ≤60 chars
- [ ] No prohibited terminology
- [ ] No writing instructions under headlines


---

## Error Handling

- If previous step returned "NA" → work with available info, note in output
- If brand guidelines inaccessible → flag for manual review
- If no internal links from Step 3 → note "Manual internal linking review needed"

---

## Next Step

[Step 7: Save Content Brief to File](step-7-save-brief.md)
