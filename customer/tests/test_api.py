def test_customers_get_all(client, customers):  # Arrange
    """Test get all customers"""
    # Act
    response = client.get("/api/v1/customers/")
    # Assert
    assert response.status_code == 200
    data = response.json["customers"]
    assert len(data) == 3
    for customer in customers:
        assert customer.id in [item["id"] for item in data]
        assert customer.first_name in [item["first_name"] for item in data]
        assert customer.last_name in [item["last_name"] for item in data]
        assert customer.email in [item["email"] for item in data]


def test_customers_get_one(client, customers):  # Arrange
    """Test get all customers"""
    for customer in customers:
        # Act
        response = client.get(f"/api/v1/customers/{customer.id}")
        data = response.json
        # Assert
        assert response.status_code == 200
        assert data["first_name"] == customer.first_name
        assert data["last_name"] == customer.last_name
        assert data["email"] == customer.email
