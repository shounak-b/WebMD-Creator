"""
Page Finder
===========
This script calls the n8n webhook to find relevant pages for a given domain and keyword.

Usage:
    python page_finder.py <domain> <keyword>

Example:
    python page_finder.py "thermofisher.com" "fill finish"
    OR
    python3 page_finder.py "thermofisher.com" "fill finish"

Dependencies:
    - requests: HTTP library for API calls
"""

import sys
import json
import requests

WEBHOOK_URL = "https://n8n.srv1110631.hstgr.cloud/webhook/0f9098d0-62f6-4eb7-93a5-09325de5ce40"


def find_pages(domain, keyword):
    """
    Find relevant pages for a domain and keyword via n8n webhook.

    Args:
        domain (str): The domain to search within (e.g. "thermofisher.com")
        keyword (str): The keyword to search for (e.g. "fill finish")

    Returns:
        dict: Parsed JSON response from the webhook

    Raises:
        requests.RequestException: If the request fails
    """
    # Request payload
    payload = {
        "domain": domain,
        "keyword": keyword
    }

    # Request headers
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Make webhook request
        response = requests.post(WEBHOOK_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        # Return parsed JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error calling webhook: {e}", file=sys.stderr)
        raise


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 3:
        print("Usage: python page_finder.py <domain> <keyword>", file=sys.stderr)
        print("Example: python page_finder.py 'thermofisher.com' 'fill finish'", file=sys.stderr)
        sys.exit(1)

    domain = sys.argv[1]
    keyword = sys.argv[2]

    try:
        result = find_pages(domain, keyword)

        # Print full response
        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Failed to find pages: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
