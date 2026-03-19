# Step 2: Determine Target Word Count Range

**Goal:** Analyze top-performing SERP results to establish an evidence-based word count range for the target page.

---

## Instructions

A. **Research the top 5 SERP results** for the exact query using the Primary Keyword from Step 1.

B. **For each of the top 5 results:**
   - Estimate the word count of the main content area (excluding navigation, headers, footers, sidebars, and boilerplate text)

C. **Calculate the average word count** across all 5 results.

D. **Apply the word count range for the Page Type provided in Step 1:**

   | Page Type     | Min (floor) | Max (ceiling) |
   |---------------|-------------|---------------|
   | Landing page  | 500         | 1500          |
   | Service page  | 500         | 1200          |
   | Category page | 300         | 800           |
   | Blog          | 1100        | 2500          |
   | Pillar page   | 2000        | 4000          |

   Use the SERP average from Step C to position the recommendation within the range for that page type. If the SERP average falls below the floor, use the floor. If it exceeds the ceiling, use the ceiling.

---

## Output Format

```
Recommended word count Range: [MIN]-[MAX] words
```

---

## Example

```
SERP Analysis for "resource scheduling software":
- Result 1: ~900 words
- Result 2: ~1100 words
- Result 3: ~850 words
- Result 4: ~1050 words
- Result 5: ~950 words

Average: 970 words
Page Type: Landing page → Allowed range: 500–1500 words

SERP average (970) falls within the allowed range.
Recommended word count Range: 800-1100 words
```

---

## Next Step

Proceed to [Step 3: Identify Internal Linking Opportunities](step-3-internal-linking.md).
