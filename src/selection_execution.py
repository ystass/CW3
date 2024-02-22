import json


def select(file):
    transactions_executed = []

    with open(file, "r", encoding="utf8") as f:
        transactions_ = json.load(f)
    #print(transactions_)
    for transaction in transactions_:
        if transaction.get("state") == "EXECUTED":
            transactions_executed.append(transaction)

    # print(transactions_executed)
    return transactions_executed

#select()
