from flask import url_for


def test_userkeys(client, access_token):
    token = access_token
    res = client.get(url_for('userkeys'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json[0]['id'] == 1
    assert len(res.json[0]['key']) > 1
    assert len(res.json[0]['authorized_key']) > 1
    assert res.json[0]['comment'] == "created by sshportal"


def test_userkey(client, access_token):
    token = access_token
    res = client.get(url_for('userkey', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert len(res.json['key']) > 1
    assert len(res.json['authorized_key']) > 1
    assert res.json['comment'] == "created by sshportal"
