import requests

url = "https://gorest.co.in/public/v2/users/1443"
headers = {"Authorization": "Bearer 8a5960423128689eaf2a5dc6eea7c5daa78aa5b746ff2f777916f9c295750df1"}
resp = requests.delete(url, headers=headers)


def testCase21_deleteResource_validate_statusCode_Positive():
    print(resp.json())
    json_resp = resp.status_code
    print(json_resp)
    assert json_resp == 204, "code doesnt match"


def testCase22_deleteResource_validate_statusCode_negative():
    print(resp.json())
    json_resp = resp.status_code
    print(json_resp)
    assert json_resp is not None




