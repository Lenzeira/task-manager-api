from app.auth import verify_password, get_password_hash

def test_password_hashing_and_verification():
    password = "senha123"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed)
    assert not verify_password("errada", hashed)
