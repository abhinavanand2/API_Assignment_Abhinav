import requests

url = "https://gorest.co.in/public/v2/posts"
resp = requests.get(url)


def testCase7_validate_response_code_positive():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    # assert response code
    assert json_response == 200, "code doesnt match"


def testCase8_validate_response_code_negative():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    # assert response code
    assert json_response is not None


def testCase9_validate_response_body_userId():
    json_response = resp.json()
    print(json_response[1]["user_id"])
    # assert the user id
    assert (json_response[1]["user_id"]) != 3079, "user id is null"


def testCase10_validate_response_body_Id():
    json_response = resp.json()
    print(json_response[1]["id"])
    # assert the user id
    assert (json_response[2]["id"]) != 1466, "user id is null"


