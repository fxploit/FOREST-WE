import sql
from datetime import timedelta
import datetime


def StrToDate(str_date):
    return datetime.datetime.strptime(str_date, r'%Y-%m-%d %H:%M:%S.%f')

def connect_chain(dbname, basetime=None, eventid_set=None):
    columns_start = []
    columns_end = []

    if basetime == None:
        columns_start = find_start_chain(dbname)
    else:
        columns_start = find_start_chain(dbname, basetime)

    if columns_start == None:
        return None

    start_time = StrToDate(columns_start[3])
    
    columns_end = find_end_chain(dbname, start_time, start_time+timedelta(seconds=60)) # 일단은 예시로 시작 시점부터 시작 시점 이후 1분 까지의 아티팩트 중 발견되는 모든 아티팩트 조사하게끔 함.
    
    if columns_end:
        end_time = StrToDate(columns_end[3])
        print("chain start point : {} and end point : {}".format(columns_start,columns_end))
    else:
        end_time = start_time+timedelta(seconds=60)
        print("chain start point : {} and end point is not founud".format(columns_start))
    
    return [start_time, end_time, columns_start, columns_end]
    

def find_start_chain(dbname, basetime=None):
    columns = sql.select_chain_start(dbname, basetime)
    if columns:
        return columns[0] # 체인을 시작할 수 있다면 반환
    else:
        return None # 더이상 체인 시작 단서가 없음



def find_end_chain(dbname, Start_Time, end_time):
    columns = sql.select_chain_end(dbname, Start_Time, end_time)
    if columns:
        return columns[0]
    else:
        return None
    
    