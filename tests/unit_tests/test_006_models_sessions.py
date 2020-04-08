from sshportal_api.models.sessions import SessionsModel


def test_sessions_by_id():
    """
    GIVEN a Sessions model
    WHEN test the first session
    THEN check the id and more
    """
    session = SessionsModel.by_id(1)
    assert session.id == 1
    assert session.status == "closed"
    assert session.user_id == 1
    assert session.host_id == 1
    assert session.comment == ""


def test_sessions_to_json():
    """
    GIVEN a Sessions model
    WHEN test the to_json method
    THEN check the id and more
    """
    session = SessionsModel.by_id(1)
    session_json = SessionsModel.to_json(session)
    assert session.id == session_json['id']
    assert session.status == session_json['status']
    assert session.user_id == session_json['user_id']
    assert session.host_id == session_json['host_id']
    assert session.comment == session_json['comment']
