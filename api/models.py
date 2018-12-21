from random import randint
from datetime import datetime


class Users:
    """
    class for creating GET and POST
    for a user
    """

    def __init__(self, firstname, lastname, othernames, email, phoneNumber, username):

        self.id = randint(1,9999)
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.today()
        self.isAdmin = False


    def json_format(self):
        return {
        "id": self.id,
        "firstname": self.firstname,
        "lastname": self.lastname,
        "othernames": self.othernames,
        "email": self.email,
        "phoneNumber" : self.phoneNumber,
        "username": self.username,
        "registered": self.registered,
        "isAdmin": self.isAdmin

        }

