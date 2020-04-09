from flask import url_for


def test_hostgroups(client, access_token):
    token = access_token
    res = client.get(url_for('hostgroups'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json[0]['id'] == 1
    assert res.json[0]['name'] == "default"
    assert res.json[0]['comment'] == "created by sshportal"
    assert 'acls' in res.json[0]
    assert 'hosts' in res.json[0]
    assert res.json[0]['acls'][0]['id'] == 1
    assert res.json[0]['acls'][0]['comment'] == "created by sshportal"


def test_hostgroup_id(client, access_token):
    token = access_token
    res = client.get(url_for('hostgroupid', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "default"
    assert res.json['comment'] == "created by sshportal"
    assert 'acls' in res.json
    assert 'hosts' in res.json
    assert res.json['acls'][0]['id'] == 1
    assert res.json['acls'][0]['comment'] == "created by sshportal"


def test_hostgroup_name(client, access_token):
    token = access_token
    res = client.get(url_for(
        'hostgroupname', name="default"),
        headers={'authorization': "Bearer {token}".format(token=token)}
    )
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "default"
    assert res.json['comment'] == "created by sshportal"
    assert 'acls' in res.json
    assert 'hosts' in res.json
    assert res.json['acls'][0]['id'] == 1
    assert res.json['acls'][0]['comment'] == "created by sshportal"
