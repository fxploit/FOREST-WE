import sql
import find_chain
import analyze_artifact
import datetime

def analyze(dbname):
    eventid_set = [1000,1001,4720,4724,4726,4731,4732,4733,4734,4735,4738,4756,4625,4624,4625,4648,4634,4616,4670,1100,1102,1149,4624,4625,4634,21,22,23,24,25,39,40,261,400,403,600,1149,5158,4104,4105,4106,4663,4670,4673,4688,4703,8193,8194,8195,8196,8197,12039,40961,53506,40962,53504,300,1035,1046,1000,1001,1002,3076,3077,3089,3099,8028,8029,8036,8038,3090,3091,3092,7035,4698,4673,5158,4720,4624,4625,4648,4616,4670,1102,4624,4625,4663]
    proc_set = []
    reg_RECmd_set = ['Run', 'Command', 'Service']
    reg_services_set = ['']
    chain_number = 1

    time = find_chain.connect_chain(dbname) # 체인의 시작 시간, 종료 시간을 받아옴

    while time: # 체인 형성 가능
        start_time = time[0] # 체인 시작 시점
        end_time = time[1] # 체인 종료 시점
        

        sql.insert_chain_art(dbname, [chain_number]+list(time[2])) # 체인 시작 기준 아티팩트
        if time[3]:
            sql.insert_chain_art(dbname, [chain_number]+list(time[3])) # 체인 종료 기준 아티팩트

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
            time = find_chain.connect_chain(dbname, end_time+datetime.timedelta(milliseconds=100)) # 체인이 형성되었다면 해당 체인 이후로부터 생성
        else:
            basetime = start_time+datetime.timedelta(seconds=1)
            time = find_chain.connect_chain(dbname, basetime) # 체인이 형성되지 않았다면 시작 아티팩트 직후부터 다시 찾기

        chain_number += 1

    return None