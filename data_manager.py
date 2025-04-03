
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.url_end_point = os.getenv("URL_ENDPOINT")
        self.users_end_point = os.getenv("USER_URL_ENDPOINT")
        self.AUTH_TOKEN_BEARER = os.getenv("AUTH_TOKEN_BEARER")
        self.HEADER = {
            "Authorization": f"Bearer {self.AUTH_TOKEN_BEARER}"
        }
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):

        response = requests.get(self.url_end_point, headers=self.HEADER)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.url_end_point}/{city['id']}",
                json=new_data,
                headers=self.HEADER
            )
            print(response.text)

    def get_customer_email(self):
        response = requests.get(self.users_end_point, headers=self.HEADER)
        data = response.json()
        print(data)
        self.customer_data = data['users']
        return self.customer_data




