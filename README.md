# TravelBuddy Automation Testing

## Overview

This repository contains an advanced automation testing framework for the TravelBuddy website (Goibibo clone). It's designed to showcase end-to-end testing capabilities using Selenium, Pytest, and GitHub Actions.

## Features
- **End-to-End Testing**: Covers login, search, booking, and payment workflows.
- **Page Object Model (POM)**: Modular and reusable design for UI interactions.
- **CI/CD Integration**: GitHub Actions for automated test execution.
- **Allure Reports**: For detailed test reporting and analysis.

## Tools & Technologies
- **Programming Language**: Python 3.10+
- **Testing Framework**: Pytest
- **Automation Tool**: Selenium WebDriver
- **Reports**: Allure Reports
- **CI/CD**: GitHub Actions

## Folder Structure

```
travelbuddy-automation/
│
├── tests/                      # Pytest test cases
├── pages/                      # Page Object Models
├── utils/                      # Helper functions/configs
├── conftest.py                 # Pytest fixtures
├── requirements.txt            # Python dependencies
├── .gitignore
├── README.md
├── pytest.ini                  # Pytest config
├── .github/
│   └── workflows/
│       └── pytest.yml          # GitHub Actions CI workflow
```

## Getting Started

### Prerequisites
- Python 3.10 or above
- ChromeDriver (Ensure compatibility with your Chrome browser version)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/altaf1346/travelbuddy-automation.git
   cd travelbuddy-automation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest --alluredir=allure-results
   ```

4. Generate Allure report:
   ```bash
   allure serve allure-results
   ```

## Contributing

Feel free to create a pull request or open an issue to enhance the project. Contributions are welcome!
