from src import replacement

test_data = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07 06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19 09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13 17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05 12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]

def test_replacement():
    assert replacement.replacement_1(test_data) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46:21.935582',
                                            'operationAmount': {'amount': '41096.24',
                                                                'currency': {'name': 'USD', 'code': 'USD'}},
                                            'description': 'Открытие вклада', 'to': ' **5907'},
                                           {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07 06:17:14.634890',
                                            'operationAmount': {'amount': '48150.39',
                                                                'currency': {'name': 'USD', 'code': 'USD'}},
                                            'description': 'Перевод организации',
                                            'from': 'Visa Classic 284287******9012', 'to': ' **3655'},
                                           {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19 09:22:25.899614',
                                            'operationAmount': {'amount': '30153.72',
                                                                'currency': {'name': 'руб.', 'code': 'RUB'}},
                                            'description': 'Перевод организации', 'from': 'Maestro 781084******5568',
                                            'to': ' **2869'},
                                           {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13 17:38:04.800051',
                                            'operationAmount': {'amount': '62814.53',
                                                                'currency': {'name': 'руб.', 'code': 'RUB'}},
                                            'description': 'Перевод со счета на счет',
                                            'from': 'Счет 3861143952******9794', 'to': ' **8125'},
                                           {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05 12:04:13.781725',
                                            'operationAmount': {'amount': '21344.35',
                                                                'currency': {'name': 'руб.', 'code': 'RUB'}},
                                            'description': 'Открытие вклада', 'to': ' **8381'}]
    assert len(replacement.replacement_1(test_data)) == 5
