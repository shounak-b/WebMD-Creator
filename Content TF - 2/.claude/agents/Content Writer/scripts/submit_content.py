#!/usr/bin/env python3
"""
Submit markdown content to Google Apps Script endpoint
"""

import sys
import json
import requests

def submit_markdown(markdown_content):
    """
    Submit markdown content to the Google Apps Script endpoint

    Args:
        markdown_content: String containing the markdown content

    Returns:
        Response from the endpoint
    """
    endpoint = "https://script.google.com/macros/s/AKfycbwxn4Un_hR2eZRu96jIzXMEfsmw1mos5DECrg1pSU891hrCO8IjhbKvNOFfqiA8j90/exec"

    payload = {
        "markdown": markdown_content
    }

    try:
        response = requests.post(
            endpoint,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        response.raise_for_status()

        print("✓ Content submitted successfully")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        return response

    except requests.exceptions.RequestException as e:
        print(f"✗ Error submitting content: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python submit_content.py <markdown_file>", file=sys.stderr)
        print("   or: python submit_content.py - (read from stdin)", file=sys.stderr)
        sys.exit(1)

    # Read markdown from file or stdin
    if sys.argv[1] == "-":
        markdown_content = sys.stdin.read()
    else:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                markdown_content = f.read()
        except FileNotFoundError:
            print(f"✗ Error: File '{sys.argv[1]}' not found", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"✗ Error reading file: {e}", file=sys.stderr)
            sys.exit(1)

    if not markdown_content.strip():
        print("✗ Error: No content to submit", file=sys.stderr)
        sys.exit(1)

    submit_markdown(markdown_content)

if __name__ == "__main__":
    main()
