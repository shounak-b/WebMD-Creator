# Step 3: Identify Relevant Pages for Internal Linking

**Goal:** Discover topically relevant pages within the site using Google Search Console data to build a strategic internal linking plan that supports SEO for the Primary Keyword.

---

## Instructions

1. **Run the Page Finder script** to pull GSC data for the target domain and Primary Keyword:
   ```
   python3 page_finder.py "<domain>" "<primary keyword>"
   ```
   This returns a list of pages and keywords from Google Search Console ranked by performance.

2. **Parse the response:**
   - The response contains a `rows` array
   - Each row has a `keys` array: `[keyword, url]`
   - Each row also includes `clicks`, `impressions`, `ctr`, and `position`

3. **Filter by ranking position:**
   - Only consider rows where `position` is between **1 and 15**
   - These are pages already ranking and visible in search

4. **Group rows by URL:**
   - Multiple rows may share the same URL (different keywords ranking for the same page)
   - Group all qualifying rows by their URL (`keys[1]`)

5. **Select anchor text per URL:**
   - For each URL, evaluate all its qualifying keywords
   - Prefer keywords with the highest combination of **impressions** and **clicks**
   - The keyword in `keys[0]` of the best-performing row becomes the **anchor text** for that URL

6. **Select the 2-5 most relevant pages:**
   - Evaluate each URL's topical relevance to the **Primary Keyword** from Step 1
   - Prioritize pages that directly support or complement the primary topic
   - Prefer pages with stronger GSC signals (higher impressions + clicks)

---

## Output Format

For each selected page, provide:
- **URL** — The page URL from `keys[1]`
- **Anchor Text** — The best-performing keyword from `keys[0]` for that URL (position 1–15, ranked by impressions + clicks)

---

## Example Output

```
1. URL: https://www.webmdhealthservices.com/well-being-platform/
   Anchor Text: employee well-being platform

2. URL: https://www.webmdhealthservices.com/health-coaching/
   Anchor Text: health coaching program

3. URL: https://www.webmdhealthservices.com/wellness-challenges/
   Anchor Text: wellness challenges
```

**Note:** WebMD Health Services' website domain is `webmdhealthservices.com`. Use this domain when running the `page_finder.py` script.

---

## Quality Checks

- [ ] `page_finder.py` was run with the correct domain and Primary Keyword
- [ ] Only rows with `position` 1–15 were considered
- [ ] Anchor text is a real keyword the page ranks for (not invented or paraphrased)
- [ ] Anchor text selection prioritised impressions and clicks
- [ ] 2–5 pages selected based on topical relevance to the Primary Keyword
- [ ] Output contains only URL and Anchor Text (no page name, level, or relevancy score)

---

## Next Step

Proceed to [Step 4: Extract Existing Page Headlines](step-4-existing-content.md) if an Existing Page URL was provided. Otherwise, skip to [Step 5: Analyze Competitor Headlines](step-5-competitor-analysis.md).
