# UI Automation Testing Project for [qa-practice.com](https://qa-practice.com/)

## About Me
My name is **Artem**, I am studying **Applied Informatics** at Belarusian State University and actively developing as a **QA Automation Engineer**.

## Project Goal
This project was developed as a **portfolio project** to demonstrate my skills as a **QA Automation Engineer**.  
It covers **UI automated testing** of the educational website [qa-practice.com](https://qa-practice.com/), using **Python + Pytest + Selenium**.  

The project showcases:
- **Page Object Model (POM)** design pattern  
- **Custom Pytest CLI parameters** for flexible test execution  
- **Parallel test execution** with pytest-xdist  
- **Logging system** with multiple log levels  
- **Artifacts capturing** on test failures (screenshots, HTML dumps, browser logs)  

---

## Tech Stack
- **Python 3.12**
- **Pytest 8.4.1** — test frameword 
- **Selenium 4.35.0** — UI automation  
- **Pytest-xdist 3.8.0** — parallel execution  
- **WebDriver Manager (custom commit)** — driver management  
- **Logging & Reporting** — detailed execution logs, artifacts on failures  

---

``` yaml
.
├── src/                  # Framework core (POM classes, helpers, utils)
├── pages/                # Page Classes (Page Objects)
├── tests/                # Automated test cases
├── artifacts/            # Failure artifacts
│   └── test_name[browser]_2025-12-31_23-59-59
├── conftest.py           # Pytest configuration & CLI options
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## Custom Test Parameters
Implemented CLI parameters for flexible test execution:

```python
--use-manager   # download drivers via webdriver-manager
--browser       # choose browser: chrome (default), firefox, edge, all
--parallel      # run tests in parallel with pytest-xdist
--headless      # headless execution mode
--debug_logs    # enable debug-level logging
```

---

## Example Runs
``` bash
# Run in Chrome
pytest tests/

# Run in Firefox
pytest tests/ --browser=firefox

# Run all browsers
pytest tests/ --browser=all

# Parallel run in 3 threads
pytest -n 3 --parallel

# Run in headless mode
pytest --headless
```

---

## Logging & Artifacts
On test failure, the following artifacts are automatically saved in artifacts/:
- Screenshot of the page at failure moment
- HTML dump of the DOM
- Browser logs (if available)
  
This ensures fast debugging and transparent root cause analysis.

---

## Future Improvements
- Integration with CI/CD (GitHub Actions)
- Allure Report for visual reporting
- Cross-browser cloud testing (BrowserStack, Selenoid)
- Dockerization for environment consistency

  ---

This project demonstrates my readiness to work with modern QA automation frameworks and integrate them into real engineering workflows.
