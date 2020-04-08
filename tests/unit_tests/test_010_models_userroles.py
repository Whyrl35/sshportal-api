from sshportal_api.models.userroles import UserRolesModel


def test_userroles_by_id():
    """
    GIVEN a Userroles model
    WHEN test the first userrole
    THEN check the id and more
    """
    ur = UserRolesModel.by_id(1)
    assert ur.id == 1
    assert ur.name == 'admin'


def test_userroles_by_name():
    """
    GIVEN a Userroles model
    WHEN test the first userrole
    THEN check the id and more
    """
    ur = UserRolesModel.by_name('admin')
    assert ur.id == 1
    assert ur.name == 'admin'


def test_userroles_to_json():
    """
    GIVEN a Userroles model
    WHEN test the to_json method
    THEN check the id and more
    """
    ur = UserRolesModel.by_id(1)
    ur_json = UserRolesModel.to_json(ur)
    assert ur.id == ur_json['id']
    assert ur.name == ur_json['name']
    assert ur_json['created_at'] == (ur.created_at.isoformat() if ur.created_at else ur.created_at)
    assert ur_json['updated_at'] == (ur.updated_at.isoformat() if ur.updated_at else ur.updated_at)
    assert ur_json['deleted_at'] == (ur.deleted_at.isoformat() if ur.deleted_at else ur.deleted_at)
