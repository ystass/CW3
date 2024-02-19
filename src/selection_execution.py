import json


def select():
    with open("operations.json", "r", encoding="utf8") as f:
        transactions_ = json.load(f)

    transactions_executed = []

    for transaction in transactions_:
        if transaction.get("state") == "EXECUTED":
            transactions_executed.append(transaction)

    #print(transactions_executed)
    return transactions_executed

select()

