# 环境


## 技术栈概述
- Python 3.6  （编程语言）
   [Python入门](https://www.imooc.com/learn/177) [python进阶](https://www.imooc.com/learn/317)
- selenium 3.8 （界面测试的插件）
- PyYaml (解析yml的插件)
- xlrd (解析excel的插件)
- requests (接口测试的插件)
- JMESPath  (JMESPath is a query language for JSON.)
- Faker (The Python tool to generate localized random data)
- HTMLTestRunner （生成测试报告）


## 项目结构概述
- config支持yml配置文件
- data 支持Excel的数据导入
- docs 相关学习文档
- driver 使用selenium进行浏览器自动化测试，所需要的驱动
- log 日志文件
- report 生成的测试报告
- test 主目录，包含接口测试 ui测试
- utils 工具类 包含一些测试/项目使用的小工具。例如 yml  Excel文件解析，发送邮件，之后按需扩充
- learn and try 学习/尝试写一些不成熟的工具
    例如 python_book_src为 《Python入门》源代码[最初版本源代码](https://github.com/ehmatthes/pcc) 



## 测试概述
- 测试只能证明程序是有错的，但不能证明软件是没有错误的。
- 不能只是一味地添加基于界面的自动化测试，而是需要对软件的自动化测试进行设计。
- 所以需要根据实际情况：测试的成本，测试的效率，缺陷定位的难易，体现实际业务。来制定测试分层。
- 测试计划，技术不是瓶颈，难点是各方协调，ROI才是王道。
#### 基于阶段分类（测试金字塔）
     
- 单元测试
- 接口测试
- 界面自动化测试
     
#### 基于测试目的分类...我也不太清楚
- 正确性测试: 
> 1 白盒测试 2 黑盒测试

- 性能测试
    
- 可靠性测试: 
> 1强壮性测试 2强壮性测试 3负载测试
    
- 安全性测试
    
    
    
[样式说明](https://www.cnblogs.com/liugang-vip/p/6337580.html)    


