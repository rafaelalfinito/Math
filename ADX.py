import pandas as pd
import numpy as np
import BMF_treatdata
from datetime import datetime, timedelta

s = '2016-12-1 00:00:00'
period_minutes = 10
assetname = 'DOLF17'
data_frame_full_day = BMF_treatdata.data_into_dataframe(2016, 12, 1, assetname)
time = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

#
# time = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
# time += timedelta(minutes=period_minutes)
# data_frame = data_frame[data_frame['Trade Time'] = + period]

DI_index = []
for n in range(0, int(24 * 60 / period_minutes), 1):
    start_time = time + (n) * timedelta(minutes=period_minutes)
    end_time = time + (n + 1) * timedelta(minutes=period_minutes)
    print('****************************')
    print(str(start_time) + ' to ' + str(end_time))
    print('****************************')
    data_frame_full_day['ts'] = pd.to_datetime((data_frame_full_day['Trade Time']))
    data_frame_full_day.ts = pd.to_datetime(data_frame_full_day.ts)
    data_frame_period = data_frame_full_day[
        data_frame_full_day.ts.dt.strftime('%H:%M:%S').between(str(start_time.time()), str(end_time.time()))]

    high = data_frame_period.max()['Trade Price']
    low = data_frame_period.min()['Trade Price']
    close = 0
    DI_index.append([start_time, end_time, high, low, close])
    print(DI_index)