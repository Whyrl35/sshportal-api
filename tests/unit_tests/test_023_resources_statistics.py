from flask import url_for


def test_statistics(client, access_token):
    token = access_token
    res = client.get(url_for('statistics'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert 'users' in res.json
    assert res.json['users']['count'] >= 0
    assert 'keys' in res.json
    assert res.json['keys']['count'] >= 0
    assert 'hosts' in res.json
    assert res.json['hosts']['count'] >= 0
    assert 'acls' in res.json
    assert res.json['acls']['count'] >= 0
    assert 'sessions' in res.json
    assert res.json['sessions']['count'] >= 0
    assert 'events' in res.json
    assert res.json['events']['count'] >= 0
