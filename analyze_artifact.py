import sql

'''
Chain_art 에 저장된 아티팩트를 분석하고 가중치를 메겨 해당 체인이 악성행위인지 여부를 판단하여 반환.
'''
def analyze_art(dbname, chain_number):
    art_weight = {
        

    }
    total = 0
    threshold = 100

    columns = sql.select_chain_art(dbname, chain_number)

    for column in columns:
        total += art_weight[column[3]]
    

    if total >= threshold:
        return 1
    else:
        return 0