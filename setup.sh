#!/bin/bash
# Setup script for Shopify Store Automation Tests

echo "=========================================="
echo "Shopify Store Automation Tests - Setup"
echo "=========================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo " Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo " Python found: $(python --version)"

# Check if Chrome is installed
if ! command -v google-chrome &> /dev/null; then
    echo "  Google Chrome not found. Please install Chrome browser."
    echo "   Download from: https://www.google.com/chrome/"
fi

echo " Chrome found: $(google-chrome --version 2>/dev/null || echo 'Version check failed')"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo " Creating virtual environment..."
    python -m venv .venv
    echo " Virtual environment created"
else
    echo " Virtual environment already exists"
fi

# Activate virtual environment
echo " Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo " Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo " Creating directories..."
mkdir -p reports
mkdir -p screenshots

# Verify installation
echo " Verifying installation..."
python -c "
try:
    import selenium
    from selenium import webdriver
    print(' Selenium installed successfully')
except ImportError as e:
    print(' Selenium import failed:', e)
    exit(1)

try:
    import pytest
    print(' Pytest installed successfully')
except ImportError as e:
    print(' Pytest import failed:', e)
    exit(1)
"

echo ""
echo "=========================================="
echo "Setup completed successfully! "
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Run tests: ./run_tests.sh"
echo "2. View reports: open reports/test_report.html"
echo ""
echo "Happy testing! "
echo "=========================================="
