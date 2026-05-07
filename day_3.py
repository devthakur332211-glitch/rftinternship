# Initial Phonebook
phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780"
}

def add_contact(name, number):
    # Bonus: Prevent duplicate entries
    name_upper = name.upper()
    if name_upper in phonebook:
        print(f"Error: {name_upper} already exists!")
    else:
        phonebook[name_upper] = number
        print(f"Contact {name_upper} added successfully.")

def search_contact(query):
    # Bonus: Partial name search
    query_upper = query.upper()
    results = {k: v for k, v in phonebook.items() if query_upper in k}
    
    if results:
        print(f"Search results for '{query}':")
        for name, num in results.items():
            print(f"- {name}: {num}")
    else:
        print("No contacts found.")

def delete_contact(name):
    name_upper = name.upper()
    if name_upper in phonebook:
        del phonebook[name_upper]
        print(f"Contact {name_upper} deleted.")
    else:
        print("Contact not found.")

# --- Testing the Features ---
print("--- Initial Phonebook ---")
print(phonebook)

print("\n1. Adding Contact...")
add_contact("Rahul", "9988776655")
add_contact("AMIT", "0000000000") # Should trigger duplicate error

print("\n2. Searching Contact...")
search_contact("RA") # Should find Rahul and Riya (Partial search)

print("\n3. Deleting Contact...")
delete_contact("RIYA")

print("\n--- Final Phonebook ---")
print(phonebook)
