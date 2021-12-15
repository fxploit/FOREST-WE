import csv
import sql
import glob
import tqdm

def collect_LogFiles(module_dst_path, dbname):
    paths = module_dst_path+'\\FileSystem\\NLT_LogFile*'
    paths = glob.glob(paths)

    for path in paths:
        with open(path, 'r', encoding='euc-kr') as f:
            reader = csv.reader(f)
            for row in tqdm(reader):
                try:
                    sql.insert_LogFile(dbname, ([row[i] for i in range(len(row))]))
                except:
                    continue