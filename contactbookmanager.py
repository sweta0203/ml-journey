import csv
import json
import os

# Configuration
DATA_FILE = "contacts.json"


def load_contacts() -> dict:
    """Loads contacts from the JSON file.
    Creates an empty file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("[WARNING] Data file corrupted. Using empty contact book.")
        return {}


def save_contacts(contacts: dict) -> None:
    """Saves the current contacts dictionary safely back to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
    except IOError:
        print("[ERROR] Error saving changes to disk.")


def add_contact(contacts: dict) -> None:
    """Adds a completely new contact to the database."""
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()

    if not name:
        print("[ERROR] Name cannot be empty.")
        return

    if name in contacts:
        print("[ERROR] Contact '{name}' already exists. Use the Update option instead.")
        return

    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    city = input("Enter City: ").strip()

    # Dictionary-of-dictionaries structure
    contacts[name] = {
        "phone": phone if phone else "N/A",
        "email": email if email else "N/A",
        "city": city if city else "N/A",
    }
    save_contacts(contacts)
    print(f"[SUCCESS] Contact '{name}' added successfully!")


def view_all_contacts(contacts: dict) -> None:
    """Displays all stored contacts formatted cleanly."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("Your contact book is empty.")
        return

    for index, (name, details) in enumerate(contacts.items(), start=1):
        print(f"\n[{index}] Name: {name}")
        print(f"    Phone: {details['phone']}")
        print(f"    Email: {details['email']}")
        print(f"    City:  {details['city']}")


def search_contact(contacts: dict) -> None:
    """Searches for a contact using partial name matching.
    Case-insensitive."""
    print("\n--- Search Contacts ---")
    query = input("Enter search term (name): ").strip().lower()

    if not query:
        print("[ERROR] Search term cannot be empty.")
        return

    found = False
    for name, details in contacts.items():
        if query in name.lower():
            print(f"\nFound: {name}")
            print(f"    Phone: {details['phone']}")
            print(f"    Email: {details['email']}")
            print(f"    City:  {details['city']}")
            found = True

    if not found:
        print("[ERROR] No matching contacts found.")


def update_contact(contacts: dict) -> None:
    """Updates selected details of an existing contact."""
    print("\n--- Update Existing Contact ---")
    name = input("Enter the exact name to update: ").strip()

    if name not in contacts:
        print("[ERROR] Contact not found.")
        return

    print(f"Updating '{name}'. Leave blank and press Enter to keep current values.")

    current = contacts[name]

    new_phone = input(f"New Phone [{current['phone']}]: ").strip()
    new_email = input(f"New Email [{current['email']}]: ").strip()
    new_city = input(f"New City [{current['city']}]: ").strip()

    if new_phone:
        contacts[name]["phone"] = new_phone
    if new_email:
        contacts[name]["email"] = new_email
    if new_city:
        contacts[name]["city"] = new_city

    save_contacts(contacts)
    print(f"[SUCCESS] Contact '{name}' updated successfully!")


def delete_contact(contacts: dict) -> None:
    """Deletes a contact using pop()."""
    print("\n--- Delete Contact ---")
    name = input("Enter the exact name to delete: ").strip()

    if name in contacts:
        contacts.pop(name)
        save_contacts(contacts)
        print(f"[SUCCESS] Contact '{name}' deleted successfully.")
    else:
        print("[ERROR] Contact not found.")


def export_contacts_csv(contacts: dict) -> None:
    """Exports all contacts to a CSV file."""
    print("\n--- Export Contacts to CSV ---")

    if not contacts:
        print("[ERROR] No contacts available to export.")
        return

    try:
        with open("contacts.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # Header row
            writer.writerow(["Name", "Phone", "Email", "City"])

            # Contact rows
            for name, details in contacts.items():
                writer.writerow(
                    [name, details["phone"], details["email"], details["city"]]
                )

        print("[SUCCESS] Contacts exported to 'contacts.csv' successfully!")

    except IOError:
        print("[ERROR] Failed to export contacts.")


def main():
    """Main application loop handler."""
    contacts = load_contacts()

    while True:
        print("\n=============================")
        print("    CONTACT BOOK CLI MENU    ")
        print("=============================")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_all_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            export_contacts_csv(contacts)

        elif choice == "7":
            print("\nGoodbye! Your data is saved safely.")
            break

        else:
            print("[ERROR] Invalid selection. Please choose an option from 1 to 7.")


if __name__ == "__main__":
    main()
