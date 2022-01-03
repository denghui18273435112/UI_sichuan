import os
import tools.YamlUtil

current =os.path.abspath(__file__)                          #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径
_config_path = BASE_DIR +os.sep+"config"                   #定义config的路径
_config_file = _config_path +os.sep+"conf.yaml"            #定义conf.yaml的路径
_yonglie_file = _config_path +os.sep+"yonglie.yaml"            #定义conf.yaml的路径
_db_config_file = _config_path +os.sep+"db_conf.yaml"     #定义db_conf.yaml的路径
_log_path = BASE_DIR +os.sep+"logs"                        #定义log文件生产路径
_data_path =BASE_DIR +os.sep+"docs"                        #定义data文件的路径
_report_path =BASE_DIR +os.sep+"report"                        #定义report文件的路径
_file_path =BASE_DIR +os.sep+"file"
_file_path_photo =_file_path +os.sep+"photo"
photo =_file_path +os.sep+"photo"

def Yaml_document_location(Yaml_name):
    current =os.path.abspath(__file__)                          #当前文件的路径
    BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径
    _config_path = BASE_DIR +os.sep+"config"                   #定义config的路径
    _yonglie_file = _config_path +os.sep+Yaml_name            #定义conf.yaml的路径
    return  _yonglie_file

def get_file_path():
    """
    :return: file文件夹的绝对路径
    """
    return  _file_path

def get_file_path_photo():
    """
    :return: photo文件夹的绝对路径
    """
    return  _file_path_photo

def get_report_path():
    """
    :return: report文件夹的绝对路径
    """
    return  _report_path

def get_config_path():
    """
    :return: config文件夹的路径
    """
    return  _config_path

def get_db_config_cpath():
    """
    :return: db_conf.yaml 文件所在的路径
    """
    return _db_config_file

def get_config_file():
    """
    :return: conf.yaml文件所在的路径
    """
    return  _config_file
def get_data_path():
    """
    :return: data文件夹所在路径
    """
    return _data_path
def get_log_path():
    """
    :return: logs文件夹的路径
    """
    return _log_path

def get_docs_path():
    """
    :return: docs文件的绝对路径
    """
    return  BASE_DIR +os.sep+"docs"



class ConfigYaml:
    def __init__(self):
        """
        #读取配置文件
        #创建类；初始化yaml读取配置文件；
        self.config return  遍历  get_config_file方法中conf.yaml文件的所有值
        self.config_all return 遍历   get_config_file方法中conf.yaml文件的所有值
        self.db_config  return 遍历   get_config_file方法中 db_conf.yaml文件的所有值
        :return:
        """
        self.config = tools.YamlUtil.YamlReaber(get_config_file()).data()

    def get_conf_log_extensiong(self):
        """
        :return: 文件的扩展名
        """
        return self.config["LOG"]["log_extensiong"]

    def get_conf_log(self):
        """
        :return: 日志级别
        """
        return self.config["LOG"]["log_level"]

    def read_yaml(self,yaml_name,a=None,b=None):
        """
        读取yaml文件中的数据
        :param yaml_name:  yaml的文件名称
        :param a: yaml文件第一级的名称
        :param b: yaml文件第二级的名称
        :return:   1、支持返回所有的yaml文件；2、第一级下的所有数据；3、固定某位置的值
        """
        self.login = tools.YamlUtil.YamlReaber(Yaml_document_location(yaml_name)).data()
        if a==None and b==None:
            return  self.login
        elif a!= None and b==None:
            return  self.login[a]
        elif a!=None and b!=None:
            return self.login[a][b]

    def get_email_info(self):
        """
        :param  获取eamil的相关信息
        :return:
        """
        return self.config["email"]

    def get_conf_url(self):
        """
        :return: url地址
        """
        return self.config["test_environment"]["url"]






#表格用例字段
test_id = "用例编号"
module = "模块"
name = "名称"
priority = "优先级"
back_name = "标题"
URL = "URL"
preposition = "前置条件"
table_data = "数据"
expected_result = "预期结果"
actual_result = "实际结果"






if __name__ == '__main__':
    #print(ConfigYaml().read_yaml("all_data.yaml","login"))
    print(get_file_path())








