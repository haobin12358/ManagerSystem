# *- coding:utf8 *-
import datetime
import re
"""
统一日期交互格式 
存进数据是 20180414182524
传给前端是 2017-08-06 12:35:26
"""
format_for_db = '%Y%m%d%H%M%S'
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
                return datetime.datetime.strptime(time_info, fomat_for_web_second).strftime(format_for_db)
            else:
                return datetime.datetime.strptime(time_info, fomat_forweb_no_second).strftime(format_for_db)
        return datetime.datetime.now().strftime(format_for_db)

    @staticmethod
    def get_web_time_str(time_str, formattype=fomat_for_web_second):
        return datetime.datetime.strptime(time_str, format_for_db).strftime(formattype)

    @staticmethod
    def get_forward_time(**kwargs):
        return (datetime.datetime.now() + datetime.timedelta(**kwargs)).strftime(format_for_db)

    @staticmethod
    def get_forward_time_web(**kwargs):
        return (datetime.datetime.now() + datetime.timedelta(**kwargs)).strftime(fomat_for_web_second)

    @staticmethod
    def get_delta_time(starttime, endtime):
        deltatime = datetime.datetime.strptime(endtime, format_for_db) - datetime.datetime.strptime(starttime, format_for_db)
        hour, remainder = divmod(deltatime.seconds, 3600)
        minute, second = divmod(remainder, 60)
        # return deltatime
        return "{0}天{1}时{2}分{3}秒".format(deltatime.days, hour, minute, second)


if __name__ == "__main__":
    delta = TimeManager.get_delta_time("20170622001100", "20170722061100")
    print(delta)
    # print type(delta)



    # timestart = datetime.datetime.strptime("20170622001100", format_for_db)
    # timesend = datetime.datetime.strptime("20170623001100", format_for_db)
    # print(timestart)
    # print(timesend)
    # print(timesend - timestart)

    # print(TimeManager.get_forward_time(days=-1))

