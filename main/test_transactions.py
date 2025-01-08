from utils import *
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_add_update_return_delete_contribution():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url + transactionUrl, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=add_Contribution_payload)
        logging.info(response)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        # logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Contribution added successfully.", \
            f"Unexpected message: {response_data.get('message')}"

        logging.info("Transaction added successfully with correct response.")

        add_transaction_id = response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Add Transaction ID: {add_transaction_id}")

    #     -update-
        logging.info("...............Update Contribution..................")
        update_payload = json.loads(update_Contribution_payload)
        update_payload["transactionId"] = add_transaction_id
        update_payload = json.dumps(update_payload)

        update_response = requests.post(dev_committee_url + update_transactions, headers={
                'Authorization': authorization_token,
                'Content-Type': 'application/json'
            }, data=update_payload)

        update_response_data = update_response.json()
        logging.info(f"Update Contribution -  Status Code: {update_response.status_code}")
        # logging.info(f"Update Contribution - Response Body: {update_response.text}")

        assert update_response.status_code == 200, f"Unexpected status code: {update_response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in Update Contribution response"
        assert update_response_data.get("message") == "Contribution updated successfully.", \
            f"Unexpected message in Update Contribution: {update_response_data.get('message')}"

        logging.info("Contribution updated successfully.")

        # update_transaction_id = update_response_data.get("responseData", {}).get("transactionID")
        # logging.info(f"Transaction ID: {update_transaction_id}")

    #    --return--
        logging.info("...............Return Contribution...............")
        return_payload = json.loads(return_Contribution_payload)
        return_payload["transactionId"] = add_transaction_id
        return_payload = json.dumps(return_payload)

        return_response = requests.post(dev_committee_url + return_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=return_payload)

        return_response_data = return_response.json()
        logging.info(f"Return Contribution -  Status Code: {return_response.status_code}")
        # logging.info(f"Update Contribution - Response Body: {return_response.text}")

        assert return_response.status_code == 200, f"Unexpected status code: {return_response.status_code}"
        assert return_response_data.get("isSuccess") is True, "isSuccess is not True in Update Contribution response"
        assert return_response_data.get("message") == "Return contribution added successfully.", \
            f"Unexpected message in return Contribution: {return_response_data.get('message')}"

        logging.info("Return updated successfully.")

        return_transaction_id = return_response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Return Transaction ID: {return_transaction_id}")

    #    --delete added--
        logging.info("............Delete added Contribution............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(add_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Contribution -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Contribution deleted successfully.", \
            f"Unexpected message in delete Contribution: {delete_response_data.get('message')}"
        logging.info("Added Contribution deleted successfully.")

    #    --delete return--
        logging.info("............Delete return Contribution...............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(return_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Return Delete Contribution -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Contribution deleted successfully.", \
            f"Unexpected message in delete Contribution: {delete_response_data.get('message')}"
        logging.info("Return Contribution deleted successfully.")

    except Exception as e:
        logging.error(f"Error in test_add_update_return_delete_contribution: {e}")
        raise e


def test_add_update_return_delete_expenditure():
    try:
        authorization_token = get_committee_token()

        response = requests.post(dev_committee_url + transactionUrl, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=add_expenditure_payload)

        response_data = response.json()

        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response_data.get("isSuccess") is True, "isSuccess is not True in response"
        assert response_data.get("message") == "Expenditure added successfully.", \
            f"Unexpected message: {response_data.get('message')}"
        add_transaction_id = response_data.get("responseData", {}).get("transactionID")

        logging.info(f"Add Transaction ID: {add_transaction_id}")
        logging.info("Expenditure added successfully with correct response.")

    #     -update-
        logging.info("...............Update Expenditure..................")
        update_payload = json.loads(update_expenditure_payload)
        update_payload["transactionId"] = add_transaction_id
        update_payload = json.dumps(update_payload)

        update_response = requests.post(dev_committee_url + update_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=update_payload)

        update_response_data = update_response.json()
        logging.info(f"Update Expenditure -  Status Code: {update_response.status_code}")
        # logging.info(f"Update Expenditure - Response Body: {update_response.text}")

        assert update_response.status_code == 200, f"Unexpected status code: {update_response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in Update Expenditure response"
        assert update_response_data.get("message") == "Expenditure updated successfully.", \
            f"Unexpected message in Update Expenditure: {update_response_data.get('message')}"

        logging.info("Expenditure updated successfully.")

#    --return--
        logging.info("...............Return Expenditure...............")
        return_payload = json.loads(return_expenditure_payload)
        return_payload["transactionId"] = add_transaction_id
        return_payload = json.dumps(return_payload)

        return_response = requests.post(dev_committee_url + return_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=return_payload)

        return_response_data = return_response.json()
        logging.info(f"Return Expenditure -  Status Code: {return_response.status_code}")
        # logging.info(f"Update Expenditure - Response Body: {return_response.text}")

        assert return_response.status_code == 200, f"Unexpected status code: {return_response.status_code}"
        assert return_response_data.get("isSuccess") is True, "isSuccess is not True in Return Expenditure response"
        assert return_response_data.get("message") == "Return expenditure added successfully.", \
            f"Unexpected message in Update Expenditure: {return_response_data.get('message')}"

        logging.info("Return updated successfully.")

        return_transaction_id = return_response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Return Transaction ID: {return_transaction_id}")

    #    --delete added--
        logging.info("............Delete added Expenditure............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(add_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Expenditure -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Expenditure deleted successfully.", \
            f"Unexpected message in Update Expenditure: {delete_response_data.get('message')}"
        logging.info("Added Expenditure deleted successfully.")

    #    --delete return--
        logging.info("............Delete return Expenditure...............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(return_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Contribution -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Expenditure deleted successfully.", \
            f"Unexpected message in Update Expenditure: {delete_response_data.get('message')}"
        logging.info("Return Expenditure deleted successfully.")

    except Exception as e:
        logging.error(f"Error in test_add_expenditure: {e}")
        raise e


def test_add_add_update_delete_worker():
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

        add_transaction_id = response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Add Transaction ID: {add_transaction_id}")

        #     -update-
        logging.info("...............Update Payment to worker transaction..................")
        update_payload = json.loads(update_worker_payload)
        update_payload["transactionId"] = add_transaction_id
        update_payload = json.dumps(update_payload)

        update_response = requests.post(dev_committee_url + update_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=update_payload)

        update_response_data = update_response.json()
        logging.info(f"Update Contribution -  Status Code: {update_response.status_code}")
        # logging.info(f"Update Contribution - Response Body: {update_response.text}")

        assert update_response.status_code == 200, f"Unexpected status code: {update_response.status_code}"
        assert update_response_data.get("isSuccess") is True, ("isSuccess is not True in Update Payment to worker "
                                                               "response")
        assert update_response_data.get("message") == "Payment to Worker updated successfully.", \
            f"Unexpected message in Update Payment to worker: {update_response_data.get('message')}"

        logging.info("Payment to worker transaction updated successfully.")

        #    --delete return--
        logging.info("............Delete Payment to worker transaction...............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(add_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Payment to worker transaction -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Payment to Worker deleted successfully.", \
            f"Unexpected message in delete Payment: {delete_response_data.get('message')}"
        logging.info("Payment to worker transaction deleted successfully.")

    except Exception as e:
        logging.error(f"Error in test_add_worker: {e}")
        raise e


def test_add_update_payment_delete_loan():
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

        # -update -
        logging.info("...............Update Loan..................")
        update_payload = json.loads(update_loan_payload)
        update_payload["transactionId"] = transaction_id
        update_payload = json.dumps(update_payload)

        update_response = requests.post(dev_committee_url + update_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=update_payload)

        update_response_data = update_response.json()
        logging.info(f"Update Loan -  Status Code: {update_response.status_code}")
        # logging.info(f"Update Loan - Response Body: {update_response.text}")

        assert update_response.status_code == 200, f"Unexpected status code: {update_response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in Update Loan response"
        assert update_response_data.get("message") == "Loan updated successfully.", \
            f"Unexpected message in Update Loan: {update_response_data.get('message')}"

        logging.info("Loan updated successfully.")

        #  --payment--
        logging.info("...............Payment Loan...............")
        return_payload = json.loads(payment_to_loan_payload)
        return_payload["transactionId"] = transaction_id
        return_payload = json.dumps(return_payload)

        return_response = requests.post(dev_committee_url + return_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=return_payload)

        return_response_data = return_response.json()
        logging.info(f"Loan payment -  Status Code: {return_response.status_code}")
        # logging.info(f"Loan payment - Response Body: {return_response.text}")

        assert return_response.status_code == 200, f"Unexpected status code: {return_response.status_code}"
        assert return_response_data.get("isSuccess") is True, "isSuccess is not True in Loan payment response"
        assert return_response_data.get("message") == "Loan payment added successfully.", \
            f"Unexpected message in Update Expenditure: {return_response_data.get('message')}"

        logging.info("Loan payment added successfully.")

        return_transaction_id = return_response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Loan payment Transaction ID: {return_transaction_id}")

        #    --delete added--
        logging.info("............Delete added ............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Expenditure -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Loan deleted successfully.", \
            f"Unexpected message in Loan delete: {delete_response_data.get('message')}"
        logging.info("Added Loan deleted successfully.")

        #    --delete payment--
        logging.info("............Delete payment Loan...............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(return_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Loan -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Loan deleted successfully.", \
            f"Unexpected message in Loan payment delete: {delete_response_data.get('message')}"
        logging.info("Loan payment deleted successfully.")

    except Exception as e:
        logging.error(f"Error in test_add_update_payment_delete_loan: {e}")
        raise e


def test_add_update_payment_delete_debt():
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

        transaction_id = response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Transaction ID: {transaction_id}")

        logging.info("Loan added successfully with correct response.")

        # -update -
        logging.info("...............Update Debt..................")
        update_payload = json.loads(update_debt_payload)
        update_payload["transactionId"] = transaction_id
        update_payload = json.dumps(update_payload)

        update_response = requests.post(dev_committee_url + update_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=update_payload)

        update_response_data = update_response.json()
        logging.info(f"Update Debt -  Status Code: {update_response.status_code}")
        # logging.info(f"Update Debt - Response Body: {update_response.text}")

        assert update_response.status_code == 200, f"Unexpected status code: {update_response.status_code}"
        assert update_response_data.get("isSuccess") is True, "isSuccess is not True in Update Debt response"
        assert update_response_data.get("message") == "Debt updated successfully.", \
            f"Unexpected message in Update Debt: {update_response_data.get('message')}"

        logging.info("Debt updated successfully.")

        #  --payment--
        logging.info("...............Debt Payment...............")
        return_payload = json.loads(debt_payment_payload)
        return_payload["transactionId"] = transaction_id
        return_payload = json.dumps(return_payload)

        return_response = requests.post(dev_committee_url + return_transactions, headers={
            'Authorization': authorization_token,
            'Content-Type': 'application/json'
        }, data=return_payload)

        return_response_data = return_response.json()
        logging.info(f"Debt payment -  Status Code: {return_response.status_code}")
        # logging.info(f"Debt payment - Response Body: {return_response.text}")

        assert return_response.status_code == 200, f"Unexpected status code: {return_response.status_code}"
        assert return_response_data.get("isSuccess") is True, "isSuccess is not True in Debt payment response"
        assert return_response_data.get("message") == "Debt payment added successfully.", \
            f"Unexpected message in Debt payment: {return_response_data.get('message')}"

        logging.info("Loan payment added successfully.")

        return_transaction_id = return_response_data.get("responseData", {}).get("transactionID")
        logging.info(f"Debt payment Transaction ID: {return_transaction_id}")

        #    --delete added--
        logging.info("............Delete added ............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Expenditure -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Debt deleted successfully.", \
            f"Unexpected message in Debt delete: {delete_response_data.get('message')}"
        logging.info("Added Debt deleted successfully.")

        #    --delete payment--
        logging.info("............Delete Debt Payment...............")
        delete_response = requests.post(dev_committee_url + delete_transactions + str(return_transaction_id),
                                        headers={'Authorization': authorization_token}, data={})
        delete_response_data = delete_response.json()
        logging.info(f"Delete Debt -  Status Code: {delete_response.status_code}")
        assert delete_response.status_code == 200, f"Unexpected status code: {delete_response.status_code}"
        assert delete_response_data.get("message") == "Debt deleted successfully.", \
            f"Unexpected message in Debt payment delete: {delete_response_data.get('message')}"
        logging.info("Debt payment deleted successfully.")

    except Exception as e:
        logging.error(f"Error in test_add_update_payment_delete_debt: {e}")
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
