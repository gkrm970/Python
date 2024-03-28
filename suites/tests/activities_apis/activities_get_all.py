import requests


def test_activities_get_all():
    headers = {'Content-Type': 'application/json'}
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
    res = requests.get(url=url, headers=headers)
    print(res.text)
    assert res.status_code == 200
    return res


test_activities_get_all()
