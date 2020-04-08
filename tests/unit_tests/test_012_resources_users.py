from flask import url_for


def test_user_login(client, create_test_user):
    name = 'pytest'
    password = 'password'
    create_test_user(name, password)
    res = client.post(url_for('login'), json={'name': name, 'password': password})
    assert res.status_code == 200
    res_json = res.json
    assert 'access_token' in res_json
    assert 'refresh_token' in res_json
    assert res_json['user'] == name
