# -*- coding: utf-8 -*-
"""
        -------------------------------------------------
           @File Name：     run_test.py
           @Description :
           @Author :       kevin
           @Email:  1545810883@qq.com
           @Date：          2018/12/20
        -------------------------------------------------
           Change Activity:
                           2018/12/20:
        -------------------------------------------------
 """
__author__ = 'kevin'

import unittest
from testcases.test_register import TestRegister
from testcases.test_recharge import TestRecharge
from common import contants
from common.HTMLTestRunnerNew import HTMLTestRunner
from common.send_email import SendEmail


# 实例化suite和loader
suite = unittest.TestSuite()
loader = unittest.TestLoader()
# 添加case到suite
# suite.addTest(loader.loadTestsFromTestCase(TestRegister))
# suite.addTest(loader.loadTestsFromTestCase(TestRecharge))
discover = unittest.defaultTestLoader.discover(contants.case_dir,pattern='test*.py',top_level_dir=None)
# 执行测试
with open(contants.report_file, 'wb+') as file:
    runner = HTMLTestRunner(file)
    runner.run(discover)
SendEmail().send_email("wenguosheng@iwhere.com",contants.report_file)





