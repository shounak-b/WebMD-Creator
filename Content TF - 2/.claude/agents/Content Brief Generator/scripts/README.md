# Available Scripts

Documentation for all executable scripts used in the Landing Page Content Brief Generator workflow.

---

## serper_search.py

Search Google using the Serper.dev API.

**Purpose:** Execute Google searches, including site-specific searches for competitor analysis.

**Usage:**
```bash
python3 scripts/serper_search.py "<search query>"
```

**Examples:**
```bash
# Basic search
python3 scripts/serper_search.py "CHO cell culture media"

# Site-specific search (competitor analysis)
python3 scripts/serper_search.py "site:sigmaaldrich.com \"cell culture media\""

# Multiple keywords
python3 scripts/serper_search.py "serum-free CHO media bioprocessing"
```

**Output:**
Returns JSON with search results structure:
```json
{
  "organic": [
    {
      "title": "Page Title",
      "link": "https://example.com/page",
      "snippet": "Preview text...",
      "position": 1
    }
  ],
  "knowledgeGraph": { ... },
  "answerBox": { ... }
}
```

**Key Fields:**
- `organic[]` — Array of organic search results
- `organic[0].link` — URL of the first result (most relevant)
- `organic[0].title` — Title of the search result

**Error Handling:**
- If API key not set → Error message "API key not found"
- If no results found → Empty `organic` array
- If query too long → Trim to reasonable length

**API Requirements:**
- Requires `SERPER_API_KEY` environment variable (or hardcoded in script)
- Rate limits apply per Serper.dev API plan

---

## linkup_scraper.py

Extract markdown content from any URL using the Linkup API.

**Purpose:** Scrape web pages and convert HTML to clean markdown for headline extraction.

**Usage:**
```bash
python3 scripts/linkup_scraper.py "<url>"
```

**Examples:**
```bash
# Scrape existing page
python3 scripts/linkup_scraper.py "https://www.thermofisher.com/us/en/home/bioprocessing/cell-culture.html"

# Scrape competitor page
python3 scripts/linkup_scraper.py "https://www.sigmaaldrich.com/US/en/products/cell-culture/media"

# Scrape for headline analysis
python3 scripts/linkup_scraper.py "https://www.cytivalifesciences.com/en/us/cell-culture"
```

**Output:**
Returns JSON with scraped content:
```json
{
  "text": "# Main Headline\n\n## Subheading\n\nParagraph text...",
  "url": "https://example.com/page",
  "status": "success"
}
```

**Key Fields:**
- `text` — Markdown-formatted page content with headlines preserved
- `url` — The URL that was scraped
- `status` — Success/error status

**Headline Extraction:**
After getting the `text` field, parse for markdown headlines:
- `# Heading` → H1
- `## Heading` → H2
- `### Heading` → H3

**Error Handling:**
- If API key not set → Error message "LINKUP_API_KEY not configured"
- If URL invalid → Error message "Invalid URL format"
- If page unreachable → Empty `text` field or error status
- If content empty → `text` field is empty string

**API Requirements:**
- Requires `LINKUP_API_KEY` environment variable (or hardcoded in script)
- Rate limits apply per Linkup API plan
- Some pages may block scraping (will return empty content)

---

## serper_scraper copy.py

*Note: This appears to be a duplicate/backup file of linkup_scraper.py.*

Legacy web scraper using Serper.dev scraping endpoint.

**Current Usage:** Not actively used in main workflow. Consider using `linkup_scraper.py` instead.

**Purpose:** Alternative scraping method if Linkup API is unavailable.

---

## Quick Usage Patterns

### Pattern 1: Competitor Headline Analysis (Step 6)

```bash
# 1. Search competitor site for keyword
python3 scripts/serper_search.py "site:competitor.com \"primary keyword\""

# 2. Extract first result URL from JSON output
# Parse organic[0].link from the JSON response

# 3. Scrape that URL
python3 scripts/linkup_scraper.py "https://competitor.com/result-url"

# 4. Extract headlines from the text field
# Parse markdown for #, ##, ### headings
```

**Example:**
```bash
# Search
python3 scripts/serper_search.py "site:sigmaaldrich.com \"CHO media\""
# Result: {"organic": [{"link": "https://www.sigmaaldrich.com/.../cho-media"}]}

# Scrape
python3 scripts/linkup_scraper.py "https://www.sigmaaldrich.com/.../cho-media"
# Result: {"text": "# CHO Media Solutions\n\n## Portfolio\n..."}

# Parse headlines manually from markdown
```

---

### Pattern 2: Existing Page Analysis (Step 5)

```bash
# If existing page URL provided
python3 scripts/linkup_scraper.py "https://www.thermofisher.com/existing-page"

# Parse JSON response for text field
# Extract H1, H2, H3 headlines from markdown
```

---

### Pattern 3: Word Count Research (Step 2)

While scripts don't directly calculate word count, you can:

1. Use `serper_search.py` to find top 5 results
2. Manually visit URLs or use `linkup_scraper.py` to get content
3. Estimate word count from scraped `text` field

```bash
# Get top 5 URLs
python3 scripts/serper_search.py "primary keyword"

# Scrape each top result (manual loop)
python3 scripts/linkup_scraper.py "<result_url_1>"
python3 scripts/linkup_scraper.py "<result_url_2>"
# ... etc
```

---

## Debugging Tips

**If serper_search.py fails:**
1. Check API key is set correctly
2. Verify query format (use quotes for exact match)
3. Check if rate limit exceeded
4. Ensure query is not too long

**If linkup_scraper.py fails:**
1. Check API key is set correctly
2. Verify URL is accessible in browser
3. Check if site blocks scraping
4. Try alternative URL for same content

**If JSON parsing fails:**
1. Print raw output to see actual response
2. Check for error messages in stderr
3. Verify JSON structure matches expected format

---

## Environment Variables

Both scripts can use environment variables or hardcoded API keys.

**Setting environment variables (optional):**

```bash
# macOS/Linux
export SERPER_API_KEY="your_key_here"
export LINKUP_API_KEY="your_key_here"

# Or add to ~/.bashrc or ~/.zshrc
echo 'export SERPER_API_KEY="your_key"' >> ~/.zshrc
echo 'export LINKUP_API_KEY="your_key"' >> ~/.zshrc
```

**Note:** Current scripts have API keys hardcoded, so environment variables are optional.

---

## Script Maintenance

**Location:**
All scripts are in: `scripts/` directory

**Dependencies:**
- Python 3.x
- `requests` library (install via: `pip install requests`)

**Updating API keys:**
Edit the script files and update the constant:
```python
SERPER_API_KEY = "your_new_key_here"
LINKUP_API_KEY = "your_new_key_here"
```

---

## Common Issues

**Issue:** "Module 'requests' not found"
**Solution:** Install requests: `pip install requests` or `pip3 install requests`

**Issue:** "Permission denied"
**Solution:** Make script executable: `chmod +x scripts/*.py`

**Issue:** "API rate limit exceeded"
**Solution:** Wait before retrying, or upgrade API plan

**Issue:** "Empty text field returned"
**Solution:** Page may block scraping; try alternative URL or manual review
