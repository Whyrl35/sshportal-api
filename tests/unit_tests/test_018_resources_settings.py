from flask import url_for


def test_settings(client, access_token):
    token = access_token
    res = client.get(url_for('settings'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200


def test_setting(client, access_token):
    token = access_token
    res = client.get(url_for('setting', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
