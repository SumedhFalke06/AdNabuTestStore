#!/bin/bash
# Test Runner Script for Search and Add to Cart Automation

echo "=========================================="
echo "Running Search and Add to Cart Test Suite"
echo "=========================================="

# Create reports directory if it doesn't exist
mkdir -p reports

# Run the test with HTML reporting
python -m pytest tests/test_search_add_to_cart.py \
    --html=reports/test_report.html \
    --self-contained-html \
    -v \
    --tb=short

echo ""
echo "=========================================="
echo "Test execution completed!"
echo "=========================================="
echo "HTML Report generated at: reports/test_report.html"
echo "=========================================="
