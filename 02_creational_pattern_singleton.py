'''
Тип: 
    Пораждающий паттерн.
Используется когда:
    - нужна отдна точка входа (БД, справочники);
    - необходим только один экземпляр.
'''

# ___________________________________________________________________

''' Догматическое написание Singleton'''

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance 

# ___________________________________________________________________

class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class DataBaseConnection(metaclass=SingletonMeta):
    connection_count = 0

    def __init__(self):
        self.connection_count += 1


# d1 = DataBaseConnection()
# print (f"Connection count: {d1.connection_count}")
# d2 = DataBaseConnection()
# print (f"Connection count: {d2.connection_count}")

# ___________________________________________________________________

import logging
import sys

class MyLogger(object, metaclass=SingletonMeta):
    _logger = None

    def __new__(cls):
        logging.basicConfig(format="%(asctime)s %(filename)s %(funcName)s %(message)s", level=logging.INFO)
        cls._logger = logging.getLogger()
        return cls._logger

logger = MyLogger()
logger.info("!!!!!! SOME TEXT !!!!!!!!")
print (id(logger))

logger1 = MyLogger()
logger.info("BOOOOOOO") 
print (id(logger1))