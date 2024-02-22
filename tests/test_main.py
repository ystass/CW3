from src import main


test_data = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': ' **5907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07 06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic  2842 87** **** 9012', 'to': ' **3655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19 09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro  7810 84** **** 5568', 'to': ' **2869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13 17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 3861 1439 52** **** 9794', 'to': ' **8125'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05 12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': ' **8381'}]

def test_main():
    assert main.output(test_data) == ['\n08.12.2019 Открытие вклада\n ->  **5907\n41096.24 USD', '\n07.12.2019 Перевод организации\nVisa Classic  2842 87** **** 9012 ->  **3655\n48150.39 USD', '\n19.11.2019 Перевод организации\nMaestro  7810 84** **** 5568 ->  **2869\n30153.72 руб.', '\n13.11.2019 Перевод со счета на счет\nСчет 3861 1439 52** **** 9794 ->  **8125\n62814.53 руб.', '\n05.11.2019 Открытие вклада\n ->  **8381\n21344.35 руб.']

