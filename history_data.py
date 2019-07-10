#!/usr/bin/env python
# coding：utf-8

import pandas.io.sql as sql
import pandas as pd
from pandas.tseries.offsets import Day
## 选取近50天的数据
def history_data(table,TaskStartTime,conn):
   ## 注意TaskStartTime的数据类型
	TaskStartTime_start = pd.to_datetime(TaskStartTime) - Day(90)
	print(TaskStartTime_start,TaskStartTime)
	history_data = sql.read_sql('select DeviceName,Data2, Data1,PatrolTime,DeviceRegion,DeviceType,IntervalName,TaskStartTime,LineName from ' + str(table) + ' where (PatrolTime >=' + '\''+str(TaskStartTime_start)+'\''+ 'and PatrolTypeID = 1) ORDER BY TaskStartTime DESC',conn)
	return history_data