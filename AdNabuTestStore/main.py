#!/usr/bin/env python
"""
Main entry point for AdNabu Test Store Automation

This script runs the test suite for the Shopify Store automation tests.
It uses pytest to execute all tests and generate HTML reports.
"""

import sys
import pytest
from pathlib import Path

def main():
    """Run the test suite with pytest"""

    # Get the project root directory
    project_root = Path(__file__).parent
    reports_dir = project_root / "reports"

    # Create reports directory if it doesn't exist
    reports_dir.mkdir(exist_ok=True)

    # Configure pytest arguments
    pytest_args = [
        str(project_root / "tests" / "test_search_add_to_cart.py"),
        f"--html={reports_dir / 'test_report.html'}",
        "--self-contained-html",
        "-v",
        "--tb=short"
    ]

    print("=" * 50)
    print("Running Search and Add to Cart Test Suite")
    print("=" * 50)
    print()

    # Run pytest
    exit_code = pytest.main(pytest_args)

    print()
    print("=" * 50)
    print("Test execution completed!")
    print("=" * 50)
    print(f"HTML Report generated at: {reports_dir / 'test_report.html'}")
    print("=" * 50)

    return exit_code

if __name__ == "__main__":
    sys.exit(main())

