
##Address Book

""" This is an address book to keep record of our friends and their personal
Info stored is name address b day and e mail"""


class AddressBook(object):
    """
    AddressBook instances hold and manage lists
    of people """
    def __init__(self):
        """Set people atribute to an empty list"""
        self.people = []

    def add_entry(self, new_entry):
        """ add an new entry to the list of people inthe addressbook the new_entry
            should be a instance of the AddressEntry class"""
        self.people.append(new_entry)
        
    


class AddressEntry(object):
    """
    AddressEntry instances hold and manage details of a person
    """
    def __init__(self, first_name=None, family_name=None,
		email_address=None,
		date_of_birth=None):
        """Initialize attributes first_name,
        family_name and date_of_birth.
        Each argument should be a string.
        date_of_birth should be of the form  "MM DD, YYYY"
        """
        self.first_name = first_name
        self.family_name = family_name
        self.email_address = email_address
        self.date_of_birth = date_of_birth



    def __repr__(self):
        """
        Given an AddressEntry object self return
        a readable string representation
        """
        template = "AddressEntry(first_name='%s', "+\
                   "family_name='%s', "+\
                   "email_address='%s', "+\
                   "date_of_birth='%s')"
        return template%(self.first_name, self.family_name,
                     self.email_address, self.date_of_birth)




if __name__ == "__main__":
    address_book = AddressBook()
    person1 = AddressEntry("Heather", "Drake", None, "01 01, 1970")
    print(person1)
    address_book.add_entry(person1)
    print(address_book.people)
    
