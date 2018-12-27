from random import randint
from datetime import datetime


class Users:
    """
    class for creating GET and POST
    for a user
    """

    def __init__(self, firstname, lastname, email, **kwargs):

        self.id = randint(1,9999)
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = kwargs['othernames']
        self.email = email
        self.phoneNumber = kwargs['phoneNumber']
        self.username = kwargs['username']
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

class RedFlag:
    def __init__(self, createdBy, types,**kwargs):
        self.id = kwargs['id']
        self.createdOn = datetime.today()
        self.createdBy = createdBy
        self.types = types
        self.location = kwargs['location']
        self.status = kwargs['status']
        self.images = kwargs['images']
        self.videos = kwargs['videos']
        self.comment = kwargs['comment']

    def json_format(self):
        format = {
        "id": self.id,
        "createdOn": self.createdOn,
        "createdBy":self.createdBy,
        "types": self.types,
        "location": self.location,
        "status": self.status,
        "images": self.images,
        "videos": self.videos,
        "comment": self.comment
        }
        return format
