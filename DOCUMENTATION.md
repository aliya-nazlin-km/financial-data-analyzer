# Project Documentation — Financial Data Analyzer

---

## Table of Contents

* [Project Overview](#project-overview)
* [System Architecture](#system-architecture)
* [Application Flowchart](#application-flowchart)
* [Component Breakdown](#component-breakdown)
* [Execution Flow](#execution-flow)
* [Internal Logic Explanation](#internal-logic-explanation)
* [File Handling and Validation](#file-handling-and-validation)
* [Design Decisions](#design-decisions)
* [Design Principles Used](#design-principles-used)
* [SOLID Principles Applied](#solid-principles-applied)
* [Future Enhancements](#future-enhancements)

---

## Project Overview

The Financial Data Analyzer is a Python-based application designed to process and analyze financial instruction data from CSV files.

The application supports both:

* Command-Line Interface (CLI)
* Graphical User Interface (GUI)

It enables users to perform structured data analysis such as searching, grouping, aggregation, and transaction insights.

---

## System Architecture

```text
User Input (CLI / GUI)
        ↓
   main.py (Launcher)
        ↓
   analyzer.py (Core Logic)
        ↓
   Pandas Data Processing
        ↓
   CSV File (Input Data)
```

---

## Application Flowchart

```text
Start
  ↓
User selects mode (CLI / GUI)
  ↓
Load CSV file
  ↓
Validate CSV structure
  ↓
User selects operation
  ↓
Process data using analyzer.py
  ↓
Display results
  ↓
End
```

---

## Component Breakdown

### analyzer.py

* Core backend logic of the application
* Handles data loading, cleaning, aggregation, and searching

### cli.py

* Command-line interface
* Provides menu-driven interaction

### gui.py

* Tkinter-based graphical interface
* Includes dropdown actions and dynamic input fields

### main.py

* Entry point of application
* Allows user to choose CLI or GUI mode

### data.csv

* Sample dataset for testing

---

## Execution Flow

1. User runs `main.py`
2. Selects CLI or GUI mode
3. CSV file is loaded
4. Data is validated
5. User selects operation
6. analyzer.py processes data
7. Results are displayed

---

## Internal Logic Explanation

### Data Handling

* Uses Pandas to load CSV data
* Converts date column using `pd.to_datetime()`
* Handles missing values using `fillna()`

---

### Core Functions

* `count_by_type()` → counts instruction types
* `group_by_type()` → aggregates count, sum, mean
* `filter_by_status()` → filters by status
* `search_by_reference()` → filters by reference
* `highest_transaction()` → finds maximum value
* `lowest_transaction()` → finds minimum value

---

### UI Logic

* Dropdown selects operation
* Dictionary mapping replaces if-else conditions
* Entry field shown only for search
* Output displayed in text widget

---

## File Handling and Validation

* Ensures uploaded file is CSV

* Validates required columns:

  * instruction_ref
  * instruction_type
  * amount
  * status
  * date

* Displays error messages for invalid inputs

---

## Design Decisions

* Used Pandas for efficient data processing
* Used Tkinter for lightweight GUI
* Separated backend logic from UI
* Used dictionary mapping for scalability
* Added validation for real-world reliability

---

## Design Principles Used

* Separation of Concerns
* Modular Architecture
* Reusability
* Input Validation
* Error Handling

---

## SOLID Principles Applied

### 1. Single Responsibility Principle (SRP)

Each module has a single responsibility:

* `analyzer.py` → data processing
* `cli.py` → CLI interaction
* `gui.py` → GUI interaction
* `main.py` → application entry point

---

### 2. Open/Closed Principle (OCP)

* System allows adding new features without modifying existing code
* New operations can be added via function mapping

---

### 3. Liskov Substitution Principle (LSP)

* Functions can be extended or replaced without affecting overall system behavior
* Consistent output format maintained

---

### 4. Interface Segregation Principle (ISP)

* CLI and GUI interact independently with analyzer
* No unnecessary dependencies

---

### 5. Dependency Inversion Principle (DIP)

* UI layers depend on analyzer abstraction
* Business logic is centralized and reusable

---

## Future Enhancements

* Add unit testing
* Add data visualization
* Export results to CSV/Excel
* Convert to web-based application

---
