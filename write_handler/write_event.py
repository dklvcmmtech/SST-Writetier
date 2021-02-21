import mysql.connector
#import connect_db
from write_handler.connect_db import MySqlConn
#from connect_db1 import MySqlConn_1

a=10



class write_sql:

  def write_data(self,val1,val2):
    self.mysqlConnObj = MySqlConn()
    mysqlConnector = self.mysqlConnObj.mysql_conn
    cursor = mysqlConnector.cursor()
    try:
      query = "INSERT INTO pod_activities(pod_id, msg) VALUES("+"'"+val1+"'"+", "+"'"+val2+"'"+");"
      cursor.execute(query)
      mysqlConnector.commit()
      cursor.close()
    except Exception as e:
      return str(e)
    return "Success"
