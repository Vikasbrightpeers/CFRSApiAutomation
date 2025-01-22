import requests
import logging
from constant import *
from randomfunctions import *
from endpoints import *


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


def register_user_from_admin():
    """
    Function to register a new user. Utilizes random data generation and admin token for authentication.
    Returns the response data, including the generated username.
    """
    try:
        # Generate random user details
        first_name = generate_first_name()
        last_name = generate_last_name()
        email = generate_random_email()
        contact_number = generate_random_mobile_number()
        user_name = f"{first_name}{last_name}{random.randint(100, 999)}"

        payload = post_register_user_payload.copy()

        # Update the payload with dynamically generated data
        payload.update({
            "userName": user_name,
            "email": email,
            "contactNumber": contact_number,
            "firstName": first_name,
            "lastName": last_name,
        })

        admin_token = get_admin_token()

        response = requests.post(
            dev_auth_url + add_and_update_user,
            headers={'Authorization': admin_token, 'Content-Type': 'application/json'}, json=payload)

        if response.status_code == 200:

            response_data = response.json()
            assert response_data.get("isSuccess"), "Registration failed. isSuccess is False."
            logging.info(f"User registered successfully. Username: {user_name}")
            assert response_data.get("isSuccess"), "Failed to Add User"
            # assert response_data.get("message") == "User added successfully.", \
            #     f"Unexpected message: {response_data.get('message')}"

            # return response_data.get("responseData")
            return response_data

        else:
            logging.error(
                f"Failed to register user. Status Code: {response.status_code}, Response: {response.text}")
            raise Exception("User registration failed.")

    except Exception as e:
        logging.error(f"Error in register_user: {e}")
        raise e
