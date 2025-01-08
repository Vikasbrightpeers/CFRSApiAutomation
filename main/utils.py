import requests
import logging
from constant import *


def get_committee_token():
    try:
        response = requests.post(dev_auth_url + dev_login_url, json=dev_login_committee_payload)

        if response.status_code == 200:
            token = response.json().get("accessToken")
            logging.info("Token fetched successfully.")
            return f"Bearer {token}"
        else:
            logging.error(f"Failed to fetch token. Status Code: {response.status_code}, Response: {response.text}")
            raise Exception("Login failed. Cannot retrieve token.")
    except Exception as e:
        logging.error(f"Error in test_get_committee_token: {e}")
        raise e


def get_admin_token():
    try:
        response = requests.post(dev_auth_url + dev_login_url, json=dev_login_admin_payload)

        if response.status_code == 200:
            token = response.json().get("accessToken")
            logging.info("Token fetched successfully.")
            return f"Bearer {token}"
        else:
            logging.error(f"Failed to fetch token. Status Code: {response.status_code}, Response: {response.text}")
            raise Exception("Login failed. Cannot retrieve token.")
    except Exception as e:
        logging.error(f"Error in test_get_admin_token: {e}")
        raise e
