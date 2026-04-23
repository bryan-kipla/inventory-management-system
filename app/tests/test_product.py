def test_create_product(client):
    # Create category first
    client.post("/categories", json={"name": "Electronics"})
    response = client.post("/products", json={
        "name": "Laptop",
        "category_id": 1,
        "price": 1200.0
    })
    assert response.status_code == 201
    assert response.json["message"] == "Product created successfully"
