from datetime import datetime
from src.selection_execution import select

def select_last():
    time_select = select()
    for transaction in time_select:
        if transaction.get('date'):
            transaction['date'] = transaction['date'][:10]+" "+transaction['date'][11:]

    for transaction in time_select:
        if transaction.get('date'):
            time_select = sorted(time_select, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S.%f'), reverse=True)
    last_five = time_select[0:5]
    #print(last_five)
    #print(len(last_five))
    return last_five

select_last()