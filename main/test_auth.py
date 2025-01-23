import logging

from utils import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Admin Dashboard
def test_get_admin_role():
    try:
        authorization_token = get_admin_token()

        response = requests.get(dev_auth_url + dev_my_admin_role_list, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        # assert response_data.get("message") == "Candida/te Registration created successfully.", \
        #     f"Unexpected message: {response_data.get('message')}"

        logging.info("Admin roles fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_get_admin_role: {e}")
        raise e


# Administrative Notes
def test_get_admin_notes_category():
    try:
        authorization_token = get_admin_token()

        response = requests.get(dev_auth_url + dev_admin_notes_category, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"

        logging.info("Admin notes category fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_get_admin_notes_category: {e}")
        raise e


def test_get_administrative_data_list():
    try:
        authorization_token = get_admin_token()
        payload = post_get_administrative_data_list_payload.copy()
        payload["pageNumber"] = 1
        payload["pageSize"] = 10
        payload["orgId"] = str(406)

        response = requests.post(dev_auth_url + dev_administrative_data_list, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=json.dumps(payload))

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Administrative Data Total Records:"
                     f" {response_data.get("responseData", {}).get("totalRecords")}")

        logging.info("Administrative Data fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_get_administrative_data_list: {e}")
        raise e


def test_add_administrative_notes():
    try:
        authorization_token = get_admin_token()

        response = requests.post(dev_auth_url + dev_add_administrative_notes, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=post_add_administrative_notes_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Administrative note added successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Administrative note added successfully.")

    except Exception as e:
        logging.error(f"Error in test_add_administrative_notes: {e}")
        raise e


# App Configure
def test_website_configuration():
    try:
        authorization_token = get_admin_token()

        response = requests.get(dev_auth_url + get_website_configuration, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info("website configuration fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_website_configuration: {e}")
        raise e


def app_page_configuration():
    try:
        authorization_token = get_admin_token()

        response = requests.get(dev_auth_url + get_app_page_configuration + "" + "", headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"

        logging.info("Page configuration fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_app_page_configuration: {e}")
        raise e


# Register, Login, Forgot Password
def test_register_forgot_username():
    try:
        user_data = register_user_from_admin()
        response_data = user_data.get("responseData", {})
        user_name = response_data.get("userName")
        logging.info(f"Username: {user_name}")

        message = user_data.get("message")
        logging.info(f"Message: {message}")
        assert message == "User added successfully.", f"Unexpected message: {message}"

        logging.info("User added successfully.")
        authorization_token = user_data.get('token')

        #   Forgot username
        logging.info("------- Forgot Username -------")
        first_name = response_data.get("firstName")
        logging.info(f"Username: {first_name}")

        last_name = response_data.get("lastName")
        logging.info(f"Last Name: {last_name}")

        email_id = response_data.get("email")
        logging.info(f"Email ID: {email_id}")

        payload = post_forgot_username_payload.copy()
        payload["firstName"] = first_name
        payload["lastName"] = last_name
        payload["email"] = email_id

        forgot_user_name_response = requests.post(dev_auth_url + forgot_username,
                                                  headers={'Authorization': authorization_token,
                                                           "Content-Type": "application/json"},
                                                  data=json.dumps(payload))

        forgot_user_name_response_data = forgot_user_name_response.json()
        logging.info(forgot_user_name_response_data)

        logging.info(f"Update Contribution -  Status Code: {forgot_user_name_response.status_code}")

        assert forgot_user_name_response.status_code == 200, f"Unexpected status code: {forgot_user_name_response.status_code}"
        assert forgot_user_name_response_data.get(
            "isSuccess") is True, "isSuccess is not True in forgot username response"
        assert (forgot_user_name_response_data.get("message") ==
                "If the email address you entered is registered in this system, you will receive an email with your username shortly."), \
            f"Unexpected message in forgot username: {forgot_user_name_response_data.get('message')}"

        logging.info("Forgot username response appears successfully with 200 Status code.")

    except Exception as e:
        logging.error(f"Error in test_register: {e}")
        raise e


def test_login_admin():
    try:
        response = requests.post(dev_auth_url + dev_login_url, json=dev_login_admin_payload)
        response_data = response.json()
        logging.info(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Login successful.", \
            f"Unexpected message: {response_data.get('message')}"
        logging.info("Login successfully.")

    except Exception as e:
        logging.error(f"Error in test_login_admin: {e}")
        raise e


# Security Questions and Answer
def test_save_and_verify_security_questions_and_answers():
    try:
        user_data = register_user_from_admin()
        response_data = user_data.get("responseData", {})
        user_name = response_data.get("userName")
        authorization_token = user_data.get("token")

        # Save Security Questions
        save_security_payload = post_save_security_question_payload.copy()
        save_security_payload["userName"] = user_name

        save_questions_response = requests.post(
            dev_auth_url + save_security_question_info,
            headers={'Authorization': authorization_token, "Content-Type": "application/json"},
            data=json.dumps(save_security_payload)
        )
        save_questions_response_data = save_questions_response.json()

        logging.info(f"Save Security Questions Response: {save_questions_response_data}")
        assert save_questions_response.status_code == 200, "Failed to save security questions"
        assert save_questions_response_data.get("isSuccess"), "Saving security questions unsuccessful"
        assert save_questions_response_data.get("message") == "User security questions are saved successfully.", \
            f"Unexpected message: {save_questions_response_data.get('message')}"

        logging.info("Security questions saved successfully.")

        #     Verify User Question And Answer

        verify_security_qa_payload = post_verify_user_question_answer_payload.copy()
        verify_security_qa_payload["userName"] = user_name

        verify_security_qa_response = requests.post(
            dev_auth_url + verify_user_question_and_answer,
            headers={'Authorization': authorization_token, "Content-Type": "application/json"},
            data=json.dumps(verify_security_qa_payload)
        )
        verify_security_qa_response_data = verify_security_qa_response.json()
        logging.info(f"Verify Security Questions Response: {save_questions_response_data}")
        assert verify_security_qa_response.status_code == 200, "Failed to save security questions"
        assert verify_security_qa_response_data.get("isSuccess"), "Verifying security questions unsuccessful"
        assert (verify_security_qa_response_data.get("message") ==
                "We have sent you an email with a Reset Password link."), \
            f"Unexpected message: {verify_security_qa_response_data.get('message')}"

        logging.info("Security questions saved successfully.")
    except Exception as e:
        logging.error(f"Error in test_save_and_verify_security_questions_and_answers: {e}")
        raise e


def test_get_all_security_questions():
    try:
        authorization_token = get_admin_token()

        response = requests.get(
            dev_auth_url + get_all_security_questions,
            headers={'Authorization': authorization_token, "Content-Type": "application/json"},
            data={}
        )
        get_questions_response_data = response.json()

        logging.info(f"Save Security Questions Response: {get_questions_response_data}")
        assert response.status_code == 200, "Failed to fetch security questions"
        assert get_questions_response_data.get("isSuccess"), "Not Fetched  All security questions"

        logging.info("All Security questions fetched successfully.")

    except Exception as e:
        logging.error(f"Error in test_get_all_security_questions: {e}")
        raise e


# Committee User Profile
def test_get_pending_committee_access_requests_and_update_committee_access_status():
    try:
        authorization_token = get_committee_token()
        payload = get_pending_committee_access_requests_payload.copy()
        payload["pageNumber"] = 1
        payload["pageSize"] = 10

        response = requests.post(dev_auth_url + get_pending_committee_access_requests,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        response_data = response.json()
        logging.info(response_data)

        logging.info(f"Get Pending Committee Access Requests Status Code: {response.status_code}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, f"isSuccess is not True"
        logging.info(f"Pending Committee Access Requests Total Records:"
                     f" {response_data.get("responseData", {}).get("totalRecords")}")
        logging.info("Pending Committee Access Requests response appears successfully with 200 Status code.")

        # Access first id in responseData → data
        data_list = response_data.get("responseData", {}).get("data", [])
        first_id = data_list[0].get("id")
        logging.info(f"First ID: {first_id}")

        #  Update Committee Access Status
        logging.info('-------- Update Committee Access Status --------')
        payload_update_access_status = update_committee_access_status_payload.copy()
        payload_update_access_status["id"] = int(first_id)
        payload_update_access_status["accessStatus"] = "Approve"

        response_for_update_access_status = requests.post(dev_auth_url + update_committee_access_status,
                                                          headers={'Authorization': authorization_token,
                                                                   'Content-Type': 'application/json'},
                                                          data=json.dumps(payload_update_access_status))
        update_access_status_response_data = response_for_update_access_status.json()
        logging.info(update_access_status_response_data)

        logging.info(f"Update Committee Access Status [Status Code: {response_for_update_access_status.status_code}]")

        assert response_for_update_access_status.status_code == 200, \
            f"Unexpected status code: {response_for_update_access_status.status_code}"
        assert update_access_status_response_data.get("isSuccess") is True, f"isSuccess is not True"
        assert update_access_status_response_data.get("message") == "User access status updated successfully.", \
            f"Unexpected message: {update_access_status_response_data.get('message')}"

        logging.info("User access status updated successfully")

    except Exception as e:
        logging.error(f"Error in test_get_pending_committee_access_requests_and_update_committee_access_status: {e}")
        raise e


# Committee Users
def test_get_my_committee_users_data_list_and_get_my_committee_invite_users_data_list():
    try:
        authorization_token = get_committee_token()

        payload = get_my_committee_users_data_list_payload.copy()
        payload["pageNumber"] = 1
        payload["pageSize"] = 10
        payload["orgId"] = 1
        response_get_user_list = requests.post(dev_auth_url + get_my_committee_users_data_list,
                                               headers={'Authorization': authorization_token,
                                                        'Content-Type': 'application/json'},
                                               data=json.dumps(payload))
        response_data_get = response_get_user_list.json()
        logging.info(response_data_get)

        logging.info(f"Get My Committee User Data List  Status Code: {response_get_user_list.status_code}")

        assert response_get_user_list.status_code == 200, f"Unexpected status code: {response_get_user_list.status_code}"
        assert response_data_get.get("isSuccess") is True, f"isSuccess is not True"
        logging.info(f"Committee User Data List Total Records:"
                     f" {response_data_get.get("responseData", {}).get("totalRecords")}")
        logging.info("Pending Committee Access Requests response appears successfully with 200 Status code.")

        #   Get My Committee Invite Users Data List
        logging.info('------ Get My Committee Invite Users Data List ------ ')
        payload = get_my_committee_invite_user_data_list_payload.copy()
        payload["pageNumber"] = 1
        payload["pageSize"] = 10

        response_get_invite_user_list = requests.post(dev_auth_url + get_my_committee_invite_users_data_list,
                                                      headers={'Authorization': authorization_token,
                                                               'Content-Type': 'application/json'},
                                                      data=json.dumps(payload))
        response_invite_user_data = response_get_invite_user_list.json()
        logging.info(response_invite_user_data)

        logging.info(f"Committee Invite Users Data List  Status Code: {response_get_invite_user_list.status_code}")

        assert response_get_invite_user_list.status_code == 200, (f"Unexpected status code: "
                                                                  f"{response_get_invite_user_list.status_code}")
        assert response_invite_user_data.get("isSuccess") is True, f"isSuccess is not True"
        logging.info(f"Committee Invite Users Data List Total Records:"
                     f" {response_invite_user_data.get("responseData", {}).get("totalRecords")}")
        logging.info("Committee Invite Users Data List response appears successfully with 200 Status code.")

    except Exception as e:
        logging.error(f"Error in test_get_my_committee_users_data_list_and_get_my_committee_invite_users_data_list: {e}")
        raise e


# User Access
def test_get_user_registration_count():
    try:
        authorization_token = get_committee_token()

        response = requests.get(dev_auth_url + get_user_registration_count, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        logging.info(f"Total approve count:"
                     f" {response_data.get("responseData", {}).get("approveCount")}")
        logging.info(f"Total pending count:"
                     f" {response_data.get("responseData", {}).get("pendingCount")}")

        logging.info("User registration count fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_get_user_registration_count: {e}")
        raise e


# My Profile Messages
def test_get_my_profile_notifications():
    try:
        authorization_token = get_committee_token()

        response = requests.get(dev_auth_url + get_my_profile_notifications, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"

        for notification in response_data.get("responseData", []):
            logging.info(f"Title: {notification.get('title')}")
            logging.info(f"Description: {notification.get('description')}")
            logging.info(f"Post Date: {notification.get('postDate')}")

        logging.info("Profile Notification fetched successfully with correct response.")

    except Exception as e:
        logging.error(f"Error in test_get_my_profile_notifications: {e}")
        raise e


# My Profile
def test_get_profile_details_by_userid_user_question_info_update_security_questions():
    try:
        authorization_token = get_committee_token()

        response = requests.get(dev_auth_url + get_profile_details_by_userid, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"

        user_profile = response_data.get("responseData", {}).get("userProfile", {})

        for key, value in user_profile.items():
            logging.info(f"{key}: {value}")

        logging.info("Profile Details fetched successfully with correct response.")

        # Get User Question Info
        logging.info('------ Get User Question Info ------')
        response = requests.get(dev_auth_url + get_user_question_info, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data={})

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"

        security_questions = response_data.get("responseData", [])
        for item in security_questions:
            logging.info(f"Question: {item['question']}")
            logging.info(f"Answer: {item['answer']}")

        logging.info("User Question Info fetched successfully with correct response.")
    #     Update User Question & Answer Info
        logging.info('------ Update User Question & Answer Info ------')
        payload = update_question_answer_info_payload.copy()
        payload["updateQuestionAnswerInfo"][0]["sid"] = 1003
        payload["updateQuestionAnswerInfo"][0]["qid"] = 1000
        payload["updateQuestionAnswerInfo"][0]["answer"] = "1"

        response = requests.post(dev_auth_url + update_question_answer_info,
                                 headers={'Authorization': authorization_token,'Content-Type': 'application/json'},
                                 data=json.dumps(payload))

        update_response_data = response.json()
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert update_response_data.get("responseData") == "Security questions updated successfully.", \
            f"Unexpected message: {update_response_data.get("message")}"
        logging.info('Security questions updated successfully.')

    except Exception as e:
        logging.error(f"Error in test_get_profile_details_by_userid_user_question_info_update_security_questions: {e}")
        raise e


def test_update_user_profile_and_profile_password():
    try:
        authorization_token = get_admin_token()
    #     Update user profile
        logging.info('------ Update user profile ------')

        random_number = generate_random_mobile_number()
        logging.info(random_number)

        payload = update_user_profile_payload.copy()
        payload["email"] = "cfrs-noreply@tgstechnology.com"
        payload["contactNumber"] = str(random_number)

        response = requests.post(dev_auth_url + update_user_profile,
                                 headers={'Authorization': authorization_token,'Content-Type': 'application/json'},
                                 data=json.dumps(payload))

        update_response_data = response.json()
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert update_response_data.get("message") == "User profile updated successfully.", \
            f"Unexpected message: {update_response_data.get("message")}"
        logging.info('User profile updated successfully.')

    #    Update profile password
        logging.info('------ Update profile password ------')

        payload = update_profile_password_payload.copy()
        payload["password"] = ""
        payload["oldPassword"] = ""
        payload["newPassword"] = ""

        response = requests.post(dev_auth_url + update_profile_password,
                                 headers={'Authorization': authorization_token, 'Content-Type': 'application/json'},
                                 data=json.dumps(payload))

        update_response_data = response.json()
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert update_response_data.get("message") == "", \
            f"Unexpected message: {update_response_data.get("message")}"
        logging.info('User profile password successfully.')

    except Exception as e:
        logging.error(f"Error in test_update_user_profile_and_profile_password: {e}")
        raise e
