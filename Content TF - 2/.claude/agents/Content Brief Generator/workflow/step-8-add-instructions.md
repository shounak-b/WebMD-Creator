# Step 8: Add Writing Instructions Under Each Headline

Add bracketed writing instructions with word counts under each headline to guide the content writer.

**Prerequisite:** User must approve the content brief from Step 7 before proceeding.

---

## Contents

- [Workflow Checklist](#workflow-checklist)
- [Instruction Format](#instruction-format)
- [Word Count Guidelines](#word-count-guidelines)
- [Instructions by Heading Type](#instructions-by-heading-type)
- [Special Elements](#special-elements)
- [Output Format](#output-format)
- [Quality Checklist](#quality-checklist)

---

## Workflow Checklist

Copy and track progress:

```
Step 8 Progress:
- [ ] A. Read content brief from Step 7
- [ ] B. Add instruction under H1 (15-20 words guidance)
- [ ] C. Add instructions under each H2 (vary by section type)
- [ ] D. Add instructions under each H3 (20-50 words guidance)
- [ ] E. Add special element notes (tables, testimonials)
- [ ] F. Apply brand guidelines to instruction language
- [ ] G. Save as content-brief-with-instructions.md
- [ ] H. Verify with quality checklist
```

---

## Instruction Format

**Format:** `[(word count): instruction text]`

**Example:**
```markdown
**H2:** *Why teams switch to Visual Planning*

[(20 words): Highlight the top reasons project managers, resource planners, and operations teams choose Visual Planning over other tools. Lead with flexibility, ease of use, and scheduling depth as the core narrative.]
```

**Rules:**
- Square brackets containing word count and instruction
- Word count in parentheses at start: `(15-20 words):`
- Instruction describes what to write, not the actual content
- Single paragraph, no line breaks within brackets

---

## Word Count Guidelines

| Heading Type | Word Count Range | When to Use |
|--------------|------------------|-------------|
| H1 intro text — Blog / Pillar page | (50-75 words) | Challenge → solution → what the article covers |
| H1 intro text — Landing / Service page | (15-20 words) | "How" behind the H1 — key differentiators or value props; optionally pain point → solution |
| H1 intro text — Category page | (15-20 words) | Key differentiators or value props for that category |
| H2 (intro) | (15-20 words) | Short section intros |
| H2 (standard) | (30-40 words) | Most H2 sections |
| H2 (detailed) | (40-60 words) | Complex topics needing more context |
| H3 (short) | (20-30 words) | Feature explanations, simple subtopics |
| H3 (standard) | (35-50 words) | Most H3 sections |
| H3 (FAQ) | (50-75 words) | FAQ answers requiring detail |

---

## Instructions by Heading Type

### H1 (Main Headline) + Intro Text

The H1 headline stands alone — no instruction on the headline itself. Add a writing instruction for the **intro text** that follows the H1 (drafted in Step 6). Use the word count for the relevant page type (see Word Count Guidelines above).

```markdown
**H1:** *Visual Planning alternatives: Compare leading solutions*

*[intro text drafted in Step 6]*

[(15-20 words): Introduce Visual Planning as a flexible, visual-first alternative to popular project management and scheduling tools. Concisely answer the "how" — focus on what makes VP distinctly suited for teams evaluating their options.]
```

### First H2 (Problem/Challenge Section)

Frame the challenge the target audience faces.

```markdown
**H2:** *Growth has exposed gaps in your planning process*

[(30-40 words): Acknowledge that as mid-market companies expand, disconnected tools and informal processes create operational blind spots that limit visibility, delay decisions, and increase coordination risk.]
```

### Standard H2

Explain what the section covers and why it matters.

```markdown
**H2:** *Visual Planning vs. the competition*

[(15-20 words): Introduce a feature comparison table that should be included below. Frame it as a simple way for teams to see how Visual Planning stacks up across key capabilities.]
```

### H3 (Subtopics)

Provide specific guidance for the subtopic.

```markdown
**H3:** *Customizable visual views*

[(20-30 words): Explain that Visual Planning offers Gantt, Kanban, and other view types that can be customized to any industry or workflow. Contrast this with rigid tools that lock teams into a single view format.]
```

### H3 (FAQ Questions)

Guide how to answer each FAQ with more detail.

```markdown
**H3:** *How does Visual Planning differ from competitors?*

[(50-75 words): Explain that unlike rigid project management tools (Smartsheet and Microsoft Project) or general task boards (monday.com and Excel), Visual Planning combines highly customizable scheduling views, such as Gantt and Kanban, with drag-and-drop simplicity, real-time collaboration, and integration with ERP and Microsoft systems. Emphasize that it is purpose-built for teams that need visual, flexible planning across industries and team sizes.]
```

---

## Special Elements

### Tables

Include table instructions in brackets:

```markdown
**H2:** *Visual Planning vs. the competition*

[(15-20 words): Introduce a feature comparison table that should be included below.]

[Include a feature comparison table. Columns: Visual Planning, Smartsheet, monday.com, Microsoft Project, Microsoft Excel. Rows should include features such as customizable views (Gantt/Kanban), drag-and-drop scheduling, real-time collaboration, resource and workforce planning, integrations, and scalability. Use checkmarks for supported features.]
```

### Testimonials

```markdown
**H2:** *What our users are saying*

[Include a testimonial carousel with 3-5 customer testimonials. Each testimonial should include a name, company or industry, and a brief quote emphasizing scheduling ease, team visibility, or time savings.]
```

---

## Output Format

### File Structure

Save as `content-brief-with-instructions.md` in the same folder as the original brief.

```markdown
# Visual Planning | [Page Topic]: Content Brief

[Keep all metadata sections from original brief unchanged]

---

## Headings/Sections

**H1:** *[headline]*

*[intro text drafted in Step 6]*

[(word count per page type): instruction text for intro]

  **H2:** *[headline]*

  [(30-40 words): instruction text]

    **H3:** *[headline]*

    [(20-30 words): instruction text]

    **H3:** *[headline]*

    [(35-50 words): instruction text]

  **H2:** *[headline]*

  [(15-20 words): instruction text]

  [Include special element note if applicable]

  **H2:** *Frequently Asked Questions*

    **H3:** *[FAQ question]?*

    [(50-75 words): instruction text]

---

[Keep Internal Links and other sections unchanged]
```

### Confirmation Message

After saving:

```
=== CONTENT BRIEF WITH INSTRUCTIONS SAVED ===

File: ./Briefs/<folder-name>/content-brief-with-instructions.md
Status: ✓ Successfully saved

Instructions added:
- [X] H1 intro text with writing instruction
- [X] H2s with section context
- [X] H3s with subtopic guidance
- [X] FAQs with answer guidance
- [X] Special elements (tables, testimonials)
```

---

## Quality Checklist

Copy and verify:

```
Quality Checklist:
- [ ] H1 intro text has instruction matching page-type word count
- [ ] Each H2 has instruction with appropriate word count
- [ ] Each H3 has instruction with appropriate word count
- [ ] FAQ H3s use (50-75 words) range
- [ ] All instructions in [(word count): text] format
- [ ] No line breaks within instruction brackets
- [ ] Special elements noted (tables, testimonials)
- [ ] Brand guidelines followed in instruction language
- [ ] File saved as content-brief-with-instructions.md
```

---

## Reference Materials

When writing instructions, reference:
- **[../brand-guidelines.md](../brand-guidelines.md)** — Tone and prohibited terms
- **Step 4 output** — Existing page content (if applicable)
- **Step 5 output** — Competitor insights
- **Step 1 inputs** — ICP, target audience, page context

---

## Error Handling

- **Cannot read brief from Step 7** → Verify file path, check Step 7 completed
- **Insufficient context** → Write general instructions based on headline topics, note limitations
- **File write fails** → Display content for manual save

---

## Next Step

The enhanced content brief with writing instructions is ready for handoff to the content writer.
