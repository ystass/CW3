import json


def select(file):
    with open(file, "r", encoding="utf8") as f:
        transactions_ = json.load(f)

    transactions_executed = []

    for transaction in transactions_:
        if transaction.get("state") == "EXECUTED":
            transactions_executed.append(transaction)

    #print(transactions_executed)
    return transactions_executed

#select()

