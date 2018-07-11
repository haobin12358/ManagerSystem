LOG_BASE = "{0}==========={1}==========={0}"
INFO = "info"
ERROR = "error"
DEBUG = "debug"


class LOG():

    def logprint(self, log_type, params, value):
        print(LOG_BASE.format(log_type, params))
        print(value)
        print(LOG_BASE.format(log_type, params))

    def info(self, params, value):
        self.logprint(INFO, params, value)

    def error(self, params, value):
        self.logprint(ERROR, params, value)

    def debug(self, params, value):
        self.logprint(DEBUG, params, value)
