import sql

'''
Chain_art 에 저장된 아티팩트를 분석하고 가중치를 메겨 해당 체인이 악성행위인지 여부를 판단하여 반환.
'''
def analyze_art(dbname, chain_number):
    art_weight = {
        # 가중치 딕셔너리로 넣는 부분
        # 10 = Malcious Execution, 5 = defender OR Powershell. 3 = WER
        '1002' : 5,
        '1000' : 3,
        '1001' : 3,
        'ShellClient':10,
        'Mimikatz':10,
        'SafetyKatz':10,
        'ProcDump':10,
        'BadPotato':10,
        'RottenPotato':10,
        'PlugX':10,
        'Empire':10,
        'Family Keylogger':10,
        'Ghost Keylogger':10,
        'Microsoft Windows PowerShell' : 5,
        'Microsoft Windows Security Auditing' : 2,
        'Microsoft Windows Eventlog' : 2,
        'Microsoft Windows TerminalServices Licensing' : 2
    }
    total = 0
    threshold = 8

    columns = sql.select_chain_art(dbname, chain_number)

    for column in columns:
        if column[3] in art_weight.keys(): # chain_art 테이블의 description 문자열이 키에 존재하는가
            total += art_weight[column[3]]
        elif '.pf' in column[3]:
            total += 2
    

    if total >= threshold:
        return chain_number
    else:
        return -1
