# Open terminal and run this command "pytest TestCases "
#
# py.test - -html = report.html - s

import requests


url = "https://gorest.co.in/public-api/users"
resp = requests.get(url)


def testCase1_validate_response_code_positive():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    # assert response code
    assert json_response == 200, "code doesnt match"


def testCase2_validate_response_code_negative():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    # assert response code
    assert json_response is not None


def testCase3_validate_response_body_emailField():
    json_response = resp.json()
    print(json_response["data"][0]["email"])
    # assert the email
    assert (json_response["data"][0]["email"]) is not None, "email is null"


def testCase4_validate_response_body_name():
    json_response = resp.json()
    print(json_response["data"][1]["name"])
    # assert the name field
    assert json_response["data"][1]["name"] is not None, "name is null"


def testCase5_validate_response_body_pagination():
    json_response = resp.json()
    print(json_response["meta"]["pagination"]["pages"])
    assert json_response["meta"]["pagination"]["pages"] is not None, "Value is null"


def testCase6_validate_response_body_pagination_negative_scenario():
    json_response = resp.json()
    print(json_response["meta"]["pagination"]["pages"])
    assert json_response["meta"]["pagination"]["pages"] != 140, "Value is null"
