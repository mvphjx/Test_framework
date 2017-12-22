from test.case.test_baidu_6 import TestBaiDu
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.config import REPORT_PATH
from utils.mail import Email

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试框架', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
    e = Email(title='捺印测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='511572653@qq.com',
              server='smtp.qq.com',
              sender='511572653@qq.com',
              password='lhmeizhxzqmvbjge',
              path=report
              )
    e.send()
