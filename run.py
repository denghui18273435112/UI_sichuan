import pytest
from config.path import *
if __name__ == "__main__":
    pytest.main([  "-s", "./testcase/role_province/test_all.py",
                   "-s", "./testcase/role_association/test_all.py",
                   "-s", "./testcase/account_login/test_all.py",
                   "-m", "test",
                   "--maxfail=1",
                  "--alluredir", result_path])
    # os.system("allure generate {0} -o {1} --clean".format(result_path, allure_report_path))
    # os.system("allure serve {}".format(result_path))
    # 测试环境

