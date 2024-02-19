from src.replacement import replacement_1


def separation_line():
    separation = replacement_1()
    for transaction in separation:
        if transaction.get('from'):
            transaction['from'] = (transaction['from'][:-16]+" "+transaction['from'][-16:-12]+" "
                                   +transaction['from'][-12:-8]+" "+transaction['from'][-8:-4]+" "
                                   +transaction['from'][-4:])
    #print(separation)
    #print(len(separation))
    return separation

separation_line()
