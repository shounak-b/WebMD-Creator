"""
Serper.dev Search API
=====================
This script uses the Serper.dev API to perform Google searches.

Usage:
    python serper_search.py <query>

Example:
    python serper_search.py "apple inc"
    OR
    python3 serper_search.py "apple inc"

Environment Variables:
    SERPER_API_KEY: Your Serper.dev API key (optional, hardcoded by default)

Dependencies:
    - requests: HTTP library for API calls
"""

import os
import sys
import json
import requests

SERPER_API_KEY = "dc45df0e83e0f9e5751fde7afdac3c2996501502"

def search_query(query, api_key=None):
    """
    Search using Serper.dev API.

    Args:
        query (str): The search query
        api_key (str, optional): Serper.dev API key. If not provided, uses hardcoded key.

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

    # Serper.dev search endpoint
    url = "https://google.serper.dev/search"

    # Request payload
    payload = {
        "q": query
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
        print(f"Error performing search: {e}", file=sys.stderr)
        raise


def extract_results_summary(results):
    """
    Extract and format search results summary.

    Args:
        results (dict): Search results from Serper.dev

    Returns:
        str: Formatted summary of results
    """
    if not results:
        return "No results found."

    summary = []

    # Extract organic results
    if 'organic' in results:
        summary.append(f"Found {len(results['organic'])} organic results")

    # Extract knowledge graph
    if 'knowledgeGraph' in results:
        summary.append("Knowledge graph available")

    # Extract answer box
    if 'answerBox' in results:
        summary.append("Answer box available")

    return " | ".join(summary) if summary else "Results retrieved"


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python serper_search.py <query>", file=sys.stderr)
        print("Example: python serper_search.py 'apple inc'", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]

    try:
        # Perform search
        result = search_query(query)

        # Print full response
        print(json.dumps(result, indent=2))

        # Display summary
        summary = extract_results_summary(result)
        print(f"\n--- {summary} ---", file=sys.stderr)

    except Exception as e:
        print(f"Failed to perform search: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
