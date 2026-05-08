# Shopify Store Automation Tests

This project contains automated tests for a Shopify store using Python and Selenium WebDriver. The tests automate the scenario of searching for a product and adding it to the cart.

##  Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)


##  Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.10+** - The project uses Python 3.13
- **Google Chrome Browser** - Latest stable version
- **ChromeDriver** - Automatically managed by selenium-manager
- **Git** - For cloning the repository (if applicable)

### System Requirements

- **Operating System**: macOS, Windows, or Linux
- **RAM**: Minimum 4GB
- **Disk Space**: 500MB free space

##  Project Structure

```
PythonProject/
├── page/                          # Page Object Model classes
│   ├── __init__.py
│   └── store_page.py             # StorePage class with all page methods
├── tests/                        # Test files and configuration
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures and hooks
│   └── test_search_add_to_cart.py # Main test case
├── reports/                      # Generated test reports
├── screenshots/                  # Screenshots captured on failures
├── .venv/                        # Python virtual environment
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
├── run_tests.sh                  # Test runner script
└── README.md                     # This documentation
```

##  Setup Instructions

### Step 1: Clone or Download the Project

If using Git:
```bash
git clone <repository-url>
cd PythonProject
```

### Step 2: Create Virtual Environment

```bash
1. Create virtual environment
python -m venv .venv

2. Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

**Key Dependencies:**
- `selenium` - Web automation framework
- `pytest` - Testing framework
- `pytest-html` - HTML report generation
- `webdriver-manager` - Automatic driver management


##  Running Tests

### Using Pytest Directly

```bash
# Run specific test with HTML report
python -m pytest tests/test_search_add_to_cart.py --html=reports/test_report.html --self-contained-html -v

# Run all tests in verbose mode
python -m pytest tests/ -v

# Run tests with different browsers (if configured)
python -m pytest tests/ --browser firefox
```

