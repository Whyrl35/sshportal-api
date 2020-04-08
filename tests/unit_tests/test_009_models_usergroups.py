from sshportal_api.models.usergroups import UserGroupsModel


def test_usergroup_by_id():
    """
    GIVEN a Usergroups model
    WHEN test the first usergroup
    THEN check the id and more
    """
    ug = UserGroupsModel.by_id(1)
    assert ug.id == 1
    assert ug.name == 'default'
    assert ug.comment == 'created by sshportal'


def test_usergroup_by_name():
    """
    GIVEN a Usergroups model
    WHEN test the usergroup by name
    THEN check the id and more
    """
    ug = UserGroupsModel.by_name('default')
    assert ug.id == 1
    assert ug.name == 'default'
    assert ug.comment == 'created by sshportal'


def test_usergroup_to_json():
    """
    GIVEN a usergroup model
    WHEN test the to_json method
    THEN check the id and more
    """
    ug = UserGroupsModel.by_id(1)
    ug_json = UserGroupsModel.to_json(ug)
    assert ug.id == ug_json['id']
    assert ug.name == ug_json['name']
    assert ug.comment == ug_json['comment']
    assert ug_json['created_at'] == (ug.created_at.isoformat() if ug.created_at else ug.created_at)
    assert ug_json['updated_at'] == (ug.updated_at.isoformat() if ug.updated_at else ug.updated_at)
    assert ug_json['deleted_at'] == (ug.deleted_at.isoformat() if ug.deleted_at else ug.deleted_at)
