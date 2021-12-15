import csv
import sql
import glob

def collect_UsnJrnls(module_dst_path, dbname):
    paths = module_dst_path+'\\FileSystem\\NLT_UsnJrnl*'
    paths = glob.glob(paths)

    for path in paths:
        with open(path, 'r', encoding='euc-kr') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    sql.insert_UsnJrnl(dbname, [row[i] for i in range(len(row))])
                except:
                    continue