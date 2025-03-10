from utils import *
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# candidate_registration
def test_api_admin_committee_registration_001():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_random_candidate_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Candidate Registration added successfully with correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")
        return registration_id

    except Exception as e:
        logging.error(f"Error in test_post_candidate_registrations: {e}")
        raise e


# pre_candidate_registration
def test_api_admin_committee_registration_002():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_pre_candidate_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Pre-Candidate Registration added successfully with correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_pre_candidate_registrations: {e}")
        raise e


# pac_registration
def test_api_admin_committee_registration_003():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_pac_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Political Action Committee Registration added successfully with correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_pac_registrations: {e}")
        raise e


# ppc_ccc_registration
def test_api_admin_committee_registration_004():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_ppc_ccc_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Political Party Committee / Caucus Campaign Committee Registration added successfully with"
                     " correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_ppc_ccc_registration: {e}")
        raise e


# iec_individual_registration
def test_api_admin_committee_registration_005():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_IEC_individual_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Independent Expenditure Committee(individual) Registration added successfully with"
                     " correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_iec_individual_registration: {e}")
        raise e


# iec_organization_registration
def test_api_admin_committee_registration_006():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_admin_url + post_registration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_IEC_organization_registration_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Candidate Registration created successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Independent Expenditure Committee(organization) Registration added successfully with"
                     " correct response.")

        registration_id = response_data.get("responseData", {}).get("orgID")
        logging.info(f"Registration ID: {registration_id}")

    except Exception as e:
        logging.error(f"Error in test_post_iec_organization_registration: {e}")
        raise e


# ecc_individual_registration
def test_api_admin_committee_registration_007():
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


# ecc_organization_registration
def test_api_admin_committee_registration_008():
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


# get all
def test_api_admin_committee_registration_009():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url+get_all_committee_registrations, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=get_all_transactions_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        total_records = response_data.get("responseData", {}).get("totalRecords")
        logging.info(f"Total Records: {total_records}")
        logging.info("Total records fetched successfully .")

    except Exception as e:
        logging.error(f"Error in get_all_committee_transactions_payload: {e}")
        raise e
