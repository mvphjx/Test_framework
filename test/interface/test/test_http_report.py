from test.interface.test.test_http import TestHTTP
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.config import REPORT_PATH
if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='XXX测试接口', description='接口html报告')
        runner.run(TestHTTP('test_http'))
