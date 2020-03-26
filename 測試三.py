import pandas as pd
import numpy as np
def alltime(i, j, k):
    df_new = pd.DataFrame()
    df = pd.read_csv(f'G:/newcase/123ＣＤツリ｜ハウス-2012-2.csv', encoding="utf-8")
    df = df.values
    df_wait = np.reshape(df, (-1, 1), order='F')
    df_wait = pd.DataFrame(df_wait)  # 等待時間
    list = []
    time = pd.date_range(f'{j}/{x}/{y}/8:15', f'{j}/{x}/{y}/21:45', freq="30min")
    list.append(time)
    df_time = np.reshape(list, (-1, 1), order='C')
    df_time = pd.DataFrame(df_time)  # 時間
    df_new = df_new.append([df_time], ignore_index=False)
    df_new['wait time'] = df_wait
    df_facility = df_new.insert(2, column="facility", value="1")
    df_new = df_new.append(df_new)
    # print(df_new)
    df_new.to_csv('G:/test/disney.csv', index=False)
    print()
    print()
    print()
for i in range(0, 1):
    x = 1
    y = 1
    for j in range(2012, 2013):
        for k in range(2, 3):
            alltime(i, j, k)