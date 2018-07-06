# *- coding:utf8 *-
#  引用python类
from sqlalchemy.orm import sessionmaker
# 引用项目类
from models import model
import time
# 实例化session
db_session = sessionmaker(bind=model.mysql_engine)


def close_session(fn):
    def inner(self, *args, **kwargs):
        try:
            result = fn(self, *args, **kwargs)
            self.session.commit()
            return result
        except Exception as e:
            print("DBERROR" + e.message)
            self.session.rollback()
            raise Exception(e.message)
        finally:
            self.session.close()
    return inner


# service 基础类
class SBase(object):
    def __init__(self):
        try:
            self.session = db_session()
        except Exception as e:
            print(e.message)

    @close_session
    def add_model(self, model_name, **kwargs):
        print(model_name)
        if not getattr(model, model_name):
            print("model name = {0} error ".format(model_name))
            return False

        model_bean = eval(" model.{0}()".format(model_name))
        for key in model_bean.__table__.columns.keys():
            if key in kwargs:
                setattr(model_bean, key, kwargs.get(key))

        self.session.add(model_bean)
        return True

    @close_session
    def check_connection(self, index=0):
        if index > 3:
            raise Exception("mysql connection failed")
        try:
            self.session.execute("select 1")
            print("mysql connection successful")
        except Exception as e:
            print("mysql connection error:", e.message)
            self.check_connection(index + 1)
            time.sleep(3)
