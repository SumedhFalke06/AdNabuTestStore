# Shopify Store Automation Tests

This project contains automated tests for a Shopify store using Python and Selenium WebDriver. The tests automate the scenario of searching for a product and adding it to the cart.

##  Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [Viewing Reports](#viewing-reports)
- [Test Configuration](#test-configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

##  Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.8+** - The project uses Python 3.13
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
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
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

### Step 4: Verify Chrome Installation

Ensure Google Chrome is installed and up to date:

```bash
# Check Chrome version
google-chrome --version
```

##  Running Tests

### Method 1: Using the Test Runner Script (Recommended)

```bash
# Make script executable (first time only)
chmod +x run_tests.sh

# Run all tests with reporting
./run_tests.sh
```

### Method 2: Using Pytest Directly

```bash
# Run specific test with HTML report
python -m pytest tests/test_search_add_to_cart.py --html=reports/test_report.html --self-contained-html -v

# Run all tests in verbose mode
python -m pytest tests/ -v

# Run tests with different browsers (if configured)
python -m pytest tests/ --browser firefox
```

### Method 3: Using Python Module

```bash
# Run tests as Python module
python -m pytest tests/test_search_add_to_cart.py
```

##  Viewing Reports

### HTML Test Reports

After test execution, HTML reports are generated in the `reports/` directory:

1. **Open the report** in your browser:
   ```bash
   open reports/test_report.html
   ```

2. **Report Contents Include:**
   - Test execution summary
   - Pass/fail status for each test
   - Execution time and duration
   - Detailed logs and error messages
   - Screenshots (captured on failures)

### Console Output

Test results are also displayed in the terminal with:
- Real-time execution status
- Test names and outcomes
- Execution time
- Error details (if any)

## ️ Test Configuration

### Pytest Configuration (`pytest.ini`)

```ini
[tool:pytest]
addopts =
    --html=reports/test_report.html
    --self-contained-html
    --capture=no
    --tb=short
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### Test Fixtures (`tests/conftest.py`)

- **driver**: Provides WebDriver instance with Chrome options
- **Screenshot capture**: Automatically captures screenshots on test failures
- **Browser configuration**: Maximized window, stable options

### Test Data

- **Store URL**: `https://adnabu-store-assignment1.myshopify.com`
- **Password**: `AdNabuQA`
- **Test Product**: `snowboard`

##  Test Scenario Details

The automation covers the following user journey:

1. **Open Store** - Navigate to the Shopify store URL
2. **Unlock Store** - Enter password to access password-protected store
3. **Search Product** - Search for "snowboard" and navigate to product page
4. **Add to Cart** - Click "Add to Cart" button
5. **Verify Addition** - Confirm product was successfully added

### Test Assertions

- Product search completes successfully
- Product page loads correctly
- Add to Cart button is clickable
- Cart confirmation appears after adding product

##  Troubleshooting

### Common Issues and Solutions

#### 1. ChromeDriver Issues
```
Error: Message: 'chromedriver' executable needs to be in PATH
```
**Solution**: Selenium Manager handles this automatically. Ensure Chrome is installed.

#### 2. Import Errors
```
ModuleNotFoundError: No module named 'selenium'
```
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Virtual Environment Issues
```
Error: Python executable not found
```
**Solution**: Activate virtual environment
```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

#### 4. Test Timeouts
```
TimeoutException: Message: timeout
```
**Solution**: Check internet connection and store availability. The tests use 20-second timeouts.

#### 5. Report Not Generated
```
No HTML report found
```
**Solution**: Run tests with HTML flag
```bash
python -m pytest tests/ --html=reports/test_report.html --self-contained-html
```

### Debug Mode

Run tests in debug mode for detailed output:

```bash
# Enable debug logging
python -m pytest tests/ -v -s --tb=long
```

### Checking Test Environment

Verify your setup:

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Check Chrome version
google-chrome --version

# Test WebDriver
python -c "from selenium import webdriver; driver = webdriver.Chrome(); driver.quit(); print('WebDriver OK')"
```

##  Contributing

### Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable and method names
- Add docstrings to classes and methods
- Keep methods focused on single responsibilities

### Adding New Tests

1. Create new test file in `tests/` directory
2. Follow naming convention: `test_*.py`
3. Use Page Object Model pattern
4. Add appropriate assertions
5. Update documentation

### Reporting Issues

When reporting bugs or issues:

1. Include full error message and traceback
2. Specify your environment (OS, Python version, Chrome version)
3. Include steps to reproduce
4. Attach relevant screenshots or logs

##  Performance Notes

- **Average Test Duration**: ~25-30 seconds
- **Browser**: Chrome (headless option available)
- **Parallel Execution**: Not configured (single-threaded)
- **Retry Logic**: Not implemented (tests run once)

##  Security Notes

- Store password is hardcoded for demo purposes
- In production, use environment variables or secure credential management
- Test data is publicly accessible

##  Support

For questions or issues:

1. Check this README first
2. Review troubleshooting section
3. Check existing issues (if applicable)
4. Create detailed bug report with logs

---

**Test Framework**: pytest + Selenium WebDriver
**Language**: Python 3.13
**Browser**: Google Chrome
**Reporting**: HTML Reports with Screenshots
**CI/CD Ready**: Configurable for automated pipelines
