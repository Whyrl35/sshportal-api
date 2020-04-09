from flask import url_for


def test_sessions(client, access_token):
    token = access_token
    res = client.get(url_for('sessions'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json[0]['id'] == 1


def test_session(client, access_token):
    token = access_token
    res = client.get(url_for('session', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
