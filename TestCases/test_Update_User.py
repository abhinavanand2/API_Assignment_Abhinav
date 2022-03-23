import requests

url = "https://gorest.co.in/public/v2/users/1477"
headers = {"Authorization": "Bearer 8a5960423128689eaf2a5dc6eea7c5daa78aa5b746ff2f777916f9c295750df1"}
payload = {"id": 1544, "post_id": 1477, "name": "Adripathi Panicker PhD",
           "email": "adripathi_phd_panicker@schoen-lockman.info",
           "body": "Quas excepturi tempora. Est iusto et. Nulla quos possimus."}

resp = requests.put(url, data=payload, headers=headers)


def testCase16_updateResource_validate_statusCode():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    assert json_response == 200, "Status code doesnt match"


def testCase17_updateResource_validate_statusCode():
    json_response = resp.json()
    json_response = resp.status_code
    print(json_response)
    assert json_response is not None


def testCase18_updateResource_validate_header():
    json_resp = resp.headers.get("content-Type")
    print(json_resp)
    assert json_resp is not None


def testCase19_updateResource_validate_response_body_gender():
    print(resp.json())
    assert resp.json()['gender'] is not None
    print("Response body validation")


def testCase20_updateResource_validate_response_body_name():
    print(resp.json())
    assert resp.json()['name'] is not None
    print("Response body validation")
