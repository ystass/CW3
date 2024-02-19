from src.separation import separation_line


def output():
    output_display = separation_line()

    for transaction in output_display:
        text = (f"""
{transaction['date'][8:10]+'.'+transaction['date'][5:7]+'.'+transaction['date'][:4]} {transaction['description']}
{transaction.get('from', '')} -> {transaction['to']}
{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}""")
        print(text)
    return text

operation = output()

#print(operation)