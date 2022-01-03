# coding=utf-8
import os
import subprocess
from datetime import  datetime

from config import Conf
from config.Conf import *
from tools.Allure import alluer
from tools.AssertUitl import AssertUitl
from tools.MysqlUitl import Mysql
from tools.MysqlUitl import Verify_database_data


def init_db(db_alias='db_1'):
    """
    :param db_alias: # 默认db_1  数据库
    :return: sql的光标对象
    """
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host  = db_info["db_host"]
    user  = db_info["db_user"]
    password  = db_info["db_password"]
    database  = db_info["db_database"]
    port  = int(db_info["db_port"])
    charse  = db_info["db_charset"]
    conn =  Mysql(host,user,password,database,port,charse)
    return  conn


def time_YmdHMS(YmdHMS=True):
    """
    返回当前时间，支持两个格式
    True：%Y%m%d%H%M%S
    False：%Y%m%d
    :return:current_time
    """
    now_time = datetime.now()
    if YmdHMS:
        current_time = now_time.strftime("%Y%m%d%H%M%S")
    else:
        current_time = now_time.strftime("%Y%m%d")
    return   current_time


def allure_report(report_path,report_html):
    """
    自动生成allure 报告
    :param report_path: pytest.main运行 生成文件的存放位置
    :param report_html: allure生成报告存放位置
    :return:
    """
    allure_cmd ="allure generate %s -o %s --clean"%(report_path,report_html)
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        raise

def assert_db(db_name,result,db_verify):
    """
    数据库比较
    :param db_name:  数据库名称
    :param result:  返回的结果 body
    :param db_verify: sql语句
    :return:
    """
    assert_util =  AssertUitl()
    #sql = init_db("db_1")
    sql = init_db(db_name)
    # 2、查询sql，excel定义好的
    db_res = sql.fetchone(db_verify)

    #log.debug("数据库查询结果：{}".format(str(db_res)))
    # 3、数据库的结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        #res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)

def report_path(run_type):
    if run_type =="本地":
        return Conf.get_report_path() + os.sep + "result"
    if run_type =="jenkins":
        return Conf.get_report_path() + os.sep + "result"

def report_html_path(run_type):
    if run_type =="本地":
        return Conf.get_report_path() + os.sep + "allure_report"
    if run_type =="jenkins":
        return Conf.get_report_path() + os.sep + "allure_report"


def result_path():
    """
    设置报告的存放位置
    """
    return  get_report_path()+os.sep+"result"

def report_path():
    """
    设置报告的存放位置
    """
    return get_report_path()+os.sep+"allure_report"

def Judgment_Reporting(Data,sql,field_names,delete_data,delete_type=None):
    """
    :param Data: 读取的内容
    :param sql: sql语句
    :param field_names:判断的sql字段
    :param content: 输入的核心内容
    :return:
    """
    database = Verify_database_data(sql,field_names,delete_data)
    if delete_type==None:
        if database !=None:
            Data["database_judge"] = True
            Data["database_data"] = database
            Data["actual_result"] = "数据库判断成功"
        else:
            Data["database_judge"] = False
            Data["database_data"] = database
            Data["actual_result"] = "数据库判断失败"
        Data["expected_result"] = delete_data
        alluer(Data)

    elif  delete_type=="真删除":
        Data["delete_data"] = delete_data
        if  database == None:
            Data["database_judge"] = True
            Data["database_data"] = database
            Data["actual_result"] = "数据库真删除；数据库判断成功"
        Data["expected_result"] = delete_data
        alluer(Data)

    elif  delete_type=="假删除":
        Data["delete_data"] = delete_data
        if  database["deleted"] == "1":
            Data["database_judge"] = True
            Data["database_data"] = database
            Data["actual_result"] = "数据库假删除；数据库判断成功"
        Data["expected_result"] = delete_data
        alluer(Data)

if __name__ == '__main__':
    pass
    #print(init_db("db_1"))
    # print(res_find( '{"Authorization": "JWT ${token}$"}'))
    # print(res_sub( '{"Authorization": "JWT ${token}$"}',"123"))

