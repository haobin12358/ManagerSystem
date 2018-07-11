# *- coding:utf8 *-
import datetime
import re
"""
统一日期交互格式 
存进数据是 20180414182524
传给前端是 2017-08-06 12:35:26
"""
fomat_for_db = '%Y%m%d%H%M%S'
fomat_for_web_second = '%Y-%m-%d %H:%M:%S'
re_fomat_for_web = r"^\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$"
fomat_forweb_no_second = '%Y-%m-%d %H:%M'
format_forweb_no_HMS = "%Y-%m-%d"


class TimeManager(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TimeManager, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        pass

    @staticmethod
    def get_db_time_str(time_info=None):
        if time_info:
            if re.match(re_fomat_for_web, time_info):
                return datetime.datetime.strptime(time_info, fomat_for_web_second).strftime(fomat_for_db)
            else:
                return datetime.datetime.strptime(time_info, fomat_forweb_no_second).strftime(fomat_for_db)
        return datetime.datetime.now().strftime(fomat_for_db)

    @staticmethod
    def get_web_time_str(time_str, formattype=fomat_for_web_second):
        return datetime.datetime.strptime(time_str, fomat_for_db).strftime(formattype)
