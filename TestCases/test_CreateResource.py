import requests

url = "https://gorest.co.in/public/v2/users"
payload = {"id": "4033", "name": "aabhi", "email": "anonybahi@test1.com", "gender": "fmale", "status": "active"}
headers = {"Authorization": "Bearer 8a5960423128689eaf2a5dc6eea7c5daa78aa5b746ff2f777916f9c295750df1"}
resp = requests.post(url, data=payload, headers=headers)


def testCase11_createResource_validate_statusCode_negative():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    assert json_response == 201, "Status code doesnt match"


def testCase12_createResource_validate_statusCode_negative():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    assert json_response is not None


def testCase13_createResource_validate_header():
    json_resp = resp.headers.get("content-Type")
    print(json_resp)
    assert json_resp is not None


def testCase14_createResource_validate_response_body_gender():
    print(resp.json())
    assert resp.json()['gender'] == 'female'
    print("Response body validation")


def testCase15_createResource_validate_response_body_id():
    print(resp.json())
    assert resp.json()['id'] is not None
    print("Response body validation")
