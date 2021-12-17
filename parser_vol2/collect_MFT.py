import csv
import sql
import glob
from tqdm import tqdm

def collect_MFTs(module_dst_path, dbname):
    path = module_dst_path+'\\FileSystem\\*$MFT_Output.csv'
    path = glob.glob(path)[-1]
    
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in tqdm(reader):
            try:
                sql.insert_MFT(dbname, ([row[i] for i in range(len(row))]))
            except:
                continue