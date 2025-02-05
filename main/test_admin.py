from utils import *
#
# # Set up Chrome options
# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Get All Notification Type
def test_api_admin_notification_001():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        response = requests.request("GET", dev_admin_url + get_all_notifications_type,
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        notification_types = data.get("responseData", {}).get("notificationTypes", {})
        for notification in notification_types:
            logging.info(f"Code: {notification.get('code')}, Description: {notification.get('description')}")
        logging.info("Notification Type Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


# Get All Notification View Status
def test_api_admin_notification_002():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        response = requests.request("GET", dev_admin_url + get_all_notification_view_status,
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        notification_status = data.get("responseData", {}).get("viewStatus", {})
        for notification in notification_status:
            logging.info(f"Code: {notification.get('code')}, Description: {notification.get('description')}")
        logging.info("Notification View Status Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


# Get All Admin Notification Data List
def test_api_admin_notification_003():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        response = requests.request("POST", dev_admin_url + get_all_notifications_data_list,
                                    headers={'Content-Type': 'application / json',
                                             'Authorization': authorization_token}, data=get_all_notification_payload)
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info(data.get("responseData", {}).get("totalRecords"))
        logging.info("All Notification Data List Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


# Add, Update, Get By ID, Delete
def test_api_admin_notification_004_005_006_007():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        payload = {'Title': 'Form Submission Late',
                   'AdminNotification': 'this is description',
                   'ViewStatus': '432',
                   'AdminNotificationType': 'FC8',
                   'PostDate': '2024-10-10',
                   'ViewMode': 'Public',
                   'Id': '0'}

        response = requests.request("POST", dev_admin_url + add_edit_notification,
                                    headers={'Authorization': authorization_token}, data=payload)
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        notification_id = data['responseData']['id']
        logging.info(notification_id)
        logging.info("Notification added succesfully")
    #     ------ update -----
        payload = {'Title': 'Form Submission',
                   'AdminNotification': 'this is description',
                   'ViewStatus': '432',
                   'AdminNotificationType': 'FC8',
                   'PostDate': '2024-10-10',
                   'ViewMode': 'Public',
                   'Id': notification_id}
        response = requests.request("POST", dev_admin_url + add_edit_notification,
                                    headers={'Authorization': authorization_token}, data=payload)
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info("Notification edited succesfully")
    #     Get By ID
        response = requests.request("GET", dev_admin_url + get_notification_by_Id + str(notification_id),
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info("Notification Fetched Succesfully")
    #     -------- delete -------
        response = requests.request("POST", dev_admin_url + delete_notification + str(notification_id),
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info("Notification deleted succesfully")

    except Exception as e:
        logging.error(e)
        raise e


# Get All Admin Notification and For Badges
def test_api_admin_notification_008_009():
    try:
        # Get All Admin Notification
        authorization_token = get_token(dev_login_admin_payload)
        response = requests.request("GET", dev_admin_url + get_all_admin_notification,
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info("All Admin Notification Fetched succesfully")

        # Get All Admin Notification For Badges
        logging.info("----- Get All Admin Notification For Badges -----")
        authorization_token = get_token(dev_login_admin_payload)
        response = requests.request("GET", dev_admin_url + get_all_notification_for_badges,
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info("All All Notification For Badges Succesfully")

        logging.info("")
    except Exception as e:
        logging.error(e)


# Committee Summary
# Get Org Details For Correct Registration By Org ID and Submit Correct Registration
def test_api_admin_committee_summary_001_002():
    try:
        # Register new committee to get ID
        authorization_token = get_token(dev_login_admin_payload)

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_random_candidate_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Candidate Registration added successfully with correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    #   Get Org Details For Correct Registration By Org ID
        logging.info('---- Get Org Details For Correct Registration By Org ID ----')
        response = requests.request("GET", dev_admin_url + get_org_details_for_correct_registration_by_org_id
                                    + str(registration_id),
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        org_id = data.get("responseData", {}).get("orgAmendDetails", {}).get("orgDetails", {}).get("orgID", None)
        logging.info(org_id)
        assert org_id is not None, "orgID is None in the response"
        assert org_id == registration_id, f"orgID ({org_id}) does not match registrationID ({registration_id})"

        logging.info("Org Details For Correct Registration Fetched succesfully")

    #  Submit Correct Registration
        logging.info('---- Submit Correct Registration ----')
        payload = correct_registration_payload.copy()
        payload["orgDetails"]["orgID"] = int(org_id)

        response = requests.request("POST", dev_admin_url + submit_correct_registration,
                                    headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                    data=json.dumps(payload))
        data = response.json()
        logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, f"isSuccess is not True"
        assert data.get("message") == "Registration updated successfully.", \
            f"Unexpected message: {data.get('message')}"

        logging.info("Registration updated successfully")
    except Exception as e:
        logging.error(f"Error in test_post_candidate_registrations: {e}")
        raise e

