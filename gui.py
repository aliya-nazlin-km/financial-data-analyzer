import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os
from analyzer import FinancialAnalyzer

# ==============================
# REQUIRED CSV STRUCTURE
# ==============================

REQUIRED_COLUMNS = [
    "instruction_ref",
    "instruction_type",
    "amount",
    "status",
    "date"
]

# Default analyzer (initial file)
analyzer = FinancialAnalyzer("data.csv")


# ==============================
# FUNCTION: LOAD CSV FILE
# ==============================

def load_csv():
    global analyzer

    # Open file dialog
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    # Validate extension
    if not file_path.endswith(".csv"):
        messagebox.showerror("Error", "Please select a CSV file")
        return

    try:
        df = pd.read_csv(file_path)

        # Validate required columns
        if not all(col in df.columns for col in REQUIRED_COLUMNS):
            messagebox.showerror(
                "Error",
                "CSV must contain columns:\n" + ", ".join(REQUIRED_COLUMNS)
            )
            return

        # Reload analyzer with new file
        analyzer = FinancialAnalyzer(file_path)

        # Show filename
        file_label.config(text=f"Loaded: {os.path.basename(file_path)}")

        messagebox.showinfo("Success", "CSV loaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ==============================
# FUNCTION: SEARCH
# ==============================

def handle_search():
    ref = entry.get().strip()
    result = analyzer.search_by_reference(ref)

    if isinstance(result, str):
        return result

    return result.to_string()


# ==============================
# FUNCTION: EXECUTE ACTION
# ==============================

def execute_action():
    action = dropdown.get()
    output.delete("1.0", tk.END)

    actions = {
        "Preview Data": lambda: analyzer.preview_data().to_string(),
        "Count by Type": lambda: analyzer.count_by_type().to_string(),
        "Group Analysis": lambda: analyzer.group_by_type().to_string(),
        "Search by Reference": handle_search,
        "Highest Transaction": lambda: analyzer.highest_transaction().to_string(),
        "Lowest Transaction": lambda: analyzer.lowest_transaction().to_string(),
    }

    func = actions.get(action)

    if func:
        result = func()
        if result:
            output.insert(tk.END, result)
    else:
        output.insert(tk.END, "Please select a valid option")


# ==============================
# FUNCTION: SHOW/HIDE ENTRY
# ==============================

def toggle_entry(event):
    selected = dropdown.get()

    if selected == "Search by Reference":
        entry_frame.pack(pady=5)
    else:
        entry_frame.pack_forget()
        entry.delete(0, tk.END)


# ==============================
# UI SETUP
# ==============================

root = tk.Tk()
root.title("Financial Instruction Analyzer")
root.geometry("800x600")
root.configure(bg="#1e1e2f")

# ==============================
# HEADER
# ==============================

header = tk.Frame(root, bg="#1e1e2f")
header.pack(pady=15)

title = tk.Label(
    header,
    text="Financial Instruction Analyzer",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack()

subtitle = tk.Label(
    header,
    text="Upload and analyze financial instruction data",
    font=("Segoe UI", 10),
    fg="#aaaaaa",
    bg="#1e1e2f"
)
subtitle.pack()

# ==============================
# CONTROL PANEL
# ==============================

control_frame = tk.Frame(root, bg="#2b2b3c", padx=20, pady=20)
control_frame.pack(pady=10, fill="x", padx=20)

# Upload button
upload_btn = tk.Button(
    control_frame,
    text="Upload CSV",
    command=load_csv,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
)
upload_btn.pack(pady=5)

# Show selected file
file_label = tk.Label(
    control_frame,
    text="Loaded: data.csv",
    fg="white",
    bg="#2b2b3c"
)
file_label.pack()

# Dropdown label
label = tk.Label(
    control_frame,
    text="Select Action:",
    fg="white",
    bg="#2b2b3c"
)
label.pack(anchor="w")

# Dropdown
options = [
    "Preview Data",
    "Count by Type",
    "Group Analysis",
    "Search by Reference",
    "Highest Transaction",
    "Lowest Transaction"
]

dropdown = ttk.Combobox(control_frame, values=options, width=40)
dropdown.set("Select an action")
dropdown.pack(pady=8)

dropdown.bind("<<ComboboxSelected>>", toggle_entry)

# ==============================
# SEARCH INPUT (HIDDEN INITIALLY)
# ==============================

entry_frame = tk.Frame(control_frame, bg="#2b2b3c")

entry_label = tk.Label(
    entry_frame,
    text="Enter Reference ID:",
    fg="white",
    bg="#2b2b3c"
)
entry_label.pack(anchor="w")

entry = tk.Entry(entry_frame, width=30)
entry.pack(pady=5)

entry_frame.pack_forget()

# ==============================
# EXECUTE BUTTON
# ==============================

execute_btn = tk.Button(
    control_frame,
    text="Execute",
    command=execute_action,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15
)
execute_btn.pack(pady=10)

# ==============================
# OUTPUT
# ==============================

output_frame = tk.Frame(root, bg="#1e1e2f")
output_frame.pack(pady=10, padx=20)

output_label = tk.Label(
    output_frame,
    text="Output:",
    fg="white",
    bg="#1e1e2f"
)
output_label.pack(anchor="w")

output = tk.Text(
    output_frame,
    height=18,
    width=95,
    bg="#2b2b3c",
    fg="white",
    insertbackground="white",
    font=("Consolas", 10),
    padx=10,
    pady=10
)
output.pack()

# ==============================
# RUN APP
# ==============================

def main():
    root.mainloop()