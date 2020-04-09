from flask import url_for


def test_userroles(client, access_token):
    token = access_token
    res = client.get(url_for('userroles'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert len(res.json) > 0
    assert res.json[0]['id'] == 1
    assert res.json[0]['name'] == "admin"
    assert 'users' in res.json[0]
    assert res.json[0]['users'][0]['id'] == 1


def test_userrole_id(client, access_token):
    token = access_token
    res = client.get(url_for('userroleid', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "admin"
    assert 'users' in res.json
    assert res.json['users'][0]['id'] == 1


def test_userrole_name(client, access_token):
    token = access_token
    headers = {'authorization': "Bearer {token}".format(token=token)}
    res = client.get(url_for('userrolename', name="admin"), headers=headers)
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "admin"
    assert 'users' in res.json
    assert res.json['users'][0]['id'] == 1
