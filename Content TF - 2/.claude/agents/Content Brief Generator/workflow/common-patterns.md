# Common Patterns

This file contains shared templates, error handling patterns, and quality checks used across workflow steps.

---

## Standard Error Handling

For all script executions, follow these patterns:

**Script execution failures:**
- If script fails → Output "NA" and continue to next step
- If API key not set → Output "NA" with error message "API key not configured"
- If URL invalid/unreachable → Output "NA" with note "URL not accessible"
- If JSON parsing fails → Output "NA" with note "Invalid response format"
- If content is empty → Output "Empty content - NA"

**File access failures:**
- If CSV file not found → Output error message with file path
- If CSV parsing fails → Output error and request manual verification

**Graceful degradation:**
- Always proceed to next step when encountering "NA"
- Note all failures in final NOTES section
- Never block the workflow completely

---

## Standard Output Format Template

Use consistent formatting across all steps:

```
=== [Section Title] ===

[Content organized hierarchically]

[Continue with structured data...]
```

**Formatting rules:**
- Use `===` for main section headers
- Use `---` for separators between items
- Maintain consistent indentation
- Use bullet points or numbered lists for clarity

---

## Quality Check Standard

Before proceeding to the next step, verify:

- [ ] Output generated successfully or "NA" noted
- [ ] Required information captured
- [ ] Error cases handled gracefully
- [ ] Output follows standard format
- [ ] Next step dependencies satisfied

---

## Script Execution Pattern

**Standard command format:**
```bash
python3 scripts/<script_name>.py "<argument>"
```

**Output capture:**
- Capture stdout as JSON
- Parse JSON for required fields
- Handle stderr separately for error messages

**Timeout handling:**
- Allow reasonable timeout for API calls (30-60 seconds)
- If timeout occurs, treat as "NA" and continue

---

## Data Validation Patterns

**URL validation:**
- Check for proper URL format (http:// or https://)
- Verify domain is accessible before scraping
- Handle redirects gracefully

**Keyword validation:**
- Ensure Primary Keyword is not empty
- Check for reasonable length (< 100 characters)
- Validate Secondary Keywords as comma-separated list

**Word count validation:**
- Ensure range has minimum ≥ 500
- Ensure range has maximum ≤ 1500
- Ensure minimum < maximum

---

## Headline Quality Checks

**SEO compliance:**
- [ ] Exactly 1 H1
- [ ] H1 includes Primary Keyword
- [ ] Multiple H2s as major sections
- [ ] H3s only appear under H2s
- [ ] No H4 or deeper levels

**Character limits:**
- [ ] All headlines ≤ 60 characters
- [ ] Primary Keyword appears naturally in H1
- [ ] Secondary Keywords distributed across H2/H3

**Logical flow:**
- [ ] Headlines follow readable progression
- [ ] Related content grouped under appropriate H2s
- [ ] No orphaned H3s without parent H2

---

## Brand Compliance Checks

**Prohibited term scan (WebMD Health Services):**
- [ ] No clichés: "rest assured", "now more than ever", "in order to", "with that being said"
- [ ] No unproven superlatives: "world-class", "best-in-class", "premier", "unique", "revolutionary", "game-changing", "perfect", "most powerful"
- [ ] No absolute claims: "guarantee(s) health outcomes", "eliminate health risks", "100% engagement", "always", "never" (as blanket absolutes)
- [ ] No wrong terms: "WHS" (use "WebMD" or "WebMD Health Services"), "preventative" (use "preventive"), "customers/consumers" (use "clients"), "end-user" (use "participant", "employee", "member"), "well-being challenges" (use "wellness challenges"), "e.g.", "i.e.", "etc."

**Tense variation checks:**
- [ ] Check present, past, future forms (guarantee/guarantees/guaranteed/guaranteeing)
- [ ] Check plural forms (ensure/ensures/ensuring — replace with "help ensure", "support")
- [ ] Check related forms (revolutionary/revolutionize/revolutionizing)

**Tone compliance:**
- [ ] Collaborative and empathetic (not aggressive or boastful)
- [ ] Evidence-based and outcome-focused (not vague promises)
- [ ] Human-centered and personal (not cold or generic)
- [ ] Clinical credibility conveyed (not overly promotional)

**Capitalization checks (per WebMD editorial guidelines):**
- [ ] H1: Title Case — all major words capitalized
- [ ] H1 titles: "Well-Being" — both W and B capitalized
- [ ] H2–H3: Sentence case — first word and proper nouns only; ends with full stop
- [ ] "WebMD ONE", "ONE Partners", "Well-Being Services", "TINYpulse" — exact casing maintained
- [ ] "well-being" — always hyphenated in body copy; "wellness" only for single dimensions or "wellness challenges"

---

## Internal Linking Quality Checks

**Link specifications:**
- [ ] 3-5 links total (not too few, not overwhelming)
- [ ] Each link has target page name
- [ ] Each link has specific anchor text
- [ ] Each link has placement location (H2/H3 section)
- [ ] URLs use "Recommended URL Structure" from CSV

**Link distribution:**
- [ ] Links distributed across multiple sections
- [ ] No single section has more than 2 links
- [ ] Anchor text includes relevant keywords naturally
- [ ] Links support Primary Keyword context

---

## Meta Description Quality Checks

**Technical requirements:**
- [ ] Length is 150-160 characters
- [ ] Primary Keyword appears naturally
- [ ] No prohibited terminology used
- [ ] Action-oriented language

**Content requirements:**
- [ ] Summarizes page value proposition
- [ ] Appeals to target audience (ICP)
- [ ] Outcome-driven phrasing
- [ ] Clear and concise messaging

---

## Content Goal Quality Checks

**Structure:**
- [ ] 2-3 sentences total
- [ ] Written in future tense
- [ ] Framed from user's perspective

**Content:**
- [ ] Describes what page will accomplish
- [ ] References target audience by role
- [ ] Aligns with messaging pillars
- [ ] Connects to Primary Keyword intent
- [ ] Clear value proposition

---

## File Operation Patterns

**Folder naming convention:**
- Convert Page Name to lowercase
- Replace spaces with hyphens
- Remove special characters except hyphens
- Examples:
  - "Employee Well-Being Program" → `employee-well-being-program`
  - "Health Coaching Platform" → `health-coaching-platform`
  - "Well-Being Solutions for Health Plans" → `well-being-solutions-for-health-plans`

**Folder creation:**
```bash
mkdir -p "./Briefs/<folder-name>"
```

**File saving:**
- SEO brief filename: `content-brief.md` (from Step 8)
- Enhanced brief filename: `content-brief-with-instructions.md` (from Step 9)
- Full paths (relative to current working directory):
  - `./Briefs/<folder-name>/content-brief.md`
  - `./Briefs/<folder-name>/content-brief-with-instructions.md`

**File verification:**
```bash
ls -lh "./Briefs/<folder-name>/content-brief.md"
ls -lh "./Briefs/<folder-name>/content-brief-with-instructions.md"
```

**Error handling for file operations:**
- If folder creation fails → Check parent directory `./Briefs` exists and permissions
- If Briefs folder doesn't exist → Create it first: `mkdir -p ./Briefs`
- If file write fails → Check folder exists and permissions
- If folder already exists → OK to proceed (overwrite existing brief)
- If any error persists → Display error message and output brief for manual save

---

## Instruction Writing Patterns

**Instruction format requirements:**
- Single paragraph per heading (no line breaks)
- Target length: 600-800 characters for H2 sections, can be shorter for H3s
- Easily copyable into Google Docs
- Technical and outcome-focused tone

**Instruction content guidelines:**
- What will be discussed, explained, demonstrated, or highlighted
- Reference specific products, platforms, or capabilities
- Connect to business outcomes or process goals
- Describe technical aspects or workflow connections
- Align with target audience needs

**Special formatting rules:**

**H1 + Intro Text:**
- The H1 headline itself has no instruction
- Add a writing instruction for the intro text that follows the H1
- Word count varies by page type: (50-75 words) for blog/pillar pages; (15-20 words) for landing, service, and category pages

**First H2 only:**
- Challenge → Solution format
- First part: Introduce the problem/challenge
- Second part: Present the solution/approach
- Frame from audience perspective

**All other H2s:**
- Explain what the section will cover
- Reference specific products or capabilities when relevant
- Describe technical aspects or workflow connections
- Connect to business outcomes

**All H3s:**
- Provide subtopic context
- More specific than parent H2
- Reference technical details or specific products
- Explain relation to broader section theme

---

## Final Deliverable Checklist

Before presenting the final content brief:

- [ ] All 9 workflow steps completed (or NA documented)
- [ ] Headline structure follows SEO hierarchy
- [ ] Brand guidelines applied to all headlines
- [ ] Internal linking opportunities specified
- [ ] Target word count range provided (500-1500)
- [ ] Content goal written (2-3 future tense sentences)
- [ ] Meta description created (150-160 chars)
- [ ] NOTES section includes any limitations or NA items
- [ ] Quality checks passed for all sections
- [ ] Output follows standard format template
- [ ] Content brief saved to file in correct folder structure (Step 8)
- [ ] Writing instructions added under each headline (Step 9)
- [ ] Enhanced brief with instructions saved as `content-brief-with-instructions.md`
