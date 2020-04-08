from sshportal_api.models.sshkeys import SshKeysModel


def test_sshkeys_by_id():
    """
    GIVEN a Sshkeys model
    WHEN test the first setting
    THEN check the id and more
    """
    sshkey = SshKeysModel.by_id(1)
    assert sshkey.id == 1
    assert sshkey.name == "default"
    assert sshkey.type == "rsa"
    assert sshkey.length == 2048
    assert sshkey.fingerprint == ""
    assert sshkey.priv_key[0:31] == "-----BEGIN RSA PRIVATE KEY-----"
    assert sshkey.pub_key[0:7] == "ssh-rsa"
    assert sshkey.comment == "created by sshportal"


def test_sshkeys_by_name():
    """
    GIVEN a Sshkeys model
    WHEN test the first setting
    THEN check the id and more
    """
    sshkey = SshKeysModel.by_name('default')
    assert sshkey.id == 1
    assert sshkey.name == "default"
    assert sshkey.type == "rsa"
    assert sshkey.length == 2048
    assert sshkey.fingerprint == ""
    assert sshkey.priv_key[0:31] == "-----BEGIN RSA PRIVATE KEY-----"
    assert sshkey.pub_key[0:7] == "ssh-rsa"
    assert sshkey.comment == "created by sshportal"


def test_sshkeys_to_json():
    """
    GIVEN a Sshkeys model
    WHEN test the to_json method
    THEN check the id and more
    """
    sshkey = SshKeysModel.by_id(1)
    sshkey_json = SshKeysModel.to_json(sshkey)
    assert sshkey.id == sshkey_json['id']
    assert sshkey.name == sshkey_json['name']
    assert sshkey.type == sshkey_json['type']
    assert sshkey.length == sshkey_json['length']
    assert sshkey.fingerprint == sshkey_json['fingerprint']
    assert sshkey.priv_key == sshkey_json['priv_key']
    assert sshkey.pub_key == sshkey_json['pub_key']
    assert sshkey.comment == sshkey_json['comment']
    assert sshkey_json['created_at'] == (sshkey.created_at.isoformat() if sshkey.created_at else sshkey.created_at)
    assert sshkey_json['updated_at'] == (sshkey.updated_at.isoformat() if sshkey.updated_at else sshkey.updated_at)
    assert sshkey_json['deleted_at'] == (sshkey.deleted_at.isoformat() if sshkey.deleted_at else sshkey.deleted_at)
