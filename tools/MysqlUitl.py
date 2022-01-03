import pymysql

from tools.Yaml_read import Yaml_read

sql=Yaml_read("sql.yaml")

class Mysql:
    def __init__(self,host=sql["ip"],user=sql["account"],password=sql["password"],database=sql["database"],port=sql["port"],charset="utf8"):
        """
        :param host:  数据库的地址
        :param user:  数据库账号
        :param password: 密码
        :param database: 方法哪个数据库
        :param port:  数据库端口  默认3306
        :param charset:  字符集
        :param self.cursor 字典类型
        :param self.conn.cursor(cursor=pymysql.cursors.DictCursor)   #获取执行sql的光标对象  cursor=pymysql.cursors.DictCursor  把输入结果更改为字典格式
        """
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset = charset,
            port = port
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def fetchone(self,sql):
        """
        单个查询
        :param sql: #执行sql语句
        :return:     #返回一天查询出来的数据
        execute(sql) 执行sql语句
        fetchone()   只返回一条记录
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchalll(self,sql):
        """
        多个查询
        :param sql: #执行sql语句
        :return:#返回查询出来的所以数据
        execute(sql) 执行sql语句
        fetchall()     返回查询出来的所有记录
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self,sql):
        """
        执行SQL语句是否成功；
        成功返回ture
        失败返回false
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    def __del__(self):
        """
        __del__方法会自动关闭
        #关闭光标对象cursor
        #关闭连接对象conn
        """
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

def mysql_inquire(sql):
    """
    数数据语句执行
    :param sql:
    :return:
    """
    return  Mysql().fetchalll(sql)

def Verify_database_data(sql, fields,comparison_data):
    """
    数据库核对数据
    :param sql:  查询sql语句
    :param fields:  需要查询的字段
    :param comparison_data: 对比的数据
    :return:
    """
    data =mysql_inquire(sql)
    for x in range(len(data)):
        if data[x][fields] == comparison_data:
            return data[x]

if __name__ == '__main__':
    # data = Verify_database_data("select * from zt_product","deleted","0")["id"]
    # print(data)
    print(Verify_database_data("select * from zt_project","id",1)["id"])

    #print(mysql_inquire("select * from  zt_user "))






