from flask import url_for


def test_user_login(client, request, create_test_user):
    name = 'pytest'
    password = 'password'
    create_test_user(name, password)
    res = client.post(url_for('login'), json={'name': name, 'password': password})
    assert res.status_code == 200
    assert 'access_token' in res.json
    assert 'refresh_token' in res.json
    assert res.json['user'] == name
    request.config.cache.set('sshportal_api/access_token', res.json['access_token'])
    request.config.cache.set('sshportal_api/refresh_token', res.json['refresh_token'])


def test_token(client, request, refresh_token):
    token = refresh_token
    res = client.post(url_for('tokenrefresh'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert 'access_token' in res.json
    request.config.cache.set('sshportal_api/access_token', res.json['access_token'])


def test_users(client, access_token):
    token = access_token
    res = client.get(url_for('allusers'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert 'users' in res.json
    assert len(res.json['users']) > 0
    assert res.json['users'][0]['id'] == 1
    assert res.json['users'][0]['name'] == "admin"


def test_user(client, access_token):
    token = access_token
    res = client.get(url_for('user'), headers={'authorization': "Bearer {token}".format(token=token)},
                     json={'name': "admin"})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "admin"
