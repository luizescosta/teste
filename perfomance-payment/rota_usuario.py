from uuid import uuid4

from locust import TaskSet, task


class UserRouteLoadTest(TaskSet):

    @task()
    def test_list_users(self):
        self.client.get("/api/healthz", name="teste")

    @task()
    def test_create(self):
        self.client.post(
            "/simple/payments",
            name="Criar Compra",
            json={
                "ClientId": "stress test",
                "MerchantOrderId": f"{uuid4()}",
                "TransactionId": f"{uuid4()}",
                "Currency": "BRL",
                "Installments": 4,
                "OrderNumber": f"{uuid4()}",
                "TotalAmount": 20000,
                "TotalDiscountAmount": 0,
                "TotalShippingAmount": 0,
                "Customer": {
                    "Name": "Anderson Costa",
                    "DocumentNumber": "23158907054",
                    "DocumentType": "CPF",
                    "Email": "userqaauto@outlook.com",
                    "Phone": "11912345678",
                    "CellPhone": "11912345678",
                    "ShippingAddress": {
                        "Country": "BRA",
                        "Street": "Pais Leme",
                        "Number": "524",
                        "Complement": "",
                        "District": "Pinheiros",
                        "ZipCode": "05424010",
                        "City": "São Paulo",
                        "State": "SP"
                    },
                    "BillingAddress": {
                        "Country": "BRA",
                        "Street": "Brigadeiro Faria Lima Avenue",
                        "Number": "4440",
                        "Complement": "10th Floor",
                        "District": "Itaim Bibi",
                        "ZipCode": "04538132",
                        "City": "São Paulo",
                        "State": "SP"
                    }
                },
                "Items": [{
                    "Id": "132981",
                    "Name": "Batedeira Walita",
                    "Price": 20000,
                    "Quantity": 1,
                    "Discount": 0,
                    "Total": 20000
                }
                ],
                "CallbackUrl": "https://mock-server.qa-titan.lendico.net.br/qa-callback"
            },
            headers={
                "API-AppKey": "90b5c7fb-63c3-4672-a2c8-2c05ce5c4e72",
                "API-AppToken": "5a7b3380-0fad-4fa2-99f4-651391c5ed45",
            }
        )
