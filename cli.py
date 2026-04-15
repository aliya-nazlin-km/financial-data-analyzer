from analyzer import FinancialAnalyzer

def main():
    analyzer = FinancialAnalyzer("data.csv")

    # Mapping choices to functions
    actions = {
        "1": lambda: print("\n=== DATA PREVIEW ===\n", analyzer.preview_data()),
        "2": lambda: print("\nTotal Instructions:", analyzer.total_instructions()),
        "3": lambda: print("\n=== COUNT BY TYPE ===\n", analyzer.count_by_type().to_string()),
        "4": lambda: print("\n=== GROUPED ANALYSIS ===\n", analyzer.group_by_type()),
        "5": lambda: search(analyzer),
        "6": lambda: print("\n=== HIGHEST TRANSACTION ===\n", analyzer.highest_transaction().reset_index()),
        "7": lambda: print("\n=== LOWEST TRANSACTION ===\n", analyzer.lowest_transaction().reset_index()),
    }

    while True:
        print("\n===== Financial Instruction Analyzer =====")
        print("1. Preview Data")
        print("2. Total Instructions")
        print("3. Count by Type")
        print("4. Group Analysis")
        print("5. Search by Reference")
        print("6. Highest Transaction")
        print("7. Lowest Transaction")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "8":
            print("Exiting program...")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice! Please try again.")


def search(analyzer):
    ref = input("Enter Instruction Reference: ")
    print("\nSearch Result:")
    print(analyzer.search_by_reference(ref))


if __name__ == "__main__":
    main()
