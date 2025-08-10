import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        data  = {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
        return data
    

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                return json.load(f)
        return []
    
    def save_contact(self):
        with open(self.filename, "w") as f:
            json.dump(self.contact, f, indent=4)
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contact()
    
    def list_contacts(self):
        if not self.contacts:
            print("No contacts found")
        for contact in self.contacts:
            print(f"{contact['name']} - {contact["phone"]} - {contact["email"]}")
    
    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        self.save_contact()
