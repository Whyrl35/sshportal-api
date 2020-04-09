from flask import url_for


def test_sshkeys(client, access_token):
    token = access_token
    res = client.get(url_for('keys'), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert len(res.json) > 0
    assert res.json[0]['id'] == 1
    assert res.json[0]['name'] == "default"
    assert res.json[0]['type'] == "rsa"
    assert res.json[0]['comment'] == "created by sshportal"
    assert res.json[0]['priv_key'][0:31] == "-----BEGIN RSA PRIVATE KEY-----"
    assert res.json[0]['pub_key'][0:7] == "ssh-rsa"
    assert res.json[0]['length'] == 2048


def test_sshkey_id(client, access_token):
    token = access_token
    res = client.get(url_for('keyid', id=1), headers={'authorization': "Bearer {token}".format(token=token)})
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "default"
    assert res.json['type'] == "rsa"
    assert res.json['comment'] == "created by sshportal"
    assert res.json['priv_key'][0:31] == "-----BEGIN RSA PRIVATE KEY-----"
    assert res.json['pub_key'][0:7] == "ssh-rsa"
    assert res.json['length'] == 2048


def test_sshkey_name(client, access_token):
    token = access_token
    headers = {'authorization': "Bearer {token}".format(token=token)}
    res = client.get(url_for('keyname', name="default"), headers=headers)
    assert res.status_code == 200
    assert res.json['id'] == 1
    assert res.json['name'] == "default"
    assert res.json['type'] == "rsa"
    assert res.json['comment'] == "created by sshportal"
    assert res.json['priv_key'][0:31] == "-----BEGIN RSA PRIVATE KEY-----"
    assert res.json['pub_key'][0:7] == "ssh-rsa"
    assert res.json['length'] == 2048
