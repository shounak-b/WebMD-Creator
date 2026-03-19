# Step 4: Extract Existing Page Headlines (Optional)

**Goal:** If an existing page URL is provided, extract the page content and identify all headlines to understand the current content structure and approach.

---

## When to Execute

- This step ONLY runs if the user provided an **Existing Page URL** in Step 1
- If no existing page URL was provided, skip this step entirely and proceed to Step 5

---

## Instructions

A. **Check for Existing Page URL:**
   - Review the information collected in Step 1
   - If the "Existing Page URL" field is empty or not provided, output "No existing page URL provided - skipping headline extraction" and proceed to Step 5
   - If a URL is provided, continue with the extraction process

B. **Execute the Page Scraper:**
   - Use the Bash tool to execute the linkup_scraper.py script:
     `python3 scripts/linkup_scraper.py "<existing_page_url>"`

C. **Parse the Scraper Output:**
   - The script returns JSON containing a `text` field with the page markdown content
   - If the script fails or returns an error, output "NA" and proceed to Step 5
   - If successful, extract the `text` field for headline parsing

D. **Extract and Format Headlines:**
   - Parse the extracted text/markdown content to identify all H1, H2, and H3 headlines
   - If no headlines are found, output "NA" and proceed to Step 5

E. **Structure the Output:**
   - Present headlines in hierarchical order as they appear in the content

---

## Output Format

```
=== Existing Page Headlines ===

H1: [Main headline text]

H2: [Subheading text]

H2: [Another subheading]

H3: [Sub-subheading]

[Continue for all headlines...]
```

---

## Important Rules

- Only return headlines that actually exist in the scraped content
- Maintain the original order and hierarchy of headlines from the source page
- If the scraping fails at any point, return: `Extraction failed: NA`
- If no existing page URL was provided, return: `No existing page URL provided - skipping headline extraction`

---

## Error Handling

- If the linkup_scraper.py script returns an error → Output "NA"
- If the LINKUP_API_KEY is not set → Output "NA" with error message
- If the URL is invalid or unreachable → Output "NA"
- If the JSON parsing fails → Output "NA"
- If the markdown content is empty → Output "Empty content - NA"

For standard error handling patterns, see [common-patterns.md](common-patterns.md).

---

## Example Output

```
=== Existing Page Headlines ===

H1: Employee Well-Being Programs for Large Employers

H2: Support all five dimensions of well-being.

H3: Physical fitness and daily habit building.

H3: Mental health coaching and stress resilience.

H2: One platform for your whole population.

H2: Clients who trust WebMD Health Services.

H3: Results from large employers.

H3: Results from health plans.
```

---

## Quality Checks

- [ ] Script execution attempted only if existing page URL is provided
- [ ] Script output captured and parsed successfully
- [ ] All H1, H2, and H3 headlines extracted
- [ ] Hierarchical structure preserved
- [ ] Error cases handled gracefully with "NA" output

---

## Next Step

Proceed to [Step 5: Analyze Competitor Headlines](step-5-competitor-analysis.md).
