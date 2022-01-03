import allure
from tools.Base import *
from tools.Yaml_read import Yaml_read


def alluer(inData):
        """
        :param inData 表格数据
        :return:
        """
        allure.dynamic.feature(inData["module"])
        allure.dynamic.story(inData["name"])
        #allure.dynamic.title(inData["标题"])
        allure.attach( "<font color='red' style='font-size: 20px;'>{}</font><Br/>".format(inData["data"]),"操作的数据",allure.attachment_type.HTML)
        desc = "<font color='red'>当前执行时间: </font> {}<Br/>" \
               "<font color='red'>用例ID: </font> {}<Br/>" \
               "<font color='red'>模块: </font>{}<Br/>" \
               "<font color='red'>名称: </font>{}<Br/>" \
               "<font color='red'>优先级: </font>{}<Br/>" \
               "<font color='red' >URL: </font>{}<Br/>"\
               "<font color='red' >前置条件: </font>{}<Br/>"\
               "<font color='red' >预期结果: </font>{}<Br/>"\
               "<font color='red' >实际结果: </font>{}<Br/>"\
               "<font color='red' >操作的数据: </font>{}<Br/>"\
            .format(
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    inData["test_id"],
                    inData["module"],
                    inData["name"],
                    inData["priority"],
                    Yaml_read("all_data.yaml","login")["joint_url"]+inData["URL"],
                    inData["preposition"],
                    inData["expected_result"],
                    inData["actual_result"],
                    inData["data"])
        allure.dynamic.description(desc)