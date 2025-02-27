import json
from randomfunctions import *
#
state_cfs_admin = "STA"
system_cfs_administrator = "ASU"
Approve = "Approve"
Remove = "Remove"

admin_module = "CFA/"
public_module = "CFP/"
registrant_module = "CFR/"

new_registration_screen = "New%20Registration"
dashboard_screen = "Dashboard"

Accept_Conditionally = 'CNDA'
Reject = 'RJCT'

# orgId": 48
# qid": "1000
# ["orgId"] = str(406)
# payload["orgId"] = "1"
# orgId": 408

# ---------- usernames & passwords -------
DEV_ADMIN_USERNAME = "ETHAdmin"
DEV_ADMIN_PASSWORD = "Tgs@1234"

QA_ADMIN_USERNAME = "ETHAdmin"
QA_ADMIN_PASSWORD = "Tgs@1234"

DEV_COMMITTEE_USERNAME = "TGSOrg"
DEV_COMMITTEE_PASSWORD = "Tgs@12345"

# ---------- payloads -------

dev_login_committee_payload = {
    "userName": DEV_COMMITTEE_USERNAME,
    "password": DEV_COMMITTEE_PASSWORD
}

dev_login_admin_payload = {
    "userName": DEV_ADMIN_USERNAME,
    "password": DEV_ADMIN_PASSWORD,
    "systemTypeCode": "CFS"
}

test_login_committee_payload = {
    "userName": "vpatel",
    "password": "Vikas@123"
}

# transactions
add_Contribution_payload = json.dumps({
    "orgID": 291,
    "orgVersID": 1,
    "orgRegistrationID": 0,
    "transactionCategoryCode": "IKD",
    "entityTypeCode": "CA",
    "transactionAmount": 100,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "electionTypeCode": "G",
    "contributorPayeeID": 175,
    "transactionTypeCode": "CON",
    "contributorPayeeVersionID": 1,
    "isFundraiser": False,
    "eventID": 0
})

update_Contribution_payload = json.dumps({
    "orgID": 291,
    "orgVersID": 1,
    "orgRegistrationID": 0,
    "transactionCategoryCode": "IKD",
    "entityTypeCode": "CA",
    "transactionAmount": 2612,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "electionTypeCode": "P",
    "contributorPayeeID": 175,
    "transactionTypeCode": "CON",
    "contributorPayeeVersionID": 1,
    "isFundraiser": False,
    "eventID": 0

})

return_Contribution_payload = json.dumps({
    "transactionVersionID": 1,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "transactionAmount": 100
})

add_expenditure_payload = json.dumps({
    "orgID": 291,
    "orgVersID": 1,
    "orgRegistrationID": 0,
    "entityTypeCode": "CA",
    "transactionPurpose": "Adv",
    "transactionTypeCode": "EXP",
    "transactionCategoryCode": "MOI",
    "transactionAmount": 100,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "contributorPayeeID": 162,
    "contributorPayeeVersionID": 1,
    "isFundraiser": False,
    "eventID": 0
})

update_expenditure_payload = json.dumps({
    "orgID": 291,
    "orgVersID": 1,
    "orgRegistrationID": 0,
    "entityTypeCode": "CA",
    "transactionPurpose": "Adv",
    "transactionTypeCode": "EXP",
    "transactionCategoryCode": "MOI",
    "transactionAmount": 150,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "contributorPayeeID": 162,
    "contributorPayeeVersionID": 1,
    "isFundraiser": False,
    "eventID": 0,
})

return_expenditure_payload = json.dumps({
    "transactionVersionID": 1,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "transactionAmount": 5
})

add_worker_payload = json.dumps({
    "orgId": 146,
    "orgVersID": 2,
    "orgRegistrationID": 0,
    "transactionAmount": 100,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "contributorPayeeID": 199,
    "contributorPayeeVersionID": 1,
    "transactionTypeCode": "PW"
})

update_worker_payload = json.dumps({
    "contributorPayeeID": 199,
    "contributorPayeeVersionID": 1,
    "orgId": 146,
    "orgVersID": 2,
    "transactionAmount": 220,
    "transactionDate": "2024-11-30T18:30:00.000Z",
    "transactionTypeCode": "PW"
})

add_loan_payload = json.dumps({
    "orgId": 24,
    "orgVersID": 1,
    "entityTypeCode": "SE",
    "transactionAmount": 20,
    "transactionDate": "2024-12-02T18:30:00.000Z",
    "transactionTypeCode": "LOAN"
})

update_loan_payload = json.dumps({
    "orgId": 24,
    "orgVersID": 1,
    "entityTypeCode": "SE",
    "transactionAmount": 25,
    "transactionDate": "2024-12-01T13:00:00.000Z",
    "contributorPayeeID": 179,
    "contributorPayeeVersionID": 1,
    "transactionTypeCode": "LOAN"
})

payment_to_loan_payload = json.dumps({
    "transactionVersionID": 1,
    "transactionDate": "2024-12-24",
    "transactionAmount": 1
})

add_debt_payload = json.dumps({
    "orgId": 24,
    "orgVersID": 1,
    "entityTypeCode": "IND",
    "transactionAmount": 1000,
    "transactionDate": "2024-12-02T18:30:00.000Z",
    "contributorPayeeID": 37,
    "contributorPayeeVersionID": 1,
    "transactionTypeCode": "DEB",
    "transactionPurpose": "DTL"

})

update_debt_payload = json.dumps({
    "orgId": 24,
    "orgVersID": 1,
    "entityTypeCode": "IND",
    "transactionAmount": 500,
    "transactionDate": "2024-12-02T18:30:00.000Z",
    "contributorPayeeID": 37,
    "transactionTypeCode": "DEB",
    "transactionPurpose": "DTL",
})

debt_payment_payload = json.dumps({
    "transactionVersionID": 1,
    "transactionDate": "2024-12-02T18:30:00.000Z",
    "transactionAmount": 100
})

get_all_transactions_payload = json.dumps({
    "pageNumber": 1,
    "pageSize": 10,
    "transactionCategory": "",
    "contributorPayeeName": "",
    "orgID": 179,
    "sortColumn": "",
    "sortDirection": "desc"
})

post_random_candidate_registration_payload = json.dumps({
    "organization": {
        "orgTypeCode": "101",
        "orgSubtypeCode": "CNDT",
        "orgName": generate_random_organization_name(),
        "isJointFundrisingOrg": True,
        "primaryPhone": generate_random_mobile_number(),
        "alternatePhone": generate_random_mobile_number(),
        "email": generate_random_email(),
        "alternateEmail1": generate_random_email(),
        "website": generate_random_website(),
        "affiliation": "",
        "filerType": "",
        "filerPlaceofBussiness": "",
        "orgStatusCode": "ACTV",
        "isCandidateAsATresurer": True
    },
    "orgRegistration": {
        "electionID": 1000,
        "officeID": 233,
        "districtID": 0,
        "partyCode": "ACT"
    },
    "residentialAddress": {
        "addressLine1": generate_random_address_line_1(),
        "addressLine2": "",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "1",
        "countryCode": "USA",
        "zipCode": generate_random_zipcode(),
        "zipExt": "8282"
    },
    "mailingAddress": {
        "addressLine1": generate_random_address_line_1(),
        "addressLine2": "",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "1",
        "countryCode": "USA",
        "zipCode": generate_random_zipcode(),
        "zipExt": "8282"
    },
    "person": {
        "prefixCode": "104",
        "firstName": generate_first_name(),
        "middleName": generate_middle_name(),
        "lastName": generate_last_name(),
        "suffixCode": "103"
    },
    "officerModelList": [
        {
            "mailingAddress": {
                "addressLine1": generate_random_address_line_1(),
                "addressLine2": "",
                "city": "Charleston",
                "stateCode": "WV",
                "countyCode": "",
                "countryCode": "USA",
                "zipCode": generate_random_zipcode(),
                "zipExt": "8282"
            },
            "person": {
                "prefixCode": "104",
                "firstName": generate_first_name(),
                "middleName": generate_middle_name(),
                "lastName": generate_last_name(),
                "suffixCode": "103",
                "primaryPhone": generate_random_mobile_number(),
                "alternatePhone": generate_random_mobile_number(),
                "email": generate_random_email()
            },
            "orgOfficer": {
                "officerTypeCode": "TRE"
            }
        }
    ]
})

correct_registration_payload = {
  "orgDetails": {
    "orgID": "",
    "orgVersID": 1,
    "orgTypeCode": "101",
    "orgSubtypeCode": "CNDT",
    "orgName": generate_random_organization_name(),
    "isJointFundrisingOrg": True,
    "affiliation": "",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "registrationID": 7520,
    "electionID": 1000,
    "officeID": 233,
    "districtID": 0,
    "partyCode": "ACT",
    "orgAddressID": 0,
    "mailingAddressID": 0,
    "primaryPhone": "7625305591",
    "alternatePhone": "9125810723",
    "website": "https://mmknvix.io",
    "email": "ehzgi3FF@ymail.com",
    "alternateEmail1": "mp83VG@ymail.com",
    "orgAddressLine1": "",
    "orgAddressLine2": "",
    "orgCity": "",
    "orgStateCode": "",
    "OrgZipCode": "",
    "OrgZipExt": "",
    "orgCountyCode": "1",
    "orgCountryCode": "USA",
    "isCandidateAsATresurer": True
  },
  "officersDetails": [
    {
      "officerTypeCode": "CAN",
      "isMailingAddressUpdated": True,
      "isRecordUpdated": True,
      "IsPersonUpdated": True,
      "orgOfficerID": 8167,
      "personID": 872,
      "personVersionID": 1,
      "addressID": 8449,
      "prefixCode": "104",
      "firstName": "Otgwkt",
      "middleName": "B",
      "lastName": "Dvheog",
      "suffixCode": "103",
      "primaryPhone": "",
      "alternatePhone": "",
      "email": "",
      "addressLine1": "8108 Oak Street",
      "addressLine2": "",
      "city": "Charleston",
      "stateCode": "WV",
      "countyCode": "1",
      "zipCode": "23709",
      "zipExt": "8282",
      "countryCode": "USA",
      "statusCode": "ACTV",
      "mailingAddressID": 8450,
      "mailingAddressLine1": "4135 Oak Street",
      "mailingAddressLine2": "23",
      "mailingCity": "Charleston",
      "mailingStateCode": "WV",
      "mailingCountyCode": "1",
      "mailingZipCode": "75814",
      "mailingZipExt": "8282",
      "mailingCountryCode": "USA"
    },
    {
      "orgOfficerID": 8168,
      "officerTypeCode": "TRE",
      "personID": 873,
      "personVersionID": 1,
      "isMailingAddressUpdated": False,
      "isRecordUpdated": False,
      "IsPersonUpdated": False,
      "prefixCode": "104",
      "firstName": "Qrcixx",
      "middleName": "J",
      "lastName": "Yutbfe",
      "suffixCode": "103",
      "primaryPhone": "8628274347",
      "alternatePhone": "8046633389",
      "email": "ZSCueo4r@ymail.com",
      "addressID": 0,
      "addressLine1": "",
      "addressLine2": "",
      "city": "Charleston",
      "stateCode": "",
      "countyCode": "",
      "zipCode": "45284-8282",
      "zipExt": "",
      "countryCode": "",
      "mailingAddressID": 8451,
      "mailingAddressLine1": "5238 Walnut Street",
      "mailingAddressLine2": "",
      "mailingCity": "Charleston",
      "mailingStateCode": "WV",
      "mailingCountyCode": "",
      "mailingZipCode": "45284",
      "mailingZipExt": "8282",
      "mailingCountryCode": "USA",
      "statusCode": "ACTV"
    }
  ],
  "isOrgAddressUpdated": False,
  "isCandidateAddressUpdated": False,
  "IsCorrectRegistration": True
}

# Registrations
post_candidate_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "101",
    "orgSubtypeCode": "CNDT",
    "orgName": "Rabon Dauke",
    "isJointFundrisingOrg": True,
    "primaryPhone": "2356986569",
    "alternatePhone": "0709601330",
    "email": "johnsmith@yomail.com",
    "alternateEmail1": "johnsmith12@yomail.com",
    "website": "www.rsppcccc.com",
    "affiliation": "",
    "filerType": "",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": True
  },
  "orgRegistration": {
    "electionID": 1000,
    "officeID": 233,
    "districtID": 0,
    "partyCode": "ACT"
  },
  "residentialAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "1",
    "countryCode": "USA",
    "zipCode": "52852",
    "zipExt": "8282"
  },
  "mailingAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "1",
    "countryCode": "USA",
    "zipCode": "52852",
    "zipExt": "8282"
  },
  "person": {
    "prefixCode": "104",
    "firstName": "Willam",
    "middleName": "B",
    "lastName": "erick",
    "suffixCode": "103"
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "52852",
        "zipExt": "8282"
      },
      "person": {
        "prefixCode": "104",
        "firstName": "Willam",
        "middleName": "B",
        "lastName": "erick",
        "suffixCode": "103",
        "primaryPhone": "",
        "alternatePhone": "",
        "email": ""
      },
      "orgOfficer": {
        "officerTypeCode": "TRE"
      }
    }
  ]
})

post_pre_candidate_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "101",
    "orgSubtypeCode": "PCND",
    "orgName": "john smith",
    "isJointFundrisingOrg": True,
    "primaryPhone": "2356986569",
    "alternatePhone": "0709601330",
    "email": "johnsmith@yomail.com",
    "alternateEmail1": "johnsmith12@yomail.com",
    "website": "www.rsppcccc.com",
    "affiliation": "",
    "filerType": "",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": True
  },
  "orgRegistration": {
    "electionID": 1000,
    "officeID": 233,
    "districtID": 0,
    "partyCode": "ACT"
  },
  "residentialAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "1",
    "countryCode": "USA",
    "zipCode": "52852",
    "zipExt": "8282"
  },
  "mailingAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "1",
    "countryCode": "USA",
    "zipCode": "52852",
    "zipExt": "8282"
  },
  "person": {
    "prefixCode": "104",
    "firstName": "Mrash",
    "middleName": "B",
    "lastName": "John",
    "suffixCode": "103"
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "52852",
        "zipExt": "8282"
      },
      "person": {
        "prefixCode": "104",
        "firstName": "Mrash",
        "middleName": "B",
        "lastName": "John",
        "suffixCode": "103",
        "primaryPhone": "",
        "alternatePhone": "",
        "email": ""
      },
      "orgOfficer": {
        "officerTypeCode": "TRE"
      }
    }
  ]
})

post_pac_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "102",
    "orgSubtypeCode": "",
    "orgName": "PAC Committee for API",
    "isJointFundrisingOrg": False,
    "primaryPhone": "6516516516",
    "alternatePhone": "5648161549",
    "email": "monarch@yopmail.com",
    "alternateEmail1": "mornac123@yopmail.cpm",
    "website": "www.monarch.com",
    "affiliation": "Monarch",
    "filerType": "",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": False
  },
  "orgRegistration": {
    "electionID": 0,
    "officeID": 0,
    "districtID": 0,
    "partyCode": ""
  },
  "residentialAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "mailingAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "Street Two",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "23569",
    "zipExt": ""
  },
  "person": {
    "prefixCode": "",
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "suffixCode": ""
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "Address Line 2",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "23569",
        "zipExt": ""
      },
      "person": {
        "prefixCode": "104",
        "firstName": "James",
        "middleName": "K",
        "lastName": "Anderson",
        "suffixCode": "103",
        "primaryPhone": "2356986569",
        "alternatePhone": "5454753855",
        "email": "James@yopmail.com"
      },
      "orgOfficer": {
        "officerTypeCode": "TRE"
      }
    }
  ]
})

post_ppc_ccc_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "103",
    "orgSubtypeCode": "",
    "orgName": "PPC committee for API",
    "isJointFundrisingOrg": False,
    "primaryPhone": "5984894832",
    "alternatePhone": "8819984498",
    "email": "ppacapi@yopmail.com",
    "alternateEmail1": "ppaccc@yomail.com",
    "website": "www.ppcgov.in",
    "affiliation": "",
    "filerType": "",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": False
  },
  "orgRegistration": {
    "electionID": 0,
    "officeID": 0,
    "districtID": 0,
    "partyCode": ""
  },
  "residentialAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "mailingAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "Street Two",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "23569",
    "zipExt": ""
  },
  "person": {
    "prefixCode": "",
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "suffixCode": ""
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "Street Two",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "23569",
        "zipExt": ""
      },
      "person": {
        "prefixCode": "105",
        "firstName": "Ward",
        "middleName": "F",
        "lastName": "Miller",
        "suffixCode": "105",
        "primaryPhone": "4573893893",
        "alternatePhone": "3456353893",
        "email": "smith@yopmail.com"
      },
      "orgOfficer": {
        "officerTypeCode": "CMO"
      }
    }
  ]
})

post_IEC_individual_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "104",
    "orgSubtypeCode": "IIDL",
    "orgName": "",
    "isJointFundrisingOrg": False,
    "primaryPhone": "5324537452",
    "alternatePhone": "2010424242",
    "email": "Mersica@yopmail.com",
    "alternateEmail1": "Mersica324@yopmail.com",
    "website": "www.Mersica.com",
    "affiliation": "",
    "filerType": "Individual",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": False
  },
  "orgRegistration": {
    "electionID": None,
    "officeID": None,
    "districtID": None,
    "partyCode": ""
  },
  "residentialAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "mailingAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "person": {
    "prefixCode": "102",
    "firstName": "Mersica",
    "middleName": "U",
    "lastName": "Lizaerf",
    "suffixCode": "101"
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "Street Two",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "23569",
        "zipExt": ""
      },
      "person": {
        "prefixCode": "105",
        "firstName": "Nick",
        "middleName": "D",
        "lastName": "Temple",
        "suffixCode": "",
        "primaryPhone": "4574254247",
        "alternatePhone": "2458854252",
        "email": "Nick@yopmail.com"
      },
      "orgOfficer": {
        "officerTypeCode": "CHP"
      }
    }
  ]
})

post_IEC_organization_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "104",
    "orgSubtypeCode": "IONZ",
    "orgName": "Neutron Research",
    "isJointFundrisingOrg": False,
    "primaryPhone": "1348637843",
    "alternatePhone": "3453883837",
    "email": "Neutronresearch@yopmail.com",
    "alternateEmail1": "research@yopmail.com",
    "website": "www.NeutronResearch.com",
    "affiliation": "",
    "filerType": "Organization",
    "filerPlaceofBussiness": "Research and Development",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": False
  },
  "orgRegistration": {
    "electionID": None,
    "officeID": None,
    "districtID": None,
    "partyCode": ""
  },
  "residentialAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "mailingAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "Street Two",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "23569",
    "zipExt": ""
  },
  "person": {
    "prefixCode": "",
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "suffixCode": ""
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "Street Two",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "23569",
        "zipExt": ""
      },
      "person": {
        "prefixCode": "105",
        "firstName": "George",
        "middleName": "S",
        "lastName": "Ward",
        "suffixCode": "107",
        "primaryPhone": "7684535345",
        "alternatePhone": "4535353599",
        "email": "George@yopmail.com"
      },
      "orgOfficer": {
        "officerTypeCode": "AUA"
      }
    }
  ]
})

post_ECC_individual_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "105",
    "orgSubtypeCode": "EIDL",
    "orgName": "",
    "isJointFundrisingOrg": False,
    "primaryPhone": "5165148441",
    "alternatePhone": "8121548151",
    "email": "honric@yopmail.com",
    "alternateEmail1": "honric123@yopmail.com",
    "website": "www.honric.com",
    "affiliation": "",
    "filerType": "Individual",
    "filerPlaceofBussiness": "",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": False
  },
  "orgRegistration": {
    "electionID": None,
    "officeID": None,
    "districtID": None,
    "partyCode": ""
  },
  "residentialAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "mailingAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "person": {
    "prefixCode": "101",
    "firstName": "Honric",
    "middleName": "H",
    "lastName": "Sam",
    "suffixCode": "107"
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "Street Two",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "23569",
        "zipExt": ""
      },
      "person": {
        "prefixCode": "102",
        "firstName": "Adam",
        "middleName": "Y",
        "lastName": "Villas",
        "suffixCode": "104",
        "primaryPhone": "2727827827",
        "alternatePhone": "2234211445",
        "email": "adam@yopmail.com"
      },
      "orgOfficer": {
        "officerTypeCode": "CMO"
      }
    }
  ]
})

post_ECC_organization_registration_payload = json.dumps({
  "organization": {
    "orgTypeCode": "105",
    "orgSubtypeCode": "EONZ",
    "orgName": "Berkshire Hathaway",
    "isJointFundrisingOrg": False,
    "primaryPhone": "4534534534",
    "alternatePhone": "1010424242",
    "email": "Berkshire@yopmail.com",
    "alternateEmail1": "Berkshire1123@yopmai.com",
    "website": "www.Hathaway.com",
    "affiliation": "",
    "filerType": "Organization",
    "filerPlaceofBussiness": "textile manufacturer",
    "orgStatusCode": "ACTV",
    "isCandidateAsATresurer": False
  },
  "orgRegistration": {
    "electionID": None,
    "officeID": None,
    "districtID": None,
    "partyCode": ""
  },
  "residentialAddress": {
    "addressLine1": "",
    "addressLine2": "",
    "city": "",
    "stateCode": "",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "",
    "zipExt": ""
  },
  "mailingAddress": {
    "addressLine1": "123 Main St",
    "addressLine2": "Street Two",
    "city": "Charleston",
    "stateCode": "WV",
    "countyCode": "",
    "countryCode": "USA",
    "zipCode": "23569",
    "zipExt": ""
  },
  "person": {
    "prefixCode": "",
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "suffixCode": ""
  },
  "officerModelList": [
    {
      "mailingAddress": {
        "addressLine1": "123 Main St",
        "addressLine2": "Street Two",
        "city": "Charleston",
        "stateCode": "WV",
        "countyCode": "",
        "countryCode": "USA",
        "zipCode": "23569",
        "zipExt": ""
      },
      "person": {
        "prefixCode": "103",
        "firstName": "Green",
        "middleName": "Y",
        "lastName": "Santovick",
        "suffixCode": "103",
        "primaryPhone": "6849848484",
        "alternatePhone": "6231654114",
        "email": "green@yopmail.com"
      },
      "orgOfficer": {
        "officerTypeCode": "CHP"
      }
    }
  ]
})

get_all_committee_transactions_payload = json.dumps({
  "pageNumber": 1,
  "searchKeyword": "",
  "pageSize": "1000",
  "sortColumn": "",
  "sortDirection": "",
  "entityId": "",
  "registrationType": "",
  "orgName": "",
  "orgType": "",
  "orgStatus": "",
  "candidateName": "",
  "treasurerName": "",
  "registrationDate": "",
  "isCommitteeSearch": False,
  "orgSubTypeCode": ""
})

get_all_officer_information_by_org_id_payload = {
  "orgId": "",
  "pageNumber": 1,
  "searchKeyword": "",
  "pageSize": 10,
  "sortColumn": "",
  "sortDirection": ""
}

edit_pending_org_registration_status_payload = {
    "orgStatusCode": "",
    "orgStatusReasonCode": "",
    "statusReasonComment": "",
    "orgId": ""
}
# ----------------- Auth -----------------

post_get_administrative_data_list_payload = {
  "pageNumber": "",
  "searchKeyword": "",
  "pageSize": "",
  "sortColumn": "",
  "sortDirection": "",
  "orgId": ""
}

post_add_administrative_notes_payload = json.dumps({
    "adminNotesCategoryID": 3,
    "adminNotes": "Please file the transactions.",
    "orgId": 48
})

# Payload for registering a user
post_register_user_payload = {
    "userName": "",
    "email": "",
    "contactNumber": "",
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "userAccountStatus": True,
    "isLocked": False
}

# Payload for saving security questions
post_save_security_question_payload = {
    "userName": "",
    "questionAnswerInfo": [
        {"qid": "1000", "answer": "1"},
        {"qid": "1002", "answer": "1"},
        {"qid": "1019", "answer": "1"}
    ]
}

post_verify_user_question_answer_payload = {
  "userName": "",
  "qid": "1002",
  "answer": "1"
}

post_forgot_username_payload = {
  "firstName": "",
  "lastName": "",
  "email": ""
}

# Committee User Profile

get_pending_committee_access_requests_payload = {
  "pageNumber": "",
  "searchKeyword": "",
  "pageSize": "",
  "sortColumn": "",
  "sortDirection": ""
}

update_committee_access_status_payload = {
  "id": "",
  "accessStatus": ""
}

# Committee Users

get_my_committee_users_data_list_payload = {
  "pageNumber": "",
  "searchKeyword": "",
  "pageSize": "",
  "sortColumn": "",
  "sortDirection": "",
  "orgId": "",
  "firstName": "",
  "lastName": "",
  "userRole": ""
}

get_my_committee_invite_user_data_list_payload = {
  "pageNumber": "",
  "searchKeyword": "",
  "pageSize": "",
  "sortColumn": "",
  "sortDirection": "",
  "firstName": "",
  "lastName": "",
  "userName": "",
  "email": ""
}

# My Profile
update_question_answer_info_payload = {
  "updateQuestionAnswerInfo": [
    {
      "sid": "",
      "qid": "",
      "answer": ""
    }
    ]
}

update_profile_password_payload = {
  "password": "",
  "oldPassword": "",
  "newPassword": ""
}

update_user_profile_payload = {
    "email": "",
    "contactNumber": ""
}

# Manage User

get_user_list_payload = {
    "pageNumber": 1,
    "pageSize": 10
}

force_user_to_change_on_next_login_payload = {
  "password": "",
  "oldPassword": "",
  "newPassword": ""
}

create_system_generated_password_payload = {
  "id": "",
  "password": "",
  "oldPassword": "",
  "newPassword": ""
}

create_new_password_payload = {
  "id": "",
  "password": "",
  "oldPassword": "",
  "newPassword": ""
}

add_user_access_payload = {
    "roleCode": "",
    "userId": ""
}

add_user_access_committee_payload = {
    "roleCode": "",
    "orgId": "",
    "userId": ""
}


update_user_access_status_payload = {
    "id": "",
    "accessStatus": ""
}

get_admin_role_by_user_data_list_payload = {
    "userId": "",
    "entityId": "",
    "orgName": "",
    "orgType": "",
    "orgAccessStatus": "",
    "userRole": "",
    "pageNumber": 1,
    "pageSize": 10
}

get_user_committee_access_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10
}

get_user_role_by_user_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10,
    "entityId": "",
    "orgName": "",
    "orgType": "",
    "orgAccessStatus": "",
    "userRole": "",
    "userId": "",
    "isAdmin": True
}

# My Committee

get_all_org_pending_registrations_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10
}

get_my_committee_list_payload = {
    "committeeType": "",
    "userRole": "",
    "entityId": "",
    "committeeName": ""
}

get_user_login_session_by_org_id_payload = {
    "orgId": "",
    "isAdmin": False,
    "pageNumber": 1,
    "searchKeyword": "",
    "pageSize": 10,
    "sortColumn": "",
    "sortDirection": ""
}

get_user_reporting_activity_by_org_id_payload = {
    "orgId": "",
    "isAdmin": False,
    "pageNumber": 1,
    "searchKeyword": "",
    "pageSize": 10,
    "sortColumn": "",
    "sortDirection": ""
}


# Notification
get_all_notification_payload = json.dumps({
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

add_edit_notification_payload = json.dumps({
    "id": 0,
    "title": "Hello ",
    "adminNotification": "this is description",
    "viewStatus": "abcd",
    "adminNotificationType": "abcd",
    "postDate": "2024-10-10",
    "viewMode": "abcd"
})

# correspondence
get_correspondence_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 387,
    "electionID": None,
    "reportingCycleID": None,
    "reportingDueDate": None,
    "reportingEndDate": None,
    "reportingPeriodID": None,
    "committeeName": None,
    "committeeStatus": None,
    "committeeType": None,
    "noticeType": None
}

get_org_info_for_correspondence_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 387,
    "electionID": None,
    "reportingCycleID": None,
    "reportingDueDate": None,
    "reportingEndDate": None,
    "reportingPeriodID": None,
    "committeeName": None,
    "committeeStatus": None,
    "committeeType": None,
    "noticeType": None
}

add_correspondence_payload = {
    "orgInfo": [
        {
            "orgID": 430
        },
        {
            "orgID": 429
        },
        {
            "orgID": 428
        }
    ],
    "noticeTypeCode": "GRN",
    "subject": "Due date for filing",
    "body": "<!DOCTYPE html>\n    <html lang=\"en\">\n    <head>\n      "
            "<meta charset=\"UTF-8\">\n      <meta name=\"viewport\" content=\"width=device-width, "
            "initial-scale=1.0\">\n      <title>Email</title>\n    </head>\n    <body>\n      "
            "<p>Due date for filing should not be accepted</p>\n    "
            "</body>\n    </html>",
    "scheduleDate": "2025-02-07"
}

get_org_filed_report_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10,
    "sortColumn": "",
    "sortDirection": "",
    "committeeName": "",
    "reportName": "",
    "filedBeginDate": None,
    "filedEndDate": None,
    "dueDateBeginDate": None,
    "dueDateEndDate": None,
    "reportStatus": ""
}

# Get All Org Documents Data List
get_all_org_documents_data_list_payload = {
    "orgID": "",
    "documentID": 0,
    "documentName": "",
    "committeeName": "",
    "documentType": "",
    "receivedDate": "",
    "documentPrivacy": "",
    "searchKeyword": "",
    "pageNumber": 1,
    "pageSize": 10,
    "sortColumn": "",
    "sortDirection": "",
    "privacyTypeCode": "AD,PR"
}


delete_document_payload = {
  "docId": ""
}

generate_administration_report_payload = {
    "reportType": "FLN",
    "reportSubType": "UFLD_RP",
    "reportFormat": "PDF",
    "reportRequest": {
        "DueBeginDate": "",
        "DueEndDate": ""
    }
}

# Audit Review
get_all_transaction_for_audit_review_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10
}

get_all_report_for_audit_review_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10,
    "filedEndDate": None,
    "filedStartDate": None,
    "complianceType": None,
    "entityID": "",
    "committeeName": "",
    "reportName": "",
    "committeeType": "",
    "violationStatus": "",
    "reportVersion": "",
    "complianceStatus": ""
}

add_edit_violation_payload = {
    "violationDate": "",
    "violationStatusCode": "",
    "violationAmount": "",
    "orgComplianceID": "",
    "orgID": ""
}

add_edit_violation_payment_payload = {
    "payerFirstName": generate_first_name(),
    "payerMiddleName": generate_middle_name(),
    "payerLastName": generate_last_name(),
    "paymentDate": "",
    "paymentTypeCode": "",
    "paymentAmount": "",
    "violationID": "",
    "orgComplianceID": "",
    "orgID": ""
}

edit_violation_payment_payload = {
    "payerFirstName": generate_first_name(),
    "payerMiddleName": generate_middle_name(),
    "payerLastName": generate_last_name(),
    "paymentDate": "",
    "paymentTypeCode": "",
    "paymentAmount": "",
    "paymentID": ""
}

get_all_violation_payment_data_list_payload = {
    "pageNumber": 1,
    "pageSize": 10,
    "violationID": ""
}

update_compliance_status_payload = {
    "complianceStatusCode": "OP",
    "orgComplianceIDs": [
        {
            "orgComplianceID": 1006
        }
    ]
}

add_edit_violation_waiver_payload = {
    "waiverDecisionTypeCode": "GT",
    "decisionDate": "2025-02-25",
    "hearingDate": "2025-02-25",
    "staffComment": "",
    "requestorComment": "",
    "requestDate": "2025-02-25",
    "requestorLastName": "Mangukia",
    "requestorMiddleName": "",
    "requestorFirstName": "Vikas",
    "waiverRequestTypeCode": "IL",
    "orgID": 3,
    "orgComplianceID": 1006
}
