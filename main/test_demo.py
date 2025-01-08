import time

from constant import *
import logging
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions.WebDriverException
from utils import *
#
# # Set up Chrome options
# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)
# wait = WebDriverWait(driver, 10)
authorizationToken = get_committee_token()


# # POST Add Election Template
# def test_add_election():
#     try:
#         random_name = "".join(random.choices(string.ascii_letters, k=7))
#         payload = json.dumps({
#             "templateId": 566565,
#             "description": random_name,
#             "townId": "030",
#             "officeIds": [
#                 4
#             ],
#             "supervisorFlag": True
#         })
#         response = requests.request("POST", electionTemplateUrl + 'add', headers=headers, data=payload)
#         resp = response.json()
#         logging.info(resp)
#         assert response.status_code == 200 or response.status_code == 201
#         logging.info('Added successfully')
#
#     except AssertionError as e:
#         logging.error(f'Assertion error: {e}')
#         logging.info('Failed')
#         raise
#
#
# # PUT Update Election Template
# def test_update_election_template():
#     try:
#
#         payload = json.dumps({
#             "templateId": 112,
#             "description": "COUNTY",
#             "townId": "",
#             "officeIds": [
#                 1,
#                 4
#             ],
#             "supervisorFlag": True
#         })
#
#         response = requests.request("PUT",  electionTemplateUrl+'update', headers=headers, data=payload)
#         resp = response.json()
#         logging.info(resp)
#         assert response.status_code == 200 or response.status_code == 201
#         logging.info('Updated successfully')
#
#     except AssertionError as e:
#         logging.error(f'Assertion error: {e}')
#         logging.info('Failed')
#         raise

# ---------------------------------------------------------------------------------------------------------------------


def test_CFRS_156_Notification_001():
    try:
        request_headers = {
            'Authorization': authorizationToken
        }
        response = requests.request("GET", notificationUrl+'getAllNotificationType', headers=request_headers, data={})
        data = response.json()
        logging.info(data)
        assert response.status_code == 200
        logging.info("Notification Type Fetched succesfully")

    except Exception as e:
        logging.error(e)
        raise e


def test_CFRS_156_Notification_002():
    try:
        request_headers = {
            'Authorization': authorizationToken
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


def test_CFRS_156_Notification_003():
    try:
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
            'Authorization': authorizationToken
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


def test_CFRS_156_Notification_004_005():
    try:
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
            'Authorization': authorizationToken
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


def test_candidate_registration():
    global driver, wait
    try:
        driver.get('https://cfs-qa.tgstechnology.net/public/home')
        driver.maximize_window()
        wait.until(EC.presence_of_element_located((By.ID, 'button1')))
        driver.find_element(By.ID, 'button1').click()
        driver.find_element(By.NAME, 'userName').send_keys('ETHAdmin')
        driver.find_element(By.NAME, 'password').send_keys('Admin@123')
        driver.find_element(By.XPATH, '//button[text()="Sign In"]').click()
        wait.until(EC.presence_of_element_located((By.ID, 'adminCommitteeSubmenu')))
        driver.find_element(By.ID, 'adminCommitteeSubmenu').click()
        logging.info('clicked at Committee menu')
        wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="New Registration"]')))
        driver.find_element(By.XPATH, '//a[text()="New Registration"]').click()
        logging.info('clicked at New')
        driver.find_element(By.ID, 'Add New Registration').click()
        logging.info('clicked at Add new')
        dropdown_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '(//div[@class="col-md-3"])[2]')))
        select = Select(dropdown_element)
        select.select_by_visible_text('State Candidate')
        time.sleep(10)
    except Exception as e:
        logging.error(e)


def test_add_worker():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url + transactionUrl, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=add_worker_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Payment to Worker added successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Payment to Worker added successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_add_worker: {e}")
        raise e


def test_add_loan():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url + transactionUrl, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=add_loan_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Loan added successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        transaction_id = response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Transaction ID: {transaction_id}")

        logging.info("Loan added successfully with correct response.")

        #     -update-
        update_loan_payload = json.dumps({
            "transactionID": transaction_id,
            "orgId": 24,
            "orgVersID": 1,
            "orgRegistrationID": 0,
            "entityTypeCode": "SE",
            "transactionAmount": 100,
            "transactionDate": "2024-12-01T13:00:00.000Z",
            "contributorPayeeID": 179,
            "contributorPayeeVersionID": 1,
            "transactionTypeCode": "LOAN"
        })
        response = requests.post(dev_committee_url + update_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=update_loan_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Loan updated successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        #     -delete-
        response = requests.post(dev_committee_url+delete_transactions+str(transaction_id), headers={}, data={})

        response_data = response.json()
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Loan deleted successfully.", \
            f"Unexpected message: {response_data.get('message')}"

    except Exception as e:
        logging.error(f"Error in test_add_loan: {e}")
        raise e


def test_add_debt():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url + transactionUrl, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=add_debt_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Debt added successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Debt added successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_add_debt: {e}")
        raise e


def test_get_all_transactions():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url+get_all_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=get_all_transactions_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        total_records = response_data.get("responseData", {}).get("totalRecords")
        logging.info(f"Total Records: {total_records}")
        logging.info("Total records fetched successfully .")

    except Exception as e:
        logging.error(f"Error in test_get_All_Transactions: {e}")
        raise e


# def test_ems():
#     global driver, wait
#     try:
#         driver.get('https://dev-ems.tgstechnology.net/voter-management/search?searchTab=focused')
#         driver.maximize_window()
#         # wait.until(EC.presence_of_element_located((By.ID, 'button1')))
#         # driver.find_element(By.ID, 'button1').click()
#         wait.until(EC.presence_of_element_located((By.ID, 'userName')))
#         time.sleep(5)
#         driver.find_element(By.ID, 'userName').send_keys('001hemang')
#         driver.find_element(By.ID, 'password').send_keys('Hemang@11111!')
#
#         driver.find_element(By.NAME, 'login').click()
#
#         # wait.until(EC.presence_of_element_located((By.ID, 'adminCommitteeSubmenu')))
#         # driver.find_element(By.ID, 'adminCommitteeSubmenu').click()
#         # logging.info('clicked at Committee menu')
#         # wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="New Registration"]')))
#         # driver.find_element(By.XPATH, '//a[text()="New Registration"]').click()
#         # logging.info('clicked at New')
#         # driver.find_element(By.ID, 'Add New Registration').click()
#         # logging.info('clicked at Add new')
#         # dropdown_element = wait.until(
#         #         EC.presence_of_element_located((By.XPATH, '(//div[@class="col-md-3"])[2]')))
#         # select = Select(dropdown_element)
#         # select.select_by_visible_text('State Candidate')
#         time.sleep(10)
#     except Exception as e:
#         logging.error(e)


def test_post_ecc_individual_registration():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_ECC_individual_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Electioneering Communication Committee(individual) Registration added successfully with"
                     " correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_ecc_individual_registration: {e}")
        raise e


def test_post_ecc_organization_registration():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_ECC_organization_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Electioneering Communication Committee(organization) Registration added successfully with"
                     " correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_ecc_organization_registration: {e}")
        raise e
