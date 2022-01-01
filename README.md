# Mod2_Challenge (Loan Qualifier Application)

This is a python project that builds on previous work done in loan_qualifier_application.py that writes qualifying loans (based on criteria pulled from an external csv file) into a new csv file and asks users if they want to save the csv file. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, returning to them the number of qualifying loans, printing the names and details of the qualifying loans to a new csv file and asking users if they want the output csv file.

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [csv] - import csv to allow for proper reading and writing to csv files

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install csv
```

---

## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

The file path to the rate-sheet (prompt #1) is:
```
./data/daily_rate_sheet.csv
```

The program saves a csv file containing qualifying loans at:
```
./data/qualifying_loans.csv
```

The app.py program relies on other files:
```
./data/daiy_rate_sheet.csv

./qualifier/filters/credit_score
./qualifier/filters/debt_to_income
./qualifier/filters/loan_to_value
./qualifier/filters/max_loan_size

./qualifier/utils/calulators
.qualifier/utils/fileio
```

## User input
Upon launching the loan qualifier application the user will be asked:
---
Enter a file path to a rate sheet (.csv)
What's your credit score?
What's your current amount of monthly debt?
What's your total monthly income?
What's your desired lona mount?
What's your home value?

---

After determining if at least one loan is available, the user will be asked:
Do you want to save a csv file of qualifyng loans?

---

If the user wants to save a file, they will be prompted:
Enter a file path where you want to save your csv file of qualifying loans:


---

## Contributors

Brought to you by Ann Howell with support from Rice FinTech Bootcamp.

---

## License

MIT

