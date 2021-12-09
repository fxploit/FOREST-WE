import csv
import os


path = r'C:\Users\lee\Desktop\문서\공부\BoB\프로젝트\parser\test\kape_test1'

os.chdir(path)

count = 0

a = 0 

with open('result.csv','w', encoding='UTF-8') as fp:
    wr = csv.writer(fp)
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if '.csv' in file[-4:]:
                try:
                    with open(root + '\\' + file, 'r', encoding='UTF-8') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            wr.writerow([root+'\\'+file]+row)
                            a+=1
                            if(a==2):
                                a=0
                                break
                            
                except Exception as ex:
                    print('\nerror occured : ' + root+'\\'+file)
                    print(ex)
                    count+=1


print(count)





# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import os

# buf = []

# os.chdir(r'C:\Users\lee\Desktop\문서\공부\BoB\프로젝트\parser\test\kape_test')


# for root, dirs, files in os.walk(os.getcwd()):
#     for file in files:
#         try:
#             if '.csv' in file:
#                 print(str(root+'\\'+file))
#                 df = pd.read_csv(str(root + '\\' + file))
#                 buf.append(df.loc[0, :])
#         except:
#             print("exception occured : " + root + '\\' + file)

# print(buf)