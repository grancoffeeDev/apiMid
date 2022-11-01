from configparser import ConfigParser
from datetime import date, datetime
import psycopg2
from psycopg2.extras import RealDictCursor
import json

class Database:

    def __init__(self) -> None:
        self.cur = None
        self.conn = None
        pass
    
    def json_serial(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))
    
    def config(filename='connection/database.ini', section='mid'):
        
        parser = ConfigParser()
        parser.read(filename)
        
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    
    def connect(self):
        params = Database.config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            
    def close(self):
        self.cur.close()
        self.conn.close()
        
    def executar(self, query, params, method):
        retorno = {}

        if(method=='GET'):
            self.cur.execute(query)
            retorno = json.dumps(self.cur.fetchall(),indent=4, default=Database.json_serial)
        elif(method=='POST'):
            self.cur.execute(query, params)
            self.conn.commit()

        return retorno