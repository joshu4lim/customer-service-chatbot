# Simple mock data for tracking numbers and statuses
# Each tracking number contains a list of: status and eta
# Statuses are: in_transit, delivered, delayed, missing
MOCK_SHIPMENTS = {
    "ABC123": ["in_transit", "1 day"],
    "DEF456": ["delivered", None],
    "GHI789": ["delayed", "1 week"],
    "JKL000": ["missing", None],
}

# Helper functions
def is_valid_tracking_number(tracking):
    """
    Function to check if the tracking number is in the MOCK_SHIPMENTS database.
    """
    return tracking in MOCK_SHIPMENTS

def lookup_status(tracking):
    """
    Look up a tracking number in our mock database and returns the package's status.
    """
    return MOCK_SHIPMENTS.get(tracking)[0]

def lookup_eta(tracking):
    """
    Look up a tracking number in our mock database and returns the package's eta.
    """
    return MOCK_SHIPMENTS.get(tracking)[1]


def track_package():
    """
    Function to handle package status based on tracking number.
    """
    print("\nBot: Please provide a valid tracking number.")

    while True:
        tracking = input("Please enter a tracking number: ").strip()

        # Error handling for valid tracking number.
        if not is_valid_tracking_number(tracking):
            print("\nBot: That doesn't seem to be a valid tracking number.")
            continue

        # Validated tracking number, check status of package.
        status = lookup_status(tracking)
        eta = lookup_eta(tracking)

        handle_status(status, eta)

        # Return back to the beginning after checking status.
        print("\nBot: Returning to the beginning.\n")
        print("Bot: Hi, how may I help you?")
        return


def handle_status(status, eta):
    """
    Handles the different possible package statuses.
    """

    if status == "in_transit":
        print(f"\nBot: The package is in transit.")
        print(f"Bot: The package will arrive {eta}.")
        return
    elif status == "delivered":
        print("\nBot: The package was delivered.")

        # Check if package is delivered but missing.
        missing = ask_yes_no("Bot: Are you still unable to find the package? (yes/no): ")
        if missing:
            print("Bot: I'm sorry you can't find your package.")
            handle_refund()
        else:
            print("Bot: Glad to hear you found it!")
        return
    elif status == "delayed":
        print("\nBot: The package is delayed.")
        print(f"Bot: It will arrive {eta}.")
        handle_refund()
        return
    elif status == "missing":
        print("\nBot: The package is lost.")
        handle_refund()
        return
    else:
        # Error handling for unexpected status.
        print("\nBot: I'm seeing an unknown status for this package.")
        print("Bot: Let me connect you with a human agent to look into this.")
        return


def ask_yes_no(prompt):
    """
    Ask a yes/no question and return True for yes, False for no.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        # Error handling for unexpected input.
        print("Bot: Please answer 'yes' or 'no'.")


def handle_refund():
    """
    Function that handles the refund process.
    Yes -> Refund processed.
    No  -> Return to beginning.
    """
    wants_refund = ask_yes_no("\nBot: Would you like a refund? (yes/no): ")

    if wants_refund:
        print("\nBot: Refund processed.")
    else:
        print("\nBot: Okay, no refund will be issued at this time.")


# Customer service chatbot main loop
def main():
    """
    Main loop: keeps running until user chooses to end.
    """
    print("Bot: Hi, how may I help you?")
    while True:
        print("\nOptions:")
        print("\t1) I'm want to check my package status.")
        print("\t2) I'm good.")
        choice = input("Please choose an option (1 or 2): ")

        # Option 1: handles tracking package
        # Option 2: exits
        # Error handling for any other invalid inputs
        if choice == '1':
            track_package()
        elif choice == '2': 
            print("Bot: Thank you for using our service, please let us know if you need any further help.")
            break
        else:
            print("Bot: I'm sorry, I didn't quite get that.")
            print("Bot: Please choose '1' if you're missing a package, or '2' if you're good.")


if __name__ == "__main__":
    main()
