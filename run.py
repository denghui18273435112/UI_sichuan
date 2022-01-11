import pytest
from config.path import *
if __name__ == "__main__":
    try:
        for one in os.listdir(result_path):
            if "environment.properties" not in one:
                os.remove(result_path+os.sep+"{}".format(one))
        for one_2 in os.listdir(logs_path):
             if ".log" in one_2:
                os.remove(logs_path+os.sep+"{}".format(one_2))
        for one_1 in os.listdir(photo_path):
            if "_截图" in one_1:
                os.remove(photo_path+os.sep+"{}".format(one_1))
    except:
        print("\n>>没有可删除的文件>>\n")
    pytest.main([  "-s", "./testcase/role_province/test_all.py",
                   "-s", "./testcase/role_association/test_all.py",
                   "-s", "./testcase/account_login/test_all.py",
                    "-s", "./testcase/delete_data/test_all.py",
                   "-m", "not(login or no)",
                   #"-m", "test",
                   "--maxfail=1",
                  "--alluredir", result_path])
    # os.system("allure generate {0} -o {1} --clean".format(result_path, allure_report_path))
    # os.system("allure serve {}".format(result_path))
