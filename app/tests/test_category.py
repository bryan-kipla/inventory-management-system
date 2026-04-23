def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
        "role": "user"
    })
    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"

def test_login_user(client):
    # First register
    client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
        "role": "user"
    })
    # Then login
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json["message"] == "Login successful"
