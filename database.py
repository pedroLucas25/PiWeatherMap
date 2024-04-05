from typing_extensions import Self
import pymysql.cursors
from config import Config
#from sqlalchemy import create_engine
import os

class Database:

    connection = None
    cursor = None

    def open(self):
        try:
            if os.environ['ENVIRONMENT'] == 'local':
                self.connection = pymysql.connect(host=Config.local_db_host,
                                                    db=Config.local_db,
                                                    user=Config.local_db_user,
                                                    password=Config.local_db_password,
                                                    cursorclass=Config.cursorclass,
                                                    charset=Config.charset,
                                                    autocommit=Config.autocommit)
            elif os.environ['ENVIRONMENT'] == 'development':
                self.connection = pymysql.connect(unix_socket=Config.development_db_host,
                                                    db=Config.development_db,
                                                    user=Config.development_db_user,
                                                    password=Config.development_db_password,
                                                    cursorclass=Config.cursorclass,
                                                    charset=Config.charset,
                                                    autocommit=Config.autocommit)
            elif os.environ['ENVIRONMENT'] == 'homolog':
                self.connection = pymysql.connect(unix_socket=Config.homolog_db_host,
                                                    db=Config.homolog_db,
                                                    user=Config.homolog_db_user,
                                                    password=Config.homolog_db_password,
                                                    cursorclass=Config.cursorclass,
                                                    charset=Config.charset,
                                                    autocommit=Config.autocommit)
            elif os.environ['ENVIRONMENT'] == 'production':
                self.connection = pymysql.connect(unix_socket=Config.production_db_host,
                                                    db=Config.production_db,
                                                    user=Config.production_db_user,
                                                    password=Config.production_db_password,
                                                    cursorclass=Config.cursorclass,
                                                    charset=Config.charset,
                                                    autocommit=Config.autocommit)

            self.cursor = self.connection.cursor()
            return self.cursor

        except Exception as e:
            print(e)
            return None

    def close(self):
        if self.cursor != None:
            self.cursor.close()

        if self.connection != None:
            self.connection.close()

class DatabaseAlchemy:
    
    connection = None
    cursor = None

    def open(self):
        try:
            if os.environ['ENVIRONMENT'] == 'local':
                self.connection = "mysql+pymysql://{}:{}@{}/{}".format(Config.local_db_user, 
                                                               Config.local_db_password, 
                                                               Config.local_db_host, 
                                                               Config.local_db)
            elif os.environ['ENVIRONMENT'] == 'development':
                self.connection = "mysql+pymysql://{}:{}@{}/{}".format(Config.development_db_user, 
                                                               Config.development_db_password, 
                                                               Config.development_db_host, 
                                                               Config.development_db)
            elif os.environ['ENVIRONMENT'] == 'homolog':
                self.connection = "mysql+pymysql://{}:{}@{}/{}".format(Config.homolog_db_user, 
                                                               Config.homolog_db_password, 
                                                               Config.homolog_db_host, 
                                                               Config.homolog_db)
            elif os.environ['ENVIRONMENT'] == 'production':
                self.connection = "mysql+pymysql://{}:{}@{}/{}".format(Config.production_db_user, 
                                                               Config.production_db_password, 
                                                               Config.production_db_host, 
                                                               Config.production_db)

                
        except Exception as e:
            print(e)
            return None        

        #return create_engine(self.connection, echo=False) #echo=True para verificar o que está sendo enviado ao banco

    def close(self):

        return None