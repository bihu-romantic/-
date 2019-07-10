#!/usr/bin/env python
# coding: utf-8

import pymssql
import pandas.io.sql as sql
def new_data(table,conn):
	TaskStartTime = sql.read_sql('select top 1 * from ' + str(table) + ' where PatrolTypeID = 1 order by TaskStartTime desc',conn)
   
	TaskStartTime_object = TaskStartTime['TaskStartTime'].astype('object')
	## 日期转字符串
	TaskStartTime_str = TaskStartTime_object.values[0]
	## 注意字符串类型的写法
	print(TaskStartTime_str)
	new_data = sql.read_sql('select DeviceName,Data2, Data1,PatrolTime,DeviceRegion,DeviceType,IntervalName,TaskStartTime,LineName from ' + str(table) + ' where TaskStartTime = ' + '\''+str(TaskStartTime_str)+'\''+ ' and PatrolTypeID = 1',conn)
	return TaskStartTime_str,new_data