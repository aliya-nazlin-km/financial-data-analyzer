def run():
    """
    Entry point to choose between CLI and GUI modes
    """
    choice = input("Run mode (cli/gui): ").strip().lower()

    if choice == "cli":
        import cli
        cli.main()

    elif choice == "gui":
        import gui
        gui.main()

    else:
        print("Invalid choice. Please enter 'cli' or 'gui'.")


# Standard Python entry point
if __name__ == "__main__":
    run()