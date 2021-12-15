import sql
import find_chain


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

        columns = sql.select_eventlog(dbname, start_time, end_time, eventid_set)
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))
        
        columns = sql.select_prefetch(dbname, start_time, end_time, proc_set)
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))
        
        columns = sql.select_reg_RECmd(dbname, start_time, end_time, reg_RECmd_set)
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))
        chain_number += 1
        time = find_chain.connect_chain(dbname, end_time)

        columns = sql.select_reg_services(dbname, start_time, end_time, reg_services_set)
        for column in columns:
            sql.insert_chain_art(dbname, [chain_number] + list(column))

    return None