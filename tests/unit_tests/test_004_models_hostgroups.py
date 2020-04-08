from sshportal_api.models.hostgroups import HostGroupsModel


def test_hostgroup_by_id():
    """
    GIVEN a Hostgroup model
    WHEN test the first hostgroup
    THEN check the id and more
    """
    hg = HostGroupsModel.by_id(1)
    assert hg.id == 1
    assert hg.name == "default"
    assert hg.comment == "created by sshportal"


def test_hostgroup_by_name():
    """
    GIVEN a Hostgroup model
    WHEN test the hostgroup by its name
    THEN check the id and more
    """
    hg = HostGroupsModel.by_name("default")
    assert hg.id == 1
    assert hg.name == "default"
    assert hg.comment == "created by sshportal"


def test_hostgroup_to_json():
    """
    GIVEN a Hostgroup model
    WHEN test the to_json method
    THEN check the id, name, comment and more
    """
    hg = HostGroupsModel.by_id(1)
    hg_json = HostGroupsModel.to_json(hg)
    assert hg.id == hg_json['id']
    assert hg.name == hg_json['name']
    assert hg.comment == hg_json['comment']
    assert hg_json['created_at'] == (hg.created_at.isoformat() if hg.created_at else hg.created_at)
    assert hg_json['updated_at'] == (hg.updated_at.isoformat() if hg.updated_at else hg.updated_at)
    assert hg_json['deleted_at'] == (hg.deleted_at.isoformat() if hg.deleted_at else hg.deleted_at)
