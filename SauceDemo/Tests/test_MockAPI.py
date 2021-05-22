import requests


class TestMock:

    def create_billpay_for(self, name):
        return {
            "name": name,
            "address": {
                "street": "My street",
                "city": "My city",
                "state": "My state",
                "zipCode": "90210",
            },
            "phoneNumber": "0123456789",
            "accountNumber": 12345,
        }

    def test_post_method(self):
        my_name = "John Smith"
        json_object = self.create_billpay_for(my_name)
        response = requests.post(
            "https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500",
            headers={"Accept": "application/json"},
            json=json_object,
        )
        assert response.status_code == 200
        assert response.json()["payeeName"] == my_name

    def create_user(self):
        return {
            "external_id": "postman"
        }

    def test_postman_create_user(self):
        json_body = self.create_user()
        response = requests.post("https://node-fake-api-server.herokuapp.com/",
                                 headers={"Content-Type": "application/json", "X-FakeAPI-Action": "register"},
                                 json=json_body)
        assert response.status_code == 201


