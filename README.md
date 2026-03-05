# 0487_Entorns
# Shop Management Project: Refactoring & Quality

## 📝 Description
This project is a Python-based utility designed to calculate final retail prices for a shop. It automatically applies category-specific discounts (such as for clothing) or surcharges (for electronics) and handles promotional vouchers for youth customers (under 18).

Originally starting as "dirty code," this project has been professionally refactored to demonstrate clean code principles, proper documentation, and version control management.

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone this repository:
   ```bash
   git clone <https://github.com/jkarrad/0487_Entorns/>
3. Navigate to the directory and run the script:
   ```bash
   python botiga.py

##🛠️ Refactoring Improvements Applied
Following the Session 1 requirements, the following "code smells" were fixed:

    Meaningful Naming: Renamed generic variables (p, t, e, res) and the main function (calcular) to descriptive names that reveal intent.
    Constant Extraction: Removed "Magic Numbers" (0.9, 1.15, 5) and replaced them with named constants at the top of the file for easier maintenance.
    Method Extraction: Isolated the category-based price logic into a dedicated function (apply_discounts_and_surcharges) to improve readability and testability.
    Simplified Logic: Streamlined the conditional flow to ensure the code is easy to follow and less prone to errors.

📚 Documentation & Quality

    Docstrings: All functions include standard Python Docstrings explaining their purpose and parameters.
    "Why" Comments: Included comments explaining business decisions, such as the reasoning behind electronics surcharges.
    Tooling: Developed using the SonarLint extension in VS Code to ensure adherence to best practices.

🎓 Course Context

    Course: CFGS Multi-platform Application Development
    Module: 0487 - Development Environments (Entorns de Desenvolupament)
    Date: 2025/2026 Academic Year

