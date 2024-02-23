import os

from src.replacement import replacement_1
from src.select_time import select_last
from src.selection_execution import select
from src.separation import separation_line

text_output = []


def output(text_output):
    file = os.path.join('operations.json')
    time_select = select(file)
    transactions_stars = select_last(time_select)
    separation = replacement_1(transactions_stars)
    output_display = separation_line(separation)

    text_output = []

    for transaction in output_display:
        text = (f"""
{transaction['date'][8:10]+'.'+transaction['date'][5:7]+'.'+transaction['date'][:4]} {transaction['description']}
{transaction.get('from', '')} -> {transaction['to']}
{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}""")
        text_output.append(text)
        print(text)
    return text_output
#output(text_output)
#result = output(text_output)
#print(result)
