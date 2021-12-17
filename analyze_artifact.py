import sql

'''
Chain_art 에 저장된 아티팩트를 분석하고 가중치를 메겨 해당 체인이 악성행위인지 여부를 판단하여 반환.
'''
def analyze_art(dbname, chain_number):
    art_weight = {
        # 가중치 딕셔너리로 넣는 부분

    }
    total = 0
    threshold = 100

    columns = sql.select_chain_art(dbname, chain_number)

    for column in columns:
        if column[3] in art_weight.keys():
            total += art_weight[column[3]]
    

    if total >= threshold:
        return chain_number
    else:
        return -1
