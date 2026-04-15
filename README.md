# 💰 Financial Data Analyzer

A Python-based application for analyzing financial instruction data using Pandas and Tkinter.
Supports both Command-Line Interface (CLI) and Graphical User Interface (GUI).

---

## 🚀 Features

* 📂 Upload and validate CSV files
* 🔍 Search by instruction reference
* 📊 Group and analyze transaction data
* 📈 Count and summarize instruction types
* 🖥️ Dual interface:

  * CLI (Command Line Interface)
  * GUI (Tkinter-based desktop application)
* 🧠 Clean architecture with separation of backend logic and UI

---

## 🛠️ Tech Stack

* Python
* Pandas
* Tkinter

---

## 📂 Project Structure

```
financial-data-analyzer/
│
├── analyzer.py   # Core data processing logic
├── cli.py        # CLI interface
├── gui.py        # GUI interface
├── main.py       # Launcher (choose CLI or GUI)
├── data.csv      # Sample dataset
```

---

## ▶️ How to Run

### Option 1: Using Launcher (Recommended)

```
python main.py
```

Then choose:

```
cli  → Command-line interface  
gui  → Graphical interface  
```

---

### Option 2: Run Directly

```
python cli.py
python gui.py
```

---

## 📊 Supported Operations

* Count instructions by type
* Group transactions by category (count, sum, average)
* Search by instruction reference
* Identify highest and lowest transactions
* Preview dataset

---

## 📁 CSV Format Requirements

The uploaded CSV file must contain the following columns:

```
instruction_ref
instruction_type
amount
status
date
```

Example:

```
INS001,Loan,50000,Completed,14-04-2026
```

---

## ⚙️ Key Concepts Implemented

* Object-Oriented Programming (OOP)
* Data processing using Pandas
* Event-driven UI (Tkinter)
* File validation and error handling
* Modular architecture (separation of concerns)

---

## 🧪 Testing

Unit tests are implemented using Python’s built-in `unittest` framework to ensure correctness and reliability of core functionalities.

### Run Tests

```bash
python test_analyzer.py
```

### Test Coverage Includes:

* Data aggregation functions
* Search functionality (valid & invalid cases)
* Data integrity checks for Pandas DataFrames

---

## 👩‍💻 Author

**Aliya Nazlin K M**
Software Engineer | Backend Developer transitioning to Python

---

## 🌟 Future Improvements

* Export results to CSV/Excel
* Add data visualizations (charts)
* Convert to web application (Flask/Django)

---
