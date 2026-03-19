"""
LinkUp Web Scraper
==================
This script uses the LinkUp API to scrape web page content.

Usage:
    python linkup_scraper.py <url>

Example:
    python linkup_scraper.py "https://www.example.com"
    OR
    python3 linkup_scraper.py "https://www.example.com"

Environment Variables:
    LINKUP_API_KEY: Your LinkUp API key (required)

Dependencies:
    - requests: HTTP library for API calls
"""

import os
import sys
import json
import requests

LINKUP_API_KEY = "53c86d99-c2e3-4e54-b4a2-4ce660f7393d"

def scrape_url(target_url, api_key=None, include_raw_html=False, render_js=False, extract_images=False):
    """
    Scrape a URL using LinkUp API.

    Args:
        target_url (str): The URL to scrape
        api_key (str, optional): LinkUp API key. If not provided, reads from env.
        include_raw_html (bool): Whether to include raw HTML in response
        render_js (bool): Whether to render JavaScript
        extract_images (bool): Whether to extract images

    Returns:
        dict: Parsed JSON response from LinkUp

    Raises:
        ValueError: If API key is not provided
        requests.RequestException: If API request fails
    """
    # Get API key from parameter, environment variable, or hardcoded constant
    if api_key is None:
        api_key = os.environ.get('LINKUP_API_KEY', LINKUP_API_KEY)

    if not api_key:
        raise ValueError(
            "API key not found. Set LINKUP_API_KEY environment variable or pass as parameter."
        )

    # LinkUp API endpoint
    url = "https://api.linkup.so/v1/fetch"

    # Request payload
    payload = {
        "url": target_url,
        "include_raw_html": include_raw_html,
        "render_js": render_js,
        "extract_images": extract_images
    }

    # Request headers
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        # Return parsed JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error scraping URL: {e}", file=sys.stderr)
        raise


def estimate_word_count(text):
    """
    Estimate word count from scraped text.

    Args:
        text (str): Text content to analyze

    Returns:
        int: Estimated word count
    """
    if not text:
        return 0
    return len(text.split())


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python linkup_scraper.py <url>", file=sys.stderr)
        print("Example: python linkup_scraper.py 'https://www.example.com'", file=sys.stderr)
        sys.exit(1)

    target_url = sys.argv[1]

    try:
        # Scrape the URL
        result = scrape_url(
            target_url,
            include_raw_html=False,
            render_js=False,
            extract_images=False
        )

        # Print full response
        print(json.dumps(result, indent=2))

        # Extract and display word count if text is available
        if 'text' in result or 'content' in result:
            text_content = result.get('text') or result.get('content', '')
            word_count = estimate_word_count(text_content)
            print(f"\n--- Word Count: {word_count} ---", file=sys.stderr)

    except Exception as e:
        print(f"Failed to scrape URL: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
