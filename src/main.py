import os

from src.replacement import replacement_1
from src.select_time import select_last
from src.selection_execution import select
from src.separation import separation_line



def output():
    file = os.path.join('operations.json')
    time_select = select(file)
    transactions_stars = select_last(time_select)
    #print(transactions_stars)
    separation = replacement_1(transactions_stars)
    #print(separation)
    output_display = separation_line(separation)

    for transaction in output_display:
        print(f"""
{transaction['date'][8:10]+'.'+transaction['date'][5:7]+'.'+transaction['date'][:4]} {transaction['description']}
{transaction.get('from', '')} -> {transaction['to']}
{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}""")

    return

output()

