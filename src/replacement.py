from src.select_time import select_last


def replacement_1(transactions_stars):

    for transaction in transactions_stars:

        if transaction.get('from'):
            transaction['from'] = transaction['from'][:-10]+"*"*6+transaction['from'][-4:]

        if transaction.get('to'):
            transaction['to'] = transaction['to'][4]+"**"+transaction['to'][-4:]

    #print(transactions_stars)
    #print(len(transactions_stars))
    return transactions_stars

#replacement_1()