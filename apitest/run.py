import os
import shutil

import pytest

if __name__ == '__main__':
    #pytest.main(['-s', '-v', '--alluredir=./report/temp', './testcase', '--clean-alluredir'])
    pytest.main(['-s', '-v', '--alluredir=./report/temp', './testcase/logistic/test_getMaterial.py', '--clean-alluredir'])
    shutil.copy('./environment.xml', './report/temp')
    os.system(f'allure serve ./report/temp')
