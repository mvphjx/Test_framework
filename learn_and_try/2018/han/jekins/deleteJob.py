import jenkins

template_xml = "config.xml"
# 与网页版Jenkins登录的账号、密码一致
server = jenkins.Jenkins('http://localhost:8080/', username='admin', password='admin')

job_list = {
    "webtest": "webtest"
}
for spider_name, crontab in job_list.items():
    with open(template_xml) as f:
        profile = f.read()
    JOB_CONFIG = profile.replace("{{description}}", crontab)
    print(JOB_CONFIG[-200:])
    server.create_job(spider_name, JOB_CONFIG)
    # del_job=server.delete_job(view_name+name)
    # print(del_job)
