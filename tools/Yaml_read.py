#-*- conding:utf-8 -*-
#@File      :Yaml_read.py
#@Time      : 10:21
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
from tools.YamlUtil import YamlReaber
from tools.YamlUtil import Yaml_file_pathS

def Yaml_read(yaml_name="conf.yaml", level_1=None, level_2=None, filePath=None, location=None):
    """
    支持yaml的单文档、多文档遍历
    :param yaml_name:  yaml的文件名称
    :param level_1: yaml文件第一级的名称
    :param level_2: yaml文件第二级的名称
    :param filePath:文件夹名称
    :param location:读取多个文档的下标
    :return:   1、支持返回所有的yaml文件；2、第一级下的所有数据；3、固定某位置的值
    """
    if filePath!=None:
        if location!=None:
            login = YamlReaber(Yaml_file_pathS(yaml_name,filePath)).data_all()
        else:
            login = YamlReaber(Yaml_file_pathS(yaml_name,filePath)).data()
    else:
        if location!=None:
            login = YamlReaber(Yaml_file_pathS(yaml_name)).data_all()
        else:
            login = YamlReaber(Yaml_file_pathS(yaml_name)).data()
    if level_1==None and level_2==None:
        if location!=None:
            return  login[location]
        else:
            return  login
    elif level_1!= None and level_2==None:
        if location!=None:
            return  login[location][level_1]
        else:
            return  login[level_1]
    elif level_1!=None and level_2!=None:
        if location!=None:
            return  login[location][level_1][level_2]
        else:
            return login[level_1][level_2]

if __name__ == '__main__':
    print(Yaml_read("all.yaml","student_details"))
