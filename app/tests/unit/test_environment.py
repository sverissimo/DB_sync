from config import env


def test_environment_vairables():

    environment_vairables = {}
    v1 = env.__dict__.items()
    v2 = list(v1)
    variables_tuple = list(filter(lambda el: el[0].isupper() == True, v2))

    for tuple in variables_tuple:
        environment_vairables[tuple[0]] = tuple[1]

    """ for key, value in environment_vairables.items():
        print(type(value), key, value) """

    assert all(type(value) == str for key, value in environment_vairables.items())
    assert all(len(value) > 0 for key, value in environment_vairables.items())
    assert all(
        key in environment_vairables
        for key in [
            "HOST",
            "USER",
            "PASS",
            "AUTH_SYNC",
            "USER_FOLDER",
            "DB_SYNC_PATH_PY",
            "SGTI_FILE_FOLDER",
            "SQL_SCRIPTS_FOLDER",
        ]
    )
