import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text, Float
from config import dbconfig as cfg

DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename, cfg.username, cfg.password, cfg.host, cfg.database, cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)
Base = declarative_base()
