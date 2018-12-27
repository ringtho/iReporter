import unittest
from api.routes import app
import json

class TestRedFlags(unittest.TestCase):

    def setUp(self):
        """initialise test client"""
        self.test_client = app.test_client()
        self.redflags = []
        self.incident = {"id": 1, "createdBy": 1, "types":"redflag", "location":"kampala", 
        "status": "rejected", "images": "image.jpg", "videos": "videos.org", 
        "comment": "my name is my name"}

    def test_delete_redflag(self):
        response = self.test_client.post("/api/v101/red-flags", json=self.incident)
        self.assertIn(response.json["data"][0]["message"], "red flag record created.")
        res = self.test_client.delete("/api/v101/red-flags/1")
        print(res)
        self.assertEqual(res.json["data"][0]["message"], "red-flag record has been deleted")
        self.assertEqual(res.json["data"][0]["id"], 1)
        
    # def test_users_when_empty(self):
    #     response = self.test_client.get("/api/v101/users")
    #     print(response)
    #     data = json.loads(response.data)
    #     print(data)
    #     self.assertEqual(response.status_code, 200)
    # #     self.assertIn("no users", data["message"])

    # def test_redflag_empty(self):
    #     response = self.test_client.get("/api/v101/red-flags")
    #     data = json.loads(response.data)
    #     print(data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(data["message"], "There are no red flags created")

    # def test_create_user(self):
    #     input_users = {"firstname": "Smith", "lastname": "Ringtho",
    #     "othernames":"J", "email": "sringtho@gmail.com", "phoneNumber": 783,
    #     "username":"sringtho"}
    #     response = self.test_client.post("/api/v101/users", json=input_users)
    #     self.assertEqual(response.status_code, 201)
    #     # self.assertIn("")

    def test_create_redflag(self):
        response = self.test_client.post("/api/v101/red-flags", json=self.incident)
        data =json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(data["data"][0]["message"], "red flag record created.")
        self.assertEqual(data["data"][0]["id"], 1)
        self.assertEqual(data["status"],201)
     
        

    def test_get_all_redflags(self):
        incidents = { "id": 2,"createdOn": "Tuesday","createdBy": 1, "types":"redflag", "location":"kampala", 
        "status": "rejected", "images": "image.jpg", "videos": "videos.org", 
        "comment": "my name is my name"}
        response = self.test_client.post("/api/v101/red-flags", json=incidents)

        incident = { "id": 1,"createdOn": "Monday","createdBy": 1, "types":"redflag", "location":"kampala", 
        "status": "accepted", "images": "image.jpg", "videos": "videos.org", 
        "comment": "my name is my name"}
        response2 = self.test_client.post("/api/v101/red-flags", json=incident)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response2.status_code, 201)
        self.assertIn(response.json["data"][0]["message"], "red flag record created.")
        self.assertIn(response2.json["data"][0]["message"], "red flag record created.")
        res = self.test_client.get("/api/v101/red-flags")
        self.assertEqual(res.status_code, 200)
        self.assertIn("rejected", res.json["data"][0]["status"])
        self.assertEqual(1, res.json["data"][0]["id"])
        

    def test_get_single_redflag(self):
        response = self.test_client.post("/api/v101/red-flags", json=self.incident)
        self.assertEqual(response.status_code, 201)
        res = self.test_client.get("/api/v101/red-flags/1")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["data"][0]["id"], 1)
        self.assertIn(data["data"][0]["status"], "rejected")


    def test_edit_location(self):
        incidents = { "id": 1,"createdOn": "Tuesday","createdBy": 1, "types":"redflag",
        "location":"kampala","status": "rejected", "images": "image.jpg", "videos": "videos.org", 
        "comment": "my name is my name"}
        response = self.test_client.post("/api/v101/red-flags", json=incidents)
        self.assertIn(response.json["data"][0]["message"], "red flag record created.")
        location = {"location": "mukono"}
        res = self.test_client.patch("/api/v101/red-flags/1/location" ,json=location)
        self.assertIn(res.json["data"][0]["message"], "Updated red-flag record's location")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["data"][0]["id"], 1)

    def test_edit_comment(self):
        response = self.test_client.post("/api/v101/red-flags", json = self.incident)
        self.assertIn(response.json["data"][0]["message"], "red flag record created.")
        comment = {"comment": "Museveni is so corrupt"}
        res = self.test_client.patch("/api/v101/red-flags/1/comment" ,json=comment)
        self.assertIn(res.json["data"][0]["message"], "Updated red-flag record's comment")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["data"][0]["id"], 1)






if __name__ == '__main__':
    unittest.main()