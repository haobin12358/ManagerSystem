LOG_BASE = "{0}==========={1}==========={0}"
INFO = "info"
ERROR = "error"
DEBUG = "debug"
class LOG(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(LOG, cls).__new__(cls, *args, **kwargs)

    def logprint(self, type, params, value):
        print(LOG_BASE.format(type, params))
        print(value)
        print(LOG_BASE.format(type, params))

    def info(self, params, value):
        self.logprint(INFO, params, value)

    def error(self, params, value):
        self.logprint(ERROR, params, value)

    def debug(self, params, value):
        self.logprint(DEBUG, params, value)
