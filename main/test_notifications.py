import time

import requests
from randomfunctions import *
from constant import *

from utils import *
#
# # Set up Chrome options
# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_get_notification_type():
    try:
        authorization_token = get_committee_token()
        request_headers = {
            'Authorization': authorization_token
        }
        response = requests.request("GET", notificationUrl+'getAllNotificationType', headers=request_headers, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        logging.info("Notification Type Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


def test_get_notification_status():
    try:
        authorization_token = get_committee_token()
        request_headers = {
            'Authorization': authorization_token
        }
        response = requests.request("GET", notificationUrl+'gettAllNotificationViewStatus',
                                    headers=request_headers, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        logging.info("Notification Status Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


def test_get_all_notification():
    try:
        authorization_token = get_committee_token()

        payload = json.dumps({
            "pageNumber": 1,
            "searchKeyword": "",
            "pageSize": 1,
            "sortColumn": "",
            "sortDirection": "",
            "notificationType": "",
            "notificationName": "",
            "postDate": "",
            "viewMode": "",
            "notificationStatus": "active"
        })
        request_headers = {
            'Content-Type': 'application / json',
            'Authorization': authorization_token
        }
        response = requests.request("POST", notificationUrl+'getAllAdminNotifications',
                                    headers=request_headers, data=payload)
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        logging.info("All Notification Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


def test_add_update_delete_notification():
    try:
        authorization_token = get_committee_token()

        payload = json.dumps({
            "id": 0,
            "title": "Hello ",
            "adminNotification": "this is description",
            "viewStatus": "abcd",
            "adminNotificationType": "abcd",
            "postDate": "2024-10-10",
            "viewMode": "abcd"
        })
        request_headers = {
            'Content-Type': 'application / json',
            'Authorization': authorization_token
        }
        response = requests.request("POST", notificationUrl+'addEditNotification',
                                    headers=request_headers, data=payload)
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        notification_id = data['responseData']['id']
        logging.info(notification_id)
        logging.info("Notification added succesfully")
    #     ------ update -----
        payload = json.dumps({
            "id": notification_id,
            "title": "Hello parth",
            "adminNotification": "this description",
            "viewStatus": "abcd",
            "adminNotificationType": "abcd",
            "postDate": "2024-10-10",
            "viewMode": "abcd"
        })
        response = requests.request("POST", notificationUrl + 'addEditNotification',
                                    headers=request_headers, data=payload)
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        logging.info("Notification edited succesfully")
    #     -------- delete -------
        response = requests.request("DELETE", notificationUrl + 'deleteNotification/' + str(notification_id),
                                    headers=request_headers, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        logging.info("Notification deleted succesfully")

    except Exception as e:
        logging.error(e)
        raise e
