## 环境


技术栈概述
- Python 3.6  （编程语言）
- selenium 3.8 （界面测试的插件）
- PyYaml (解析yml的插件)
- xlrd (解析excel的插件)
- requests (接口测试的插件)
- JMESPath  (JMESPath is a query language for JSON.)
- Faker (The Python tool to generate localized random data)
- HTMLTestRunner （生成测试报告）


项目结构概述
    1 config支持yml配置文件
    2 data 支持Excel的数据导入
    3 docs 相关学习文档
    4 driver 使用selenium进行浏览器自动化测试，所需要的驱动
    5 log 日志文件
    6 report 生成的测试报告
    7 test 主目录，包含接口测试 ui测试
    8 utils 工具类 包含一些测试/项目使用的小工具。例如 yml  Excel文件解析，发送邮件，之后按需扩充



测试概述
测试只能证明程序是有错的，但不能证明软件是没有错误的。
不能只是一味地添加基于界面的自动化测试，而是需要对软件的自动化测试进行设计。
所以需要根据实际情况：测试的成本，测试的效率，缺陷定位的难易，体现实际业务。来制定测试分层。
测试计划，技术不是瓶颈，难点是各方协调，ROI才是王道。
 1 基于阶段分类（测试金字塔）
       界面自动化测试
      ***接口测试***
    *****单元测试*****
 2 基于测试目的分类...我也不太清楚
    1)正确性测试
       a)白盒测试
       b)黑盒测试
    2)性能测试
    3)可靠性测试
       a)强壮性测试
       b)异常处理测试
       c)负载测试
    4)安全性测试

