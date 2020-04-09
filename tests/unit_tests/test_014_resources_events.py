from flask import url_for


def test_events(client, access_token):
    token = access_token
    res = client.get(url_for('events'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json[0]['id'] == 1
    assert res.json[0]['domain'] == "system"
    assert res.json[0]['action'] == "migrated"


def test_event(client, access_token):
    token = access_token
    res = client.get(url_for('event', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['domain'] == "system"
    assert res.json['action'] == "migrated"
