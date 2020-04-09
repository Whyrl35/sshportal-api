from flask import url_for


def test_usergroups(client, access_token):
    token = access_token
    res = client.get(url_for('usergroups'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert len(res.json) > 0
    assert res.json[0]['id'] == 1
    assert res.json[0]['name'] == "default"
    assert res.json[0]['comment'] == "created by sshportal"
    assert 'users' in res.json[0]
    assert 'acls' in res.json[0]
    assert res.json[0]['users'][0]['id'] == 1
    assert res.json[0]['acls'][0]['id'] == 1


def test_usergroup_id(client, access_token):
    token = access_token
    res = client.get(url_for('usergroupid', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "default"
    assert res.json['comment'] == "created by sshportal"
    assert 'users' in res.json
    assert 'acls' in res.json
    assert res.json['users'][0]['id'] == 1
    assert res.json['acls'][0]['id'] == 1


def test_usergroup_name(client, access_token):
    token = access_token
    headers = {'authorization': "Bearer {token}".format(token=token)}
    res = client.get(url_for('usergroupname', name="default"), headers=headers)
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['id'] == 1
    assert res.json['name'] == "default"
    assert res.json['comment'] == "created by sshportal"
    assert 'users' in res.json
    assert 'acls' in res.json
    assert res.json['users'][0]['id'] == 1
    assert res.json['acls'][0]['id'] == 1
