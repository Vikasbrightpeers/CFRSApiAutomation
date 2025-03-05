from utils import *

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


# Add, Update, Get By ID, Delete Notification
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


# Committee Summary - Get Org Details For Correct Registration By Org ID and Submit Correct Registration
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


# Committee Transaction - Get Contribution and Expenditure Chart Data
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


# correspondence - Get correspondence data list, org info for correspondence data list, Add correspondence
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


# Committee Report - Get org filed report data list
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


# Committee Documents -  Get All Org Documents Data List
def test_api_admin_committee_documents_001_002_003_004():
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

        # Get Org Documents By Document ID
        logging.info("------- Get Org Documents By Document ID -------")
        response = requests.get(dev_admin_url + get_org_documents_by_document_id + "1011",
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        logging.info(response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Document Name:" f" {data.get("responseData", {}).get("documentName")}")
        logging.info("Org Documents Details By Document ID Fetched Succesfully")

    #     Delete Org Document
        logging.info("------- Delete Org Document -------")
        payload = delete_document_payload.copy()
        payload["docId"] = 1011
        response = requests.post(dev_admin_url + delete_org_document,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(payload))
        data = response.json()
        logging.info(data)
        logging.info(response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Message:" f" {data.get("message", {})}")
        logging.info("Documents Deleted Succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_committee_documents_001_002_003_004: {e}")
        raise e


# Committee registration
def test_api_admin_committee_registration_001_009_010_011_015_016_017():
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
        logging.error(f"Error in test_api_admin_committee_registration_001_009_010_011_012_015_016_017: {e}")
        raise e


def test_api_admin_committee_registration_012_013_014():
    try:
        authorization_token = get_admin_token()
        # Create committee for OrgId
        registration_id = committee_registration(authorization_token)

        #  Edit Pending Org Registration Status
        logging.info("----- Edit Pending Org Registration Status for Active-----")
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

        logging.info("----- Edit Pending Org Registration Status for Accept Conditionally -----")
        payload = edit_pending_org_registration_status_payload.copy()
        payload["orgStatusCode"] = "CNDA"
        payload["orgStatusReasonCode"] = "CFR"
        payload["statusReasonComment"] = ("The Secretary of State's office has not received a CFRS Authorization for "
                                          "this committee's account.")
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

        logging.info("----- Edit Pending Org Registration Status for Reject -----")
        payload = edit_pending_org_registration_status_payload.copy()
        payload["orgStatusCode"] = "RJCT"
        payload["orgStatusReasonCode"] = "SOI"
        payload["statusReasonComment"] = ("The statement of support or opposition in the committee's registration "
                                          "does not provide sufficient information to indicate what the committee"
                                          " supports or opposes.")
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

    except Exception as e:
        logging.error(f"Error in test_api_admin_committee_registration_012_013_014: {e}")
        raise e


# Admin Report
def test_api_admin_admin_report_001_002_003():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Get Admin sub report type
        report_types = ["ORG", "CAN", "FLN"]
        for report_type in report_types:
            logging.info(f"------- Get Admin sub report type - {report_type} -------")
            response = requests.get(
                f"{dev_admin_url}{admin_sub_report_type}{report_type}",
                headers={'Authorization': authorization_token},
                data={}
            )
            data = response.json()
            logging.info(data)
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
            assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info("Admin sub report type list fetched succesfully")
    except Exception as e:
        logging.error(f"Error in test_api_admin_admin_report_001_002_003: {e}")
        raise e


# Audit review
def test_api_admin_audit_review_001_002_003_004_005_006_007_008_009_011_012_013_014_015():
    try:
        authorization_token = get_token(dev_login_admin_payload)

        # Get All Transaction for Audit Review Data List
        logging.info(f"------- Get All Transaction for Audit Review Data List-------")
        response = requests.post(dev_admin_url + get_all_transaction_for_audit_review_data_list,
                                 headers={'Authorization': authorization_token,  'Content-Type': 'application/json'},
                                 data=json.dumps(get_all_transaction_for_audit_review_data_list_payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All Transaction for Audit Review Data List fetched succesfully")

        # Get All Reports for Audit Review Data List
        logging.info(f"------- Get All Reports for Audit Review Data List-------")
        response = requests.post(dev_admin_url + get_all_report_for_audit_review_data_list,
                                 headers={'Authorization': authorization_token,  'Content-Type': 'application/json'},
                                 data=json.dumps(get_all_report_for_audit_review_data_list_payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All Reports for Audit Review Data List fetched succesfully")

        # Get All Committee for Audit Review Data List
        logging.info(f"------- Get All Committee for Audit Review Data List-------")
        response = requests.post(dev_admin_url + get_all_committee_for_audit_review_data_list,
                                 headers={'Authorization': authorization_token,  'Content-Type': 'application/json'},
                                 data=json.dumps(get_all_report_for_audit_review_data_list_payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All Committees for Audit Review Data List fetched succesfully")

        # Get compliance information by org compliance id
        logging.info(f"------- Get compliance information by org compliance id-------")
        response = requests.get(dev_admin_url + get_compliance_information_by_org_compliance_id + "1006",
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("orgName") == "Maller, Marsh f"
        logging.info("compliance information by org compliance id fetched succesfully")

        # Update compliance status Open/Close
        logging.info(f"------- Update compliance status -------")
        for status in ["OP", "CL"]:
            logging.info(f"Updating compliance status to {status}")
            payload = update_compliance_status_payload.copy()
            payload["complianceStatusCode"] = status
            response = requests.post(dev_admin_url + update_compliance_status,
                                     headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                     data=json.dumps(payload))
            data = response.json()
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
            assert data.get("isSuccess"), "isSuccess is not True in response"
            logging.info("Compliance Status updated successfully")

        #    ------------------ Add Edit Get Violation ------------------
        # Add  Violation
        logging.info(f"------- Add  Violation-------")
        payload = add_edit_violation_payload.copy()
        payload["violationDate"] = "2025-02-25"
        payload["violationStatusCode"] = "OP"
        payload["violationAmount"] = 2612
        payload["orgComplianceID"] = 1006
        payload["orgID"] = 2
        response = requests.post(dev_admin_url + add_edit_violation,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("orgComplianceID") == 1006
        assert data.get("responseData", {}).get("violationAmount") == 2612
        assert data.get("message") == "Violation created successfully.", f"Unexpected message: {data.get('message')}"
        violation_id = data.get("responseData", {}).get("violationID")
        logging.info(f"Violation ID : {violation_id}")
        logging.info("Violation created successfully")

        # Edit  Violation
        logging.info(f"------- Edit  Violation-------")
        payload = add_edit_violation_payload.copy()
        payload["violationDate"] = "2025-02-25"
        payload["violationStatusCode"] = "OP"
        payload["violationAmount"] = 1226
        payload["orgComplianceID"] = 1006
        payload["orgID"] = 2
        payload["violationID"] = violation_id
        response = requests.post(dev_admin_url + add_edit_violation,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("orgComplianceID") == 1006
        assert data.get("responseData", {}).get("violationAmount") == 1226
        assert data.get("message") == "Violation updated successfully.", f"Unexpected message: {data.get('message')}"
        logging.info("Violation updated successfully")

        # Get violation by id
        logging.info(f"------- Get violation by id-------")
        response = requests.get(dev_admin_url + get_violation_by_id + str(violation_id),
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("violationID") == violation_id
        assert data.get("responseData", {}).get("violationAmount") == 1226
        logging.info("Violation data by ID  fetched succesfully")

    #    ------------------ Add Edit Delete Get Violation Payment ------------------
        logging.info(f"------- Add Violation Payment -------")
        payload = add_edit_violation_payment_payload.copy()
        payload["paymentDate"] = "2025-02-25"
        payload["paymentTypeCode"] = 2
        payload["violationID"] = violation_id
        payload["paymentAmount"] = 2
        payload["orgComplianceID"] = 1006
        payload["orgID"] = 3
        response = requests.post(dev_admin_url + add_edit_violation_payment,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("paymentAmount") == 2
        assert data.get("message") == "Violation Payment added successfully.", \
            f"Unexpected message: {data.get('message')}"
        payment_id = data.get("responseData", {}).get("paymentID")
        logging.info(f"Payment ID : {payment_id}")
        logging.info("Violation payment added successfully")

    #      Edit Violation Payment
        logging.info(f"------- Edit  Violation Payment -------")
        payload = edit_violation_payment_payload.copy()
        payload["paymentDate"] = "2025-02-25"
        payload["paymentTypeCode"] = 2
        payload["paymentAmount"] = 1
        payload["paymentID"] = payment_id
        response = requests.post(dev_admin_url + add_edit_violation_payment,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("paymentAmount") == 1
        assert data.get("responseData", {}).get("paymentID") == payment_id
        assert data.get("message") == "Violation Payment updated successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info(f"Violation Payment({payment_id}) updated successfully")

    #     Get violation payment by ID
        logging.info(f"------- Get violation payment by ID -------")
        response = requests.get(dev_admin_url + get_violation_payment_by_id + str(payment_id),
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("violationID") == violation_id
        assert data.get("responseData", {}).get("paymentAmount") == 1
        logging.info(f"Violation payment data by ID {payment_id} fetched succesfully")

        # Get All violation payment data list
        logging.info(f"------- Get All violation payment data list -------")
        payload = get_all_violation_payment_data_list_payload.copy()
        payload["violationID"] = violation_id
        response = requests.post(dev_admin_url + get_all_violation_payment_data_list,
                                 headers={'Authorization': authorization_token,  'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All violation payment data fetched succesfully")

        #     Delete  violation payment by ID
        logging.info(f"------- Delete violation payment by ID -------")
        response = requests.post(dev_admin_url + delete_violation_payment + str(payment_id),
                                 headers={'Authorization': authorization_token}, data={})
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Violation Payment deleted successfully.", \
            f"Unexpected message: {data.get('message')}"

        logging.info(f"Violation Payment ID {payment_id} deleted successfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_audit_review_001_002_003_004_005_006_007_011_012_013_014_015: {e}")
        raise e


# Add Edit Get Delete Violation Waiver
def test_api_admin_audit_review_016_017_018_019_020():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Add  Violation for Add Waiver
        logging.info(f"------- Add  Violation-------")
        payload = add_edit_violation_payload.copy()
        payload["violationDate"] = "2025-02-25"
        payload["violationStatusCode"] = "OP"
        payload["violationAmount"] = 2612
        payload["orgComplianceID"] = 1006
        payload["orgID"] = 2
        response = requests.post(dev_admin_url + add_edit_violation,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("orgComplianceID") == 1006
        assert data.get("responseData", {}).get("violationAmount") == 2612
        assert data.get("message") == "Violation created successfully.", f"Unexpected message: {data.get('message')}"
        violation_id = data.get("responseData", {}).get("violationID")
        logging.info(f"Violation ID : {violation_id}")
        logging.info("Violation created successfully")

        # Add  Violation Waiver
        logging.info(f"------- Add  Violation Waiver -------")
        payload = add_edit_violation_waiver_payload.copy()
        payload["orgComplianceID"] = 1006
        payload["orgID"] = 2
        payload["violationID"] = violation_id
        payload["violationID"] = violation_id
        response = requests.post(dev_admin_url + add_edit_violation_waiver,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Violation Waiver Added successfully.", \
            f"Unexpected message: {data.get('message')}"
        waiver_request_id = data.get("responseData", {}).get("waiverRequestID")
        logging.info(f"Waiver Request ID : {waiver_request_id}")
        logging.info("Violation Waiver Added successfully")

        # Edit  Violation waiver
        logging.info(f"------- Edit  Violation waiver -------")
        payload = add_edit_violation_waiver_payload.copy()
        payload["orgComplianceID"] = 1006
        payload["orgID"] = 2
        payload["violationID"] = violation_id
        payload["waiverRequestID"] = waiver_request_id
        response = requests.post(dev_admin_url + add_edit_violation_waiver,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("waiverRequestID") == waiver_request_id
        assert data.get(
            "message") == "Violation Waiver Updated successfully.", f"Unexpected message: {data.get('message')}"
        logging.info(f"Violation Waiver ({waiver_request_id}) updated successfully")

        #     Get violation waiver request by ID
        logging.info(f"------- Get violation waiver request by ID -------")
        response = requests.get(dev_admin_url + get_violation_waiver_by_id + str(waiver_request_id),
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("violationID") == violation_id
        logging.info(f"Violation waiver request data by ID {waiver_request_id} fetched succesfully")

        # Get All violation waiver request data list
        logging.info(f"------- Get All violation waiver request data list -------")
        payload = get_all_violation_payment_data_list_payload.copy()
        payload["violationID"] = violation_id
        response = requests.post(dev_admin_url + get_all_violation_waiver_data_list,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All violation waiver request data fetched succesfully")

        #     Delete  violation waiver request by ID
        logging.info(f"------- Delete violation waiver request by ID -------")
        response = requests.post(dev_admin_url + delete_violation_waiver + str(waiver_request_id),
                                 headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Violation Waiver Deleted successfully.", \
            f"Unexpected message: {data.get('message')}"

        logging.info(f"Violation waiver request ID {waiver_request_id} deleted successfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_audit_review_016_017_018_019_020: {e}")
        raise e


# Reporting Schedule
# Add Edit Get Delete Election
def test_api_admin_reporting_schedule_001_002_003_004():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Add Election
        logging.info(f"------- Add Election-------")
        payload = add_edit_election_payload.copy()
        payload["allJurisdiction"] = False
        payload["jurisdictionCode"] = "CO"
        payload["electionTypeCode"] = "G"
        payload["primaryDate"] = "2025-03-03"
        payload["electionDate"] = "2025-03-03"
        payload["electionCategoryCode"] = "C"
        response = requests.post(dev_admin_url + add_edit_election,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Election created successfully.", f"Unexpected message: {data.get('message')}"
        election_id = data.get("responseData", {}).get("electionID")
        logging.info(f"Election Name : {data.get("responseData", {}).get("electionName")}")
        logging.info(f"Election ID : {election_id}")
        logging.info("Election created successfully")

        # Edit Election
        logging.info(f"------- Edit Election -------")
        payload["allJurisdiction"] = False
        payload["jurisdictionCode"] = "CO"
        payload["electionTypeCode"] = "G"
        payload["primaryDate"] = "2025-03-03"
        payload["electionDate"] = "2025-03-03"
        payload["electionCategoryCode"] = "C"
        payload["electionID"] = election_id
        response = requests.post(dev_admin_url + add_edit_election,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("electionID") == election_id
        assert data.get("message") == "Election updated successfully.", f"Unexpected message: {data.get('message')}"
        logging.info(f"Election ID : ({election_id}) updated successfully")
        # Get Election by ID - Not implemented
        # logging.info(f"------- Get Election by ID -------")
        # response = requests.get(dev_admin_url + get_election_by_id + str(election_id),
        #                         headers={'Authorization': authorization_token}, data={})
        # data = response.json()
        # assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        # assert data.get("isSuccess") is True, "isSuccess is not True in response"
        # assert data.get("responseData", {}).get("electionID") == election_id
        # logging.info(f"Election By ID {election_id} fetched succesfully")

        # Delete Election by ID
        logging.info(f"------- Delete Election by ID -------")
        response = requests.post(dev_admin_url + delete_election_by_id + str(election_id),
                                 headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData") == "deleted successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info(f"Election ID: {election_id} deleted successfully")

        # Get All Election Data List
        logging.info(f"------- Get All Election Data List -------")
        response = requests.post(dev_admin_url + get_all_election_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(get_all_election_data_list_payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Election Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All Election Data List Fetched succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_reporting_schedule_001_002_003_004: {e}")
        raise e


# Add, Edit, Get by ID, Get, Delete Reporting Cycle
def test_api_admin_reporting_schedule_005_006_007_008_009():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Add Election to use while creating the R.C
        logging.info(f"------- Add Election-------")
        payload = add_edit_election_payload.copy()
        payload["allJurisdiction"] = False
        payload["jurisdictionCode"] = "CO"
        payload["electionTypeCode"] = "G"
        payload["primaryDate"] = "2025-03-03"
        payload["electionDate"] = "2025-03-03"
        payload["electionCategoryCode"] = "C"
        response = requests.post(dev_admin_url + add_edit_election,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        election_id = data.get("responseData", {}).get("electionID")
        logging.info(f"Election ID : {election_id}")

        # Add Reporting Cycle
        logging.info(f"------- Add Reporting Cycle -------")
        payload = add_edit_reporting_cycle_payload.copy()
        payload["electionid"] = election_id
        payload["periodStartDate"] = "2025-03-01"
        payload["periodEndDate"] = "2025-03-31"
        payload["regStartDate"] = "2025-03-01"
        payload["regEndDate"] = "2025-03-03"
        payload["regDueDate"] = "2025-03-31"
        response = requests.post(dev_admin_url + add_edit_reporting_cycle,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        # logging.info(data)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Reporting Cycle created successfully.", f"Unexpected message: {data.get('message')}"
        reporting_cycle_id = data.get("responseData", {}).get("reportingCycleID")
        logging.info(f"Reporting Cycle Name: {data.get("responseData", {}).get("description")}")
        logging.info(f"Reporting Cycle ID : {reporting_cycle_id}")
        logging.info("Reporting Cycle created successfully.")

        # Edit Reporting Cycle
        logging.info(f"------- Edit Reporting Cycle -------")
        payload["allJurisdiction"] = False
        payload["jurisdictionCode"] = "CO"
        payload["electionTypeCode"] = "G"
        payload["primaryDate"] = "2025-03-03"
        payload["electionDate"] = "2025-03-03"
        payload["electionCategoryCode"] = "C"
        payload["reportingCycleID"] = reporting_cycle_id
        response = requests.post(dev_admin_url + add_edit_reporting_cycle,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("reportingCycleID") == reporting_cycle_id
        assert data.get("message") == "Reporting Cycle updated successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info(f"Reporting Cycle : ({reporting_cycle_id}) updated successfully")

        # Get Reporting Cycle by ID
        logging.info(f"------- Get Reporting Cycle By ID -------")
        response = requests.get(dev_admin_url + get_reporting_cycle_by_id + str(reporting_cycle_id),
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("reportingCycleID") == reporting_cycle_id
        logging.info(f"Reporting Cycle By ID {reporting_cycle_id} fetched succesfully")

        # Delete Reporting Cycle by ID
        logging.info(f"------- Delete Reporting Cycle by ID -------")
        response = requests.post(dev_admin_url + delete_reporting_cycle_by_id + str(reporting_cycle_id),
                                 headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData") == "deleted successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info(f"Reporting Cycle: {reporting_cycle_id} deleted successfully")

        # Get All Reporting Cycle Data List
        logging.info(f"------- Get All Reporting Cycle Data List -------")
        response = requests.post(dev_admin_url + get_all_reporting_cycle_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(get_all_election_data_list_payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Reporting Cycle Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All Reporting Cycle Data List Fetched succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_reporting_schedule_005_006_007_008_009: {e}")
        raise e


# Add, Edit, Get by ID, Get, Delete Reporting Period
def test_api_admin_reporting_schedule_010_011_012_013_014():
    try:
        authorization_token = get_token(dev_login_admin_payload)
        # Add Election to use while creating the R.C
        logging.info(f"------- Add Election-------")
        payload = add_edit_election_payload.copy()
        payload["allJurisdiction"] = False
        payload["jurisdictionCode"] = "CO"
        payload["electionTypeCode"] = "G"
        payload["primaryDate"] = "2025-03-03"
        payload["electionDate"] = "2025-03-03"
        payload["electionCategoryCode"] = "C"
        response = requests.post(dev_admin_url + add_edit_election,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        election_id = data.get("responseData", {}).get("electionID")
        logging.info(f"Election ID : {election_id}")

        # Add Reporting Cycle to use while creating the Reporting Period
        logging.info(f"------- Add Reporting Cycle -------")
        payload = add_edit_reporting_cycle_payload.copy()
        payload["electionid"] = election_id
        payload["periodStartDate"] = "2025-03-01"
        payload["periodEndDate"] = "2025-03-31"
        payload["regStartDate"] = "2025-03-01"
        payload["regEndDate"] = "2025-03-03"
        payload["regDueDate"] = "2025-03-31"
        response = requests.post(dev_admin_url + add_edit_reporting_cycle,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("message") == "Reporting Cycle created successfully.", f"Unexpected message: {data.get('message')}"
        reporting_cycle_id = data.get("responseData", {}).get("reportingCycleID")
        logging.info(f"Reporting Cycle ID : {reporting_cycle_id}")
        logging.info("Reporting Cycle created successfully.")
        # ------------------------------------------------------------------------------------------
        # Add Reporting Period
        logging.info(f"------- Add Reporting Period -------")
        payload = add_edit_reporting_period_payload.copy()
        payload["electionid"] = election_id
        payload["reportingCycleID"] = reporting_cycle_id
        payload["formType"] = "201"
        payload["reportingPeriodType"] = "OPT"
        payload["reportTypeCode"] = "1007"
        payload["beginDate"] = "2025-03-03"
        payload["endDate"] = "2025-03-31"
        payload["allowableFilingPeriodBeginDate"] = "2025-03-04"
        payload["dueDate"] = "2025-04-29"
        response = requests.post(dev_admin_url + add_edit_reporting_period,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get(
            "message") == "Reporting Period created successfully.", f"Unexpected message: {data.get('message')}"
        reporting_period_id = data.get("responseData", {}).get("reportingPeriodID")
        logging.info(f"Reporting Period ID : {reporting_period_id}")
        logging.info("Reporting Period created successfully.")

        # Edit Reporting Period
        logging.info(f"------- Edit Reporting Period -------")
        payload = add_edit_reporting_period_payload.copy()
        payload["electionid"] = election_id
        payload["reportingCycleID"] = reporting_cycle_id
        payload["formType"] = "201"
        payload["reportingPeriodType"] = "OPT"
        payload["reportTypeCode"] = "1007"
        payload["beginDate"] = "2025-03-03"
        payload["endDate"] = "2025-03-31"
        payload["allowableFilingPeriodBeginDate"] = "2025-03-04"
        payload["dueDate"] = "2025-04-29"
        payload["reportingPeriodID"] = reporting_period_id
        response = requests.post(dev_admin_url + add_edit_reporting_period,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("reportingPeriodID") == reporting_period_id
        assert data.get("message") == "Reporting Period updated successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info(f"Reporting Period : ({reporting_period_id}) updated successfully")

        # Get Reporting Period by ID
        logging.info(f"------- Get Reporting Period By ID -------")
        response = requests.get(dev_admin_url + get_reporting_period_by_id + str(reporting_period_id),
                                headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData", {}).get("reportingPeriodID") == reporting_period_id
        logging.info(f"Reporting Period By ID {reporting_period_id} fetched succesfully")

        # Delete Reporting Period by ID
        logging.info(f"------- Delete Reporting Period by ID -------")
        response = requests.post(dev_admin_url + delete_reporting_period_by_id + str(reporting_period_id),
                                 headers={'Authorization': authorization_token}, data={})
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        assert data.get("responseData") == "deleted successfully.", \
            f"Unexpected message: {data.get('message')}"
        logging.info(f"Reporting Period: {reporting_period_id} deleted successfully")

        # Get All Reporting Period Data List
        logging.info(f"------- Get All Reporting Period Data List -------")
        response = requests.post(dev_admin_url + get_all_reporting_period_data_list,
                                 headers={'Content-Type': 'application/json', 'Authorization': authorization_token},
                                 data=json.dumps(get_all_election_data_list_payload))
        data = response.json()
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total Reporting Period Records : {data.get("responseData", {}).get("totalRecords")}")
        logging.info("All Reporting Period Data List Fetched succesfully")

    except Exception as e:
        logging.error(f"Error in test_api_admin_reporting_schedule_010_011_012_013_014: {e}")
        raise e
