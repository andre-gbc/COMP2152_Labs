contacts = {
    "Alice": "555-1254",
    "Bob": "555-5678",
    "Charlie": "555-8765",
}
print("Alice number: ", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after Diana", contacts)
contacts["Bob"] = "555-0000"
print("Contacts after Bob change", contacts)
del contacts["Charlie"]
print("Contacts after Charlie deletion", contacts)
print("All names:", contacts.keys())
print("All numbers:", contacts.values())

