import sql
import find_chain
import analyze_artifact
import datetime

def analyze(dbname):
    eventid_set = []
    proc_set = []
    reg_RECmd_set = []
    reg_services_set = []
    chain_number = 1

    time = find_chain.connect_chain(dbname) # 체인의 시작 시간, 종료 시간을 받아옴
    while time: # 체인 형성 가능
        start_time = time[0] # 체인 시작
        end_time = time[1] # 체인 종료

        sql.insert_chain_art(dbname, [chain_number]+list(time[2]))
        sql.insert_chain_art(dbname, [chain_number]+list(time[3]))

        columns = sql.select_eventlog(dbname, start_time, end_time, eventid_set) # start~end 시간대에 생성되었으며 가중치를 메길만한 evnetlog 모두 chain_art 테이블에 저장
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column)) 
        
        columns = sql.select_prefetch(dbname, start_time, end_time, proc_set) # start~end 시간대에 생성되었으며 가중치를 메길만한 프리패치 항목들을 chain_art 테이블에 저장
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))
        
        columns = sql.select_reg_RECmd(dbname, start_time, end_time, reg_RECmd_set) # start~end 시간대에 생성된 레지스트리들을 chain_art에 저장
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))

        columns = sql.select_reg_services(dbname, start_time, end_time, reg_services_set) # 해당 시점에 생성된 서비스 관련 레지스트리 chain_art에 저장
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))
        
        # 위의 모든 값들은 start~end 시간대, 즉 체인이 구성된 동안의 아티팩트들의 모임이다.
        
        
        if analyze_artifact.analyze_art(dbname, chain_number):
            time = find_chain.connect_chain(dbname, end_time+datetime.timedelta(milliseconds=1)) # 체인이 형성되었다면 해당 체인 이후로부터 생성
        else:
            time = find_chain.connect_chain(dbname, start_time+datetime.timedelta(milliseconds=1)) # 체인이 형성되지 않았다면 시작 아티팩트 직후부터 다시 찾기

        chain_number = chain_number + datetime.timedelta(eventid_set)
        

    return None