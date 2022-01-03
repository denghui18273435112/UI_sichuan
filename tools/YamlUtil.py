import os

import yaml


class YamlReaber:
                                                        #先初始化；文件是否存在
    def __init__(self,yamlfile):                        #yamlfile 文件名
        if os.path.exists(yamlfile):                    #判断yamlfile文件是否存在； os.path.exists 文件存不存在
            self.yamlfile =yamlfile                     #存在赋值给 self.yamlfile
        else:
            raise FileNotFoundError("文件不存在")       #不存在就是提示
        self._data = None
        self._data_all = None

    def data(self):
        """
        读取单个文档
        yaml文件名称在初始化中
        :return: yaml文件中的所有内容
        """
        if not self._data:                          #如果_all不为空,直接返回之前保存的数据
            with open(self.yamlfile,"rb") as f:     #打开文件
                self._data = yaml.safe_load(f)      #使用yaml方法读取;方法safe_load() 读取单个文档；
        return  self._data

    def data_all(self):
        """
        读取多个文档
         yaml文件名称在初始化中
        :return: yaml文件中的所有内容
        """
        if not self._data_all:                                #如果_all不为空,直接返回之前保存的数据
            with open(self.yamlfile,"rb") as f:              #打开文件
                self._data_all = list(yaml.safe_load_all(f))  #使用yaml方法读取;多个文档则用safe_load_all()
        return  self._data_all


def Yaml_file_pathS(Yaml_name, filePath="config"):
    """
    :param Yaml_name：yaml的文件夹名称
    :param filePath: 默认configs文件夹下
    :return: 返回当前yaml文件的绝对路径+文件名称
    """
    current =os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(os.path.dirname(current))

    _config_path= BASE_DIR +os.sep+filePath
    return _config_path +os.sep+Yaml_name



