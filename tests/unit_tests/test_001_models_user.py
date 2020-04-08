from sshportal_api.models.users import UserModel


def test_find_user_name():
    """
    GIVEN a User model
    WHEN test the default user
    THEN check the email, hashed_password, and somes fields are well configured
    """
    user = UserModel.find_by_name("admin")
    assert user.name == "admin"
    assert user.email == "admin@localhost"
    assert user.comment == "created by sshportal"
    assert user.password is None


def test_find_user_id():
    """
    GIVEN a User model
    WHEN test the default user by id
    THEN check the email, hashed_password, and somes fields are well configured
    """
    user = UserModel.by_id(1)
    assert user.name == "admin"
    assert user.email == "admin@localhost"
    assert user.comment == "created by sshportal"
    assert user.password is None


def test_user_to_json():
    """
    GIVEN a User model
    WHEN test the to_json method
    THEN check the email, hashed_password, and somes fields are well configured
    """
    user = UserModel.find_by_name("admin")
    user_json = UserModel.to_json(user)
    assert user.name == user_json['name']
    assert user.email == user_json['email']
    assert user.comment == user_json['comment']
    assert user.password == user_json['password']
    assert user_json['created_at'] == (user.created_at.isoformat() if user.created_at else user.created_at)
    assert user_json['updated_at'] == (user.updated_at.isoformat() if user.updated_at else user.updated_at)
    assert user_json['deleted_at'] == (user.deleted_at.isoformat() if user.deleted_at else user.deleted_at)
    assert user.is_admin == user_json['is_admin']


def test_user_hash():
    """
    GIVEN a User model
    WHEN test the password hashing method
    THEN checkt the password and its hash
    """
    password = "MyTestingPassword"
    hashed = UserModel.generate_hash(password)
    assert UserModel.verify_hash(password, hashed) is True
