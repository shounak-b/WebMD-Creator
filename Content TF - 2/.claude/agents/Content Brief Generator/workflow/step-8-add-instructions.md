# Step 8: Add Writing Instructions Under Each Headline

Add bracketed writing instructions with word counts under each headline to guide the content writer.

**Prerequisite:** User must approve the content brief from Step 7 before proceeding.

**🚨 CRITICAL OUTPUT REQUIREMENT:**
- ALL instructions MUST be output as **PLAIN TEXT**, NOT in markdown code blocks
- NEVER use ``` markers around instructions
- Format: `[(X words): Discuss/highlight/explain/note...]`
- Instructions appear as regular text paragraphs under each headline

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

**🚨 CRITICAL: Output ALL instructions as plain text paragraphs. NEVER wrap in markdown code blocks (no ``` markers).**

**Format:** `[(word count): instruction text]`

**Example:**
**H2:** *Why HR leaders choose WebMD Health Services.*

[(30-40 words): Highlight the top reasons HR Directors, Benefits Managers, and CHROs choose WebMD Health Services. Lead with clinical credibility, the holistic five-dimension approach, and the human-centered coaching model as core differentiators versus point solutions.]

**Rules:**
- Square brackets containing word count and instruction
- Word count in parentheses at start: `(15-20 words):` or `(20 words):` or `(30-40 words):`
- Instruction describes what to write, not the actual content
- Single paragraph, no line breaks within brackets
- Output as plain text directly under the headline

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

**Example:**

**H1:** *Employee Well-Being Programs for Large Employers*

*[intro text drafted in Step 6]*

[(15-20 words): Introduce WebMD Health Services as a clinically grounded well-being partner. Concisely answer the "how" — lead with the holistic, five-dimension approach and the breadth of the platform.]

### First H2 (Problem/Challenge Section)

Frame the challenge the target audience faces.

**Example:**

**H2:** *Why fragmented point solutions fail your workforce.*

[(30-40 words): Acknowledge that as large employers invest in multiple disconnected well-being tools, employees disengage due to irrelevant experiences, HR struggles to prove ROI, and healthcare costs remain high. Frame this as the case for a unified platform approach.]

### Standard H2

Explain what the section covers and why it matters.

**Example:**

**H2:** *One platform for holistic employee well-being.*

[(30-40 words): Introduce WebMD ONE as the core platform that unifies physical, emotional, social, financial, and clinical well-being into a single, connected experience. Explain how it supports employers in delivering a personalized program at scale.]

### H3 (Subtopics)

Provide specific guidance for the subtopic.

**Example:**

**H3:** *WebMD ONE — the core well-being platform.*

[(20-30 words): Describe WebMD ONE's key capabilities — Health Assessment, Wellness Challenges, Daily Habits, Digital Coaching, and Benefits Navigation — and explain how the platform drives behavior change across all five dimensions of well-being.]

### H3 (FAQ Questions)

Guide how to answer each FAQ with more detail.

**Example:**

**H3:** *How does WebMD Health Services differ from competitors?*

[(50-75 words): Explain that unlike digital-only or fitness-focused platforms (Personify Health, Wellhub), WebMD Health Services offers the only solution that includes the Clinical dimension of well-being — chronic condition management and preventive care — alongside the other four dimensions. Highlight the WebMD brand trust, 25+ years of clinical credibility, award-winning health coaching, and the Clinical Advisory Board as key differentiators unavailable elsewhere.]

---

## Special Elements

### Tables

Include table instructions in brackets.

**Example:**

**H2:** *WebMD Health Services vs. the competition.*

[(15-20 words): Introduce a feature comparison table that should be included below. Frame it as a straightforward way for HR leaders to compare well-being platforms across the dimensions that matter most to them.]

[Include a feature comparison table. Columns: WebMD Health Services, Personify Health, Sharecare, Vitality, Wellhub. Rows should include dimensions covered (physical, emotional, social, financial, clinical), health coaching (human-led), WebMD brand trust, Clinical Advisory Board, available countries/languages, and average client health improvement. Use checkmarks for supported features.]

### Testimonials

**Example:**

**H2:** *What our clients are saying.*

[Include a testimonial carousel with 3-5 client testimonials. Each testimonial should include a name, title, organization type (for example, large employer or health plan), and a brief quote emphasizing engagement outcomes, behavior change, healthcare cost reduction, or strategic partnership value.]

---

## Output Format

### File Structure

Save as `content-brief-with-instructions.md` in the same folder as the original brief.

**Example structure:**

# WebMD Health Services | [Page Topic]: Content Brief

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
