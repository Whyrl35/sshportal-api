from sshportal_api.models.userkeys import UserKeysModel


def test_userkeys_by_id():
    """
    GIVEN a Userkeys model
    WHEN test the first userkey
    THEN check the id and more
    """
    uk = UserKeysModel.by_id(1)
    assert uk.id == 1
    # FIXME : test that key is a string, contains stuff => assert uk.key == ""
    assert uk.user_id == 1
    assert uk.comment == "created by sshportal"
    assert uk.authorized_key[0:7] == "ssh-rsa"


def test_userkeys_to_json():
    """
    GIVEN a Settings model
    WHEN test the to_json method
    THEN check the id and more
    """
    uk = UserKeysModel.by_id(1)
    uk_json = UserKeysModel.to_json(uk)
    assert uk.id == uk_json['id']
    # FIXME : test that key exist, is a string and decrypt it via paramiko => assert uk.key == uk_json['key']
    assert uk.user_id == uk_json['user_id']
    assert uk.comment == uk_json['comment']
    assert uk.authorized_key == uk_json['authorized_key']
    assert uk_json['created_at'] == (uk.created_at.isoformat() if uk.created_at else uk.created_at)
    assert uk_json['updated_at'] == (uk.updated_at.isoformat() if uk.updated_at else uk.updated_at)
    assert uk_json['deleted_at'] == (uk.deleted_at.isoformat() if uk.deleted_at else uk.deleted_at)
