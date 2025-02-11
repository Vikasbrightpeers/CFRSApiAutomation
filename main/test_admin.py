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
        logging.error(f"Error in test_api_admin_notification_001: {e}")
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
        logging.error(f"Error in test_api_admin_notification_002: {e}")
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
        logging.error(f"Error in test_api_admin_notification_003: {e}")
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
        logging.error(f"Error in test_api_admin_notification_004_005_006_007: {e}")
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

    except Exception as e:
        logging.error(f"Error in test_api_admin_notification_008_009: {e}")
        raise e


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
        logging.error(f"Error in test_api_admin_committee_summary_001_002: {e}")
        raise e


# Committee Transaction
# Get Contribution and Expenditure Chart Data
def test_api_admin_committee_transaction_001_002():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        logging.info("------- Get Contribution Chart Data -------")
        response = requests.request("GET", dev_admin_url + get_contribution_chart_data,
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        if data.get("isSuccess"):
            for item in data.get("responseData", []):
                name = item.get("name")
                total_amount = item.get("totalAmount")
                logging.info(f"Name: {name}, Total Amount: {total_amount}")
        else:
            logging.error(f"Error in response: {data.get('message')}")
        logging.info("Contribution Chart Data Fetched succesfully")
    #
        logging.info("------- Get Expenditure Chart Data -------")
        response = requests.request("GET", dev_admin_url + get_expenditure_chart_data,
                                    headers={'Authorization': authorization_token}, data={})
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        if data.get("isSuccess"):
            for item in data.get("responseData", []):
                name = item.get("name")
                total_amount = item.get("totalAmount")
                logging.info(f"Name: {name}, Total Amount: {total_amount}")
        else:
            logging.error(f"Error in response: {data.get('message')}")
        logging.info("Expenditure Chart Data Fetched succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_committee_transaction_001_002: {e}")
        raise e


# correspondence
# Get correspondence data list, org info for correspondence data list, Add correspondence
def test_api_admin_correspondence_001_002_003():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Get correspondence data list
        logging.info("------- Get correspondence data list -------")
        response = requests.post(dev_admin_url + get_correspondence_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(get_correspondence_data_list_payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Correspondence data list Total Records:" f" {data.get("responseData", {}).get("totalRecords")}")
        logging.info("Get correspondence data list Fetched succesfully")
        # Get org info for correspondence data list
        logging.info("------- Get org info for correspondence data list -------")
        response = requests.post(dev_admin_url + get_org_info_for_correspondence_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(get_org_info_for_correspondence_data_list_payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Org info for Correspondence data list Total Records:" 
                     f" {data.get("responseData", {}).get("totalRecords")}")
        logging.info("Get org info for correspondence data list Fetched succesfully")

    #   Add correspondence
        logging.info("------- Add correspondence -------")
        response = requests.post(dev_admin_url + add_correspondence,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(add_correspondence_payload))
        data = response.json()
        logging.info(response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Correspondence added successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info("Correspondence added successfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_correspondence_001_002_003: {e}")
        raise e


# Committee Report
# Get org filed report data list
def test_api_admin_committee_report_001_002():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Get correspondence data list
        logging.info("------- Get org filed report data list -------")
        response = requests.post(dev_admin_url + get_org_filed_report_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(get_org_filed_report_data_list_payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Records:" f" {data.get("responseData", {}).get("totalRecords")}")
        logging.info("Get org filed report data list fetched succesfully")

        # Get org filed report amend history list
        logging.info("------- Get org filed report amend history list -------")
        response = requests.get(dev_admin_url + get_org_filed_report_amend_history + str(320),
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        try:
            for items in data.get("responseData", []):
                report_id = items.get("reportID")
                report_name = items.get("reportFileName")
                report_status = items.get("reportStatus")
                logging.info(f"Report ID - {report_id}\n"
                             f"Report Name - {report_name}\n"
                             f"Report Status - {report_status}")
        except Exception as e:
            logging.error(f"Error in response: {data.get('message')}")
            raise e
        logging.info("Get org filed report amend history list fetched succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_committee_report_001_002: {e}")
        raise e


# Committee Documents
# Get All Org Documents Data List
def test_api_admin_committee_api_admin_committee_documents_001_002():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Get All Org Documents Data List
        logging.info("------- Get All Org Documents Data List -------")
        payload = get_all_org_documents_data_list_payload.copy()
        payload["orgID"] = 432
        response = requests.post(dev_admin_url + get_all_org_documents_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(payload))
        data = response.json()
        logging.info(response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Org Documents Data List Total Records:" f" {data.get("responseData", {}).get("totalRecords")}")
        logging.info("Org Documents Data List Fetched Succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_committee_documents_001_002: {e}")
        raise e


# Committee registration
def test_api_admin_committee_registration_001_009_010_011_012_015_016_017():
    try:
        authorization_token = get_admin_token()
        # Submit Committee Registration Data
        logging.info("----- Submit Committee Registration Data -----")
        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_random_candidate_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")
        # logging.info(f"Response Body: {response_data}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Candidate Registration added successfully with correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    #     Get All Committee Registration Data List
        logging.info("----- Get All Committee Registration Data List -----")
        response = requests.post(dev_admin_url + get_all_committee_registrations, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=get_all_transactions_payload)

        response_data = response.json()
        logging.info(f"Response Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        total_records = response_data.get("responseData", {}).get("totalRecords")
        logging.info(f"Total Records: {total_records}")
        logging.info("Total records fetched successfully.")

    #     Get Committee Profile By Org ID
        logging.info("----- Get Committee Profile By Org ID -----")
        response = requests.get(dev_admin_url + get_committee_profile_by_org_id + str(registration_id), headers={
            'Authorization': authorization_token}, data={})
        response_data = response.json()
        logging.info(response_data)
        logging.info(f"Response Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info("Committee Profile By ID fetched successfully.")

    #     Get All Officers Information By Org ID
        logging.info("----- Get All Officers Information By Org ID -----")
        payload = get_all_officer_information_by_org_id_payload.copy()
        payload["orgId"] = int(registration_id)

        response = requests.post(dev_admin_url + get_all_officer_information_by_org_id, headers={
            'Authorization': authorization_token, 'Content-Type': 'application/json'
        }, data=json.dumps(payload))

        response_data = response.json()
        logging.info(response_data)
        logging.info(f"Response Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"

        logging.info("All Officers Information By Org ID fetched successfully.")

    #     Edit Pending Org Registration Status
        logging.info("----- Edit Pending Org Registration Status -----")
        payload = edit_pending_org_registration_status_payload.copy()
        payload["orgStatusCode"] = "ACTV"
        payload["orgId"] = int(registration_id)

        response = requests.post(dev_admin_url + edit_pending_org_registration_status, headers={
            'Authorization': authorization_token, 'Content-Type': 'application/json'
        }, data=json.dumps(payload))

        response_data = response.json()
        logging.info(response_data)
        logging.info(f"Response Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Registration status updated successfully.", \
            f"Unexpected message: {response_data.get('message')}"
        logging.info("Registration status updated successfully.")

    #     Get all org reasons by status code for Accept_Conditionally and Reject
        status_codes = {'Accept_Conditionally': Accept_Conditionally, 'Reject': Reject}
        for status_label, status_code in status_codes.items():
            logging.info(f"----- Get all org reasons by status code : {status_label}-----")
            response = requests.get(dev_admin_url + get_all_org_reasons_by_status_code + status_code, headers={
                'Authorization': authorization_token}, data={})

            response_data = response.json()
            logging.info(response_data)
            logging.info(f"Response Status Code: {response.status_code}")

            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
            assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
            if response_data.get("isSuccess"):
                org_status_reasons = response_data.get("responseData", {}).get("orgStatusReason", [])
                for item in org_status_reasons:
                    description = item.get("description")
                    related_description = item.get("relatedDescription")
                    logging.info(f"Description: {description}\n, Related Description: {related_description}")

            logging.info("All org reasons by status code fetched successfully.")
    #   View org registration report
        logging.info(f"----- View org registration report -----")
        url = dev_admin_url + view_org_registration_report + str(registration_id) + "/1"
        logging.info(url)
        response = requests.get(url, headers={
            'Authorization': authorization_token}, data={})
        response_data = response.json()
        logging.info(response_data)
        logging.info(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info("Org registration report fetched successfully.")

    except Exception as e:
        logging.error(f"Error in test_post_candidate_registrations: {e}")
        raise e
