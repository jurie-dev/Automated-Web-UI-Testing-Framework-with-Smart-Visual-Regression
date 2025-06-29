# 🧪 Automated Web UI Testing Framework with Smart Visual Regression

This project performs automated UI testing with visual regression for [SauceDemo](https://www.saucedemo.com). It uses:
- **Selenium** for browser automation
- **Pytest** for testing structure
- **Pillow** for image comparison
- **pytest-html** for HTML reporting

## 📸 Features
- Tests login and cart functionality.
- Takes screenshots and compares them with baseline images.
- Highlights any visual changes via image diffs.
- Runs on Chrome and Firefox via GitHub Actions.

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/visual-regression-test.git
   cd visual-regression-test

2. Create Virtual Environment
  python -m venv venv
  source venv/bin/activate  # For Linux/macOS
  venv\Scripts\activate     # For Windows

3. Install Dependencies
    pip install -r requirements.txt

4. Directory Structure

├── pages/
├── screenshots/
│   ├── baseline/
│   ├── current/
├── tests/
│   ├── test_login.py
│   ├── test_cart_visual.py
├── utils/
│   ├── visual_compare.py
├── conftest.py
├── requirements.txt
├── .github/workflows/test.yml
└── README.md

▶️ Run Tests Locally

  pytest --html=report.html


🔁 GitHub Actions
This project includes a CI pipeline using GitHub Actions.
📂 .github/workflows/test.yml

name: Run UI Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    strategy:
      matrix:
        browser: [chrome, firefox]

    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Tests
        env:
          BROWSER: ${{ matrix.browser }}
        run: pytest --html=report-${{ matrix.browser }}.html


🌐 Browser Matrix
Test Case	Chrome	Firefox
test_login_ui	✅	✅
test_cart_visual	✅	✅

✅ = Supported in GitHub Actions workflow

📬 Contributions
Feel free to open issues or submit PRs to enhance cross-browser testing, visual diffing, or reporting!

📝 License
MIT License

Let me know if you want the `.github/workflows/test.yml` file generated separately or changes in the `requirements.txt`.





