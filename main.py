#!/usr/bin/env python3

"""
Regex Data Extraction Project

This script extracts various data types from a block of raw text using Python's re module.
It is designed to fulfill all requirements of the ALU Regex Onboarding Hackathon assignment.

Author: Vanessa Umwari
GitHub Repository: https://github.com/YOUR_USERNAME/alu_regex-data-extraction-YOUR_USERNAME
"""

import re

# Sample input string for testing
sample_data = """
    Emails: zaphira.qwenzi@ikoranotech.rw, thabiso.mutema@afrosolutions.africa
    URLs: https://www.kigalitech.rw, https://portal.savannah-hub.org/projects
    Phones: (250) 789-123456, 0788-456-789, 0722.333.111
    Credit Cards: 4578 3456 7890 1234, 6011-7821-4321-9087
    Times: 09:45, 11:59 PM
    HTML: <header>, <section class="hero">, <img src="logo.png" alt="Company Logo">
    Hashtags: #CodeRwanda, #Tech4Good
    Currency: $8,745.99, $342.00
"""

# Dictionary of regex patterns
patterns = {
    "Email Addresses": r"[\w.-]+@[\w.-]+\.\w+",
    "URLs": r"https?://[\w./-]+",
    "Phone Numbers": r"(?:\(\d{3}\)[ ]?|\d{3}[-.])\d{3}[-.]\d{4}",
    "Credit Card Numbers": r"\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}",
    "Times (12/24 hour)": r"(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?",
    "HTML Tags": r"<[^>]+>",
    "Hashtags": r"#\w+",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

# Function to extract and print results
def extract_all(text, pattern_dict):
    print("\n--- Extracted Data ---")
    for label, pattern in pattern_dict.items():
        matches = re.findall(pattern, text)
        print(f"\n{label} ({len(matches)} found):")
        for match in matches:
            print(f"  - {match}")

# Run extraction
if __name__ == '__main__':
    extract_all(sample_data, patterns)
