# 🛒 E-commerce Cart QA Automation Project

**Manual Testing • UI Automation (Playwright) • API Testing**

This project demonstrates a complete QA workflow for validating an e-commerce shopping cart system.
It includes **manual test design**, **UI automation using Playwright**, **API testing**, and **XML reporting**, organized in a clean and scalable structure.

---

## ⭐ Project Overview

This project focuses on testing the core functionality of an e-commerce cart, using both manual and automated techniques.

Key components include:

* **Manual test cases** (functional, regression, negative)
* **UI automation with Playwright + Python**
* **API validation using the Requests library**
* **JUnit XML test reporting via Pytest**
* **Custom Playwright fixture** (no dependency on pytest-playwright)

### Main features tested:

* Adding items to the cart
* Removing items
* Checking cart item quantities
* Validating checkout flow
* API test for user creation

---

## 🧪 Tech Stack

### **Tools & Technologies**

* **Python 3.12**
* **Playwright** (browser automation)
* **Pytest** (test framework)
* **Requests** (API testing)
* **JUnit-style XML reports**

---

## 📁 Folder Structure

```
ecommerce-cart-qa-project/
│
├── automation/
│   ├── api/
│   │   └── test_cart_api.py
│   └── ui/
│       ├── test_add_to_cart.py
│       ├── test_checkout_flow.py
│       └── test_remove_item.py
│
├── bug-reports/
│   └── bug-report.xlsx
│
├── manual-tests/
│   └── test-cases-cart.xlsx
│
├── reports/
│   └── ui-report.xml
│
├── conftest.py
├── README.md
└── venv/
```

---

## 🎯 Test Coverage

### **UI Test Scenarios**

✔ Successful login
✔ Add product to cart
✔ Remove product from cart
✔ Validate checkout flow
✔ Verify item count in cart

### **API Test Scenarios**

✔ Create a new user (POST)
✔ Validate status code
✔ Validate response body

---

## 🖥 Running the Tests

### **1️⃣ Set up virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **2️⃣ Install dependencies**

```bash
pip install pytest requests playwright
playwright install
```

---

### **3️⃣ Run full test suite**

```bash
pytest --junitxml=reports/ui-report.xml
```

---

### **4️⃣ Run UI-only tests**

```bash
pytest automation/ui/
```

---

### **5️⃣ Run API-only tests**

```bash
pytest automation/api/
```

---

## 📄 Test Reporting

Pytest generates **JUnit XML reports** at:

```
reports/ui-report.xml
```

These reports can be used in CI/CD systems such as GitHub Actions, Jenkins, GitLab CI, and Azure DevOps.

You can also view the generated HTML version:

👉 **[Download HTML Report](sandbox:/mnt/data/ui-report.html)**

---

## 🔧 Custom Playwright Fixture

This project uses a custom Playwright fixture defined in `conftest.py`:

```python
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()
```

This ensures stable browser sessions without requiring external pytest plugins.

---

## 🚀 Future Enhancements

* Implement Page Object Model (POM)
* Capture screenshots on test failure
* Integrate Allure or pytest-html for advanced reports
* Add GitHub Actions CI workflow
* Add performance/load testing (e.g., with Locust)

---

## 👤 Author

**Md Hasanul Kabir**
QA Engineer • Automation • Python • Playwright
