import datetime
import logging
import os

from config import Conf
from config.Conf import ConfigYaml

#定义日志级别的映射
log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR
}
class Logger:
                                                                             #2定义参数；想想需要有哪些參數；生成日志文件名称、Logger名称、日志级别
    def __init__(self,log_file,log_Logger_name,log_level):
        self.log_file = log_file                                            #扩展名；在配置文件写
        self.log_Logger_name = log_Logger_name                              #Logger名称，不在配置文件写
        self.log_level = log_level                                          #日志级别；在配置文件写
        self.logger_name = logging.getLogger(self.log_Logger_name)          #第一步：设置logger名称
        self.logger_name.setLevel(log_l[self.log_level])                    #第二步：设置log级别
        self.logger = logging.getLogger(self.log_Logger_name)               #第一步：设置logger名称
        self.logger.setLevel(log_l[self.log_level])                         #第二步：设置log级别
        if not self.logger_name.handlers:                                   #判断handler是否存在
            #输入文件
            print(self.log_file)
            fh_file = logging.FileHandler(self.log_file,encoding='utf-8')   #第三步：写入文件的handler
            fh_file.setLevel(log_l[self.log_level])                         #第四步：设置日志级别
            formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_file.setFormatter(formatter)                                 #第五步：定义格式
            self.logger_name.addHandler(fh_file)                            #第六步：添加handler

             # 输出控制台
            # fh_stream = logging.StreamHandler()
            # fh_stream.setLevel(log_l[self.log_level])
            # formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')
            # fh_stream.setFormatter(formatter)
            # self.logger.addHandler(fh_stream)


def generate_file():
    # """
    # #1、初始化参数数据
    # #日志文件名称、日志文件级别
    # #日志文件名称=log目录+当前时间+扩展名
    # #log目录; #当前时间;#扩展名
    # #合并（log目录+当前时间+扩展名）并创建*.log文件  logfile返回G:\pycharm\script\api_frame\logs\2020-04-07.log
    # :return:  生成的日志文件名称
    # """

    log_path = Conf.get_log_path()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    log_extensiong = ConfigYaml().get_conf_log_extensiong()
    logfile = os.path.join(log_path,current_time+log_extensiong)
    return logfile


def my_log(log_Logger_name = __file__):
    """
    打印日志的方法：支持输入到终端和日志文件中;只需要传入日志名称即可
    对方方法，初始log工具类，提供其它类使用
    :param log_Logger_name: log名称
    :return
        log_file            日志文件名称        generate_file() 方法获取文件名称
        log_level           日志文件级别        ConfigYaml().get_conf_log()  获取日志文件级别
        logger_name         logger名称
        log_Logger_name     日志文件打印部分  get_conf_log
    """
    return Logger(log_file=generate_file(),log_Logger_name=log_Logger_name,log_level=  ConfigYaml().get_conf_log()).logger_name

if __name__ == '__main__':
    my_log().debug("ss")





