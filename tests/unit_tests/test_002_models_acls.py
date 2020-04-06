
from sshportal_api.models.acls import AclsModel


def test_acls_by_id():
    """
    GIVEN a Acl model
    WHEN test the default acl
    THEN check the id, action, comment, weight
    """
    acl = AclsModel.by_id(1)
    assert acl.id == 1
    assert acl.action == "allow"
    assert acl.comment == "created by sshportal"
    assert acl.weight == 0


def test_acls_to_json():
    acl = AclsModel.by_id(1)
    acl_json = AclsModel.to_json(acl)
    assert acl.id == acl_json['id']
    assert acl.action == acl_json['action']
    assert acl.comment == acl_json['comment']
    assert acl.weight == acl_json['weight']
    assert acl.host_pattern == acl_json['host_pattern']
    assert acl_json['created_at'] == (acl.created_at.isoformat() if acl.created_at else acl.created_at)
    assert acl_json['updated_at'] == (acl.updated_at.isoformat() if acl.updated_at else acl.updated_at)
    assert acl_json['deleted_at'] == (acl.deleted_at.isoformat() if acl.deleted_at else acl.deleted_at)


