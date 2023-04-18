import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(253, 0)
    with pytest.raises(TypeError):
        encrypt_message('message', 'key')

    assert encrypt_message("python", -6) == "nohtyp"
    assert encrypt_message("python", 4) == "no_htyp"
