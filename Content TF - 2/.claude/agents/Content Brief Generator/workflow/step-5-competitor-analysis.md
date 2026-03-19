# Step 5: Extract Unique Headlines and FAQs from Competitors

**Goal:** Extract only the unique headlines and FAQ questions from competitor landing pages by searching each competitor domain for the Primary Keyword.

---

## Why This Matters

Collecting unique headlines and FAQs from competitors helps identify content gaps and common questions that should be addressed in the landing page. By searching within each competitor domain, we get their most relevant page for the Primary Keyword.

---

## Instructions

A. **Prepare Site-Specific Searches:**
   - Use the **Primary Keyword** from Step 1
   - Use the **Competitor Domains** from Step 1 (comma-separated list)
   - For each competitor domain, construct a site-specific search query:
     - Format: `site:<competitor_domain> "<primary_keyword>"`
     - Example: `site:sigmaaldrich.com "cell culture media"`

B. **Execute Site-Specific Searches:**
   - For EACH competitor domain, execute a separate search using serper_search.py:
     `python3 scripts/serper_search.py "site:<competitor_domain> \"<primary_keyword>\""`
   - Example: `python3 scripts/serper_search.py "site:sigmaaldrich.com \"cell culture media\""`
   - Repeat for each competitor domain provided in Step 1

C. **Extract Top Ranking URL from Each Search:**
   - Parse the JSON output from each search
   - Extract URLs from the `organic` array
   - **Take ONLY the first result (position 0)** from each competitor search
   - Extract the `link` field from the first result
   - If a search returns no results, skip that competitor and continue

D. **Apply Hard Cap on Total URLs:**
   - **CRITICAL:** Collect a maximum of 5 URLs total across all competitor searches
   - If you have more than 5 competitor domains, only process the first 5 domains
   - **DO NOT scrape more than 5 URLs under any circumstances**

E. **Scrape Each Top-Ranking URL:**
   - For each collected URL (max 5), use the Bash tool to execute the linkup_scraper.py script:
     `python3 scripts/linkup_scraper.py "<url>"`
   - If the script fails or the `text` field is empty, skip that URL and continue to the next
   - **REMINDER:** Maximum 5 URLs scraped total
   - **NOTE:** The linkup_scraper.py script can only be used 5 times maximum per workflow execution

F. **Extract Headlines and FAQs from Each Page:**
   - Parse the `text` field containing markdown content from the scraper output
   - Identify all H1, H2, and H3 headlines
   - Identify all FAQ questions (look for FAQ sections, Q&A sections, or question patterns)
   - If no headlines or FAQs are found, skip that page

G. **Deduplicate and Compile Unique Items:**
   - After collecting all headlines and FAQs from the URLs (max 5), deduplicate them
   - Remove exact duplicates (case-insensitive comparison)
   - Keep only unique headlines and unique FAQ questions
   - For headlines, preserve the H1, H2, or H3 tag with each headline
   - Output format: "H1: [headline text]", "H2: [headline text]", etc.
   - Do not include any other information

---

## Output Format

```
=== UNIQUE HEADLINES ===

H1: [Unique headline 1]
H2: [Unique headline 2]
H3: [Unique headline 3]
H1: [Unique headline 4]
[...]

=== UNIQUE FAQs ===

[Unique FAQ question 1]
[Unique FAQ question 2]
[Unique FAQ question 3]
[...]
```

---

## Error Handling

- If a site-specific search returns no results for a competitor domain → Skip that competitor and continue to next domain
- If the scraper fails for a URL → Note "Could not scrape <url>" and skip to next URL
- If no headlines or FAQs are found in the markdown → Skip that page
- If the SERPER_API_KEY or LINKUP_API_KEY is not set → Output appropriate error message
- If more than 5 competitor domains are provided → Only process the first 5 domains
- **REMINDER:** Never scrape more than 5 URLs regardless of availability

For standard error handling patterns, see [common-patterns.md](common-patterns.md).

---

## Example Execution

**Given:**
- Primary Keyword: "employee well-being program"
- Competitor Domains: "personifyhealth.com, sharecare.com, vitality.com"

**Step-by-step:**

1. **Search site:personifyhealth.com "employee well-being program"**
   - Get 1st ranking URL: https://personifyhealth.com/employee-well-being

2. **Search site:sharecare.com "employee well-being program"**
   - Get 1st ranking URL: https://www.sharecare.com/employer/well-being

3. **Search site:vitality.com "employee well-being program"**
   - Get 1st ranking URL: https://www.vitality.com/employers/wellness

4. **Scrape each URL** (max 5 total)
   - Scrape URL 1, extract headlines and FAQs
   - Scrape URL 2, extract headlines and FAQs
   - Scrape URL 3, extract headlines and FAQs

5. **Deduplicate and output unique items**

**WebMD Health Services' Known Competitors** (use as defaults if the user doesn't provide competitor domains):
- personifyhealth.com — formerly Virgin Pulse; comprehensive well-being platform
- sharecare.com — health and well-being platform; often competes in public sector
- vitality.com — incentive-based well-being and insurance programs
- wellhub.com — formerly Gympass; fitness and wellness benefit platform
- springhealth.com — mental health benefits platform

---

## Example Output

```
=== UNIQUE HEADLINES ===

H1: Employee Well-Being Programs for the Whole Person
H2: Address all five dimensions of well-being.
H3: Physical fitness and daily habit building.
H3: Mental health and emotional resilience.
H2: Incentive-based programs that drive participation.
H3: Rewards that motivate lasting behavior change.
H3: Points and challenges built into the platform.
H1: Well-Being Solutions for Employers and Health Plans
H2: How our platform supports workforce health.
H2: Integrate with your existing benefits ecosystem.
H3: Single sign-on and HR system connections.
H3: Health plan and EAP integrations.

=== UNIQUE FAQs ===

What is an employee well-being program?
How is well-being different from wellness?
Can well-being programs be customized for different employee populations?
Does the platform support remote and hybrid workforces?
How do well-being programs reduce healthcare costs?
What data and reporting is available to HR leaders?
Is the platform suitable for large enterprise and mid-market organizations?
```

---

## Quality Checks

- [ ] Executed site-specific search for EACH competitor domain
- [ ] Each search uses format: `site:<domain> "<primary_keyword>"`
- [ ] Extracted only the 1st ranking URL from each competitor search
- [ ] Applied hard cap: maximum 5 competitor domains processed
- [ ] Verified hard cap: no more than 5 URLs were scraped total
- [ ] Attempted to scrape each collected URL
- [ ] Extracted H1, H2, and H3 headlines where available
- [ ] Extracted FAQ questions where available
- [ ] Deduplicated all headlines and FAQs
- [ ] Output contains ONLY unique headlines and unique FAQs

---

## Next Step

Proceed to [Step 6: Generate Content Brief](step-6-generate-brief.md).
