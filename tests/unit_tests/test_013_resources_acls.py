from flask import url_for


def test_acls(client, access_token):
    token = access_token
    res = client.get(url_for('acls'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json[0]['id'] == 1
    assert res.json[0]['action'] == "allow"
    assert res.json[0]['comment'] == "created by sshportal"
    assert 'host_groups' in res.json[0]
    assert 'user_groups' in res.json[0]
    assert res.json[0]['host_groups']['name'] == "default"
    assert res.json[0]['user_groups']['name'] == "default"


def test_acl(client, access_token):
    token = access_token
    res = client.get(url_for('acl', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['action'] == "allow"
    assert res.json['comment'] == "created by sshportal"
    assert 'host_groups' in res.json
    assert 'user_groups' in res.json
    assert res.json['host_groups']['name'] == "default"
    assert res.json['user_groups']['name'] == "default"
