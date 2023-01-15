# Pixela Module

import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


class Pixela:
    def __init__(self, username, token):
        try:
            username.lower()
            self.__token = token
            self.__username = username
            self.__header = {
                "X-USER-TOKEN": self.__token
            }
            self.__url = f"https://pixe.la/@{self.__username}"
        except AttributeError:
            print("Please use an alphanumeric string [a-z]/[0-9] characters for username only.")
        else:
            if not username.isalnum():
                raise Exception("Please use an alphanumeric [a-z]/[0-9] characters for username only.")

    """Changes User Variables"""
    def create_user(self):
        endpoint = PIXELA_ENDPOINT
        parameter = {
            "token": self.__token,
            "username": self.__username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
            "message": "User Created Successfully",
            "isSuccess": True
        }
        response = requests.post(url=endpoint, json=parameter)
        response.raise_for_status()
        print(response.text)
        return response

    def update_user(self, new_token):
        endpoint = f"{PIXELA_ENDPOINT}/{self.__username}"
        parameter = {
            "newToken": new_token
        }
        response = requests.put(url=endpoint, json=parameter, headers=self.__header)
        response.raise_for_status()
        print(response.text)
        return response

    def delete_user(self):
        endpoint = f"{PIXELA_ENDPOINT}/{self.__username}"
        response = requests.delete(url=endpoint, headers=self.__header)
        response.raise_for_status()
        print(response.text)
        return response

    """Get/Set-up Profile Variables"""
    def get_url(self):
        return self.__url

    def get_profile(self):
        endpoint = f"{PIXELA_ENDPOINT}/@{self.__username}"
        response = requests.get(endpoint)
        response.raise_for_status()
        return response

    """Graph Functions"""
    def create_graph(self, graph_name, graph_id, color="shibafu", unit="commit", number_type="int"):
        endpoint = f"{PIXELA_ENDPOINT}/{self.__username}/graphs"
        parameters = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": number_type,
            "color": color
        }
        response = requests.post(url=endpoint, json=parameters, headers=self.__header)
        response.raise_for_status()
        print(response.text)
        return response

    def delete_graph(self, graph_id):
        endpoint = f"{PIXELA_ENDPOINT}/{self.__username}/graphs/{graph_id}"
        response = requests.delete(url=endpoint, headers=self.__header)
        print(response.text)
        return response

    """Pixel Functions"""
    def register_pixel(self, graph_id, date=datetime.date.today().strftime("%Y%m%d"),  quantity=1):
        endpoint = f"{PIXELA_ENDPOINT}/{self.__username}/graphs/{graph_id}"
        parameters = {
            "date": str(date),
            "quantity": str(quantity)
        }
        response = requests.post(url=endpoint, json=parameters, headers=self.__header)
        response.raise_for_status()
        print(response.text)
        return response

    def delete_pixel(self, graph_id, date):
        endpoint = f"{PIXELA_ENDPOINT}/{self.__username}/graphs/{graph_id}/{str(date)}"
        response = requests.delete(url=endpoint, headers=self.__header)
        response.raise_for_status()
        print(response.text)
        return response
