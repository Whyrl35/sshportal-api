from flask import url_for


def test_hosts(client, access_token):
    token = access_token
    res = client.get(url_for('hosts'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json[0]['id'] == 1


def test_host_id(client, access_token):
    token = access_token
    res = client.get(url_for('hostid', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1


# def test_host_name(client, access_token):
    # token = access_token
    # res = client.get(url_for('hostname', name="default"), headers={'authorization': "Bearer {token}".format(token=token)})  # noqa
    # assert res.status_code == 200
