"""
Serper.dev Web Scraper
======================
This script uses the Serper.dev API to scrape web page content.

Usage:
    python serper_scraper.py <url>

Example:
    python serper_scraper.py "https://www.example.com"
    OR
    python3 serper_scraper.py "https://www.example.com"

Environment Variables:
    SERPER_API_KEY: Your Serper.dev API key (required)

Dependencies:
    - requests: HTTP library for API calls
"""

import os
import sys
import json
import requests

SERPER_API_KEY = "dc45df0e83e0f9e5751fde7afdac3c2996501502"

def scrape_url(target_url, api_key=None):
    """
    Scrape a URL using Serper.dev API.

    Args:
        target_url (str): The URL to scrape
        api_key (str, optional): Serper.dev API key. If not provided, reads from env.

    Returns:
        dict: Parsed JSON response from Serper.dev

    Raises:
        ValueError: If API key is not provided
        requests.RequestException: If API request fails
    """
    # Get API key from parameter, environment variable, or hardcoded constant
    if api_key is None:
        api_key = os.environ.get('SERPER_API_KEY', SERPER_API_KEY)

    if not api_key:
        raise ValueError(
            "API key not found. Set SERPER_API_KEY environment variable or pass as parameter."
        )

    # Serper.dev scraping endpoint
    url = "https://scrape.serper.dev"

    # Request payload
    payload = {
        "url": target_url
    }

    # Request headers
    headers = {
        'X-API-KEY': api_key,
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
        print("Usage: python serper_scraper.py <url>", file=sys.stderr)
        print("Example: python serper_scraper.py 'https://www.example.com'", file=sys.stderr)
        sys.exit(1)

    target_url = sys.argv[1]

    try:
        # Scrape the URL
        result = scrape_url(target_url)

        # Print full response
        print(json.dumps(result, indent=2))

        # Extract and display word count if text is available
        if 'text' in result:
            word_count = estimate_word_count(result['text'])
            print(f"\n--- Word Count: {word_count} ---", file=sys.stderr)

    except Exception as e:
        print(f"Failed to scrape URL: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
