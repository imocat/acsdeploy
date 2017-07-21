# ACSDeploy

阿里云容器服务部署工具

# 使用说明

目录结构如下 

```bash
├── acsdeploy
│   ├── ACSAgent.py
│   ├── ACSProject.py
│   └── APIRequestClient.py
├── config.json
├── projectname
│   ├── production
│   │   ├── ca.pem
│   │   ├── cert.pem
│   │   └── key.pem
│   ├── stage
│   │   ├── ca.pem
│   │   ├── cert.pem
│   │   └── key.pem
│   └── test
│       ├── ca.pem
│       ├── cert.pem
│       └── key.pem
├── requirement.txt
├── test-projectname.py
└── test-web.yml
```

`config.json` 文件用来配置阿里云容器集群信息，内容如下  

```json
{
  "projectname": {
    "stage": {
      "cert": "projectname/stage/cert.pem",
      "key": "projectname/stage/key.pem",
      "masterUrl": "https://master123.cs-cn-beijing.aliyun.com:20012",
      "ca": "projectname/stage/ca.pem"
    },
    "production": {
      "cert": "projectname/production/cert.pem",
      "key": "projectname/production/key.pem",
      "masterUrl": "https://master123.cs-cn-beijing.aliyun.com:20012",
      "ca": "projectname/production/ca.pem"
    },
    "test": {
      "cert": "projectname/test/cert.pem",
      "key": "projectname/test/key.pem",
      "masterUrl": "https://master123.cs-cn-beijing.aliyun.com:20012",
      "ca": "projectname/test/ca.pem"
    }
  }
}
```

`test-projectname.py` 使用 acsdeplooy 部署服务到 test-projectname 集群，文件如下

```python
#!/usr/bin/env python

from json import dumps
from acsdeploy.ACSProject import ACSProject
from time import time

if __name__ == '__main__':
    version = str(time())

    project = ACSProject('./config.json', 'projectname', 'test')
    
    # print project.deploy('test-web', version, 'blue-green', './test-web.yml')
    # print project.stopApp('test-web')
    # print project.startApp('test-web')
    # print project.removeApp('test-web')
    # print project.getServices()
    # print project.getService('TEST-WEB_test-web')
    # print project.stopService('TEST-WEB_test-web')
    # print project.startService('TEST-WEB_test-web')
    # print project.restartService('TEST-WEB_test-web')
    # print project.killService('TEST-WEB_test-web')
    # print project.scaleService('TEST-WEB_test-web',2)
```
`test-web.yml` 为阿里云部署的 docker-compose.yml 文件，详情请查看阿里云容器服务编排说明文档

# 文档

### 应用操作

#### getApps
#### getApp
#### createApp
#### updateApp
#### removeApp
#### killApp
#### deployApp
#### startApp
#### stopApp

### 服务操作

#### getServices
#### getService
#### startService
#### stopService
#### restartService
#### killService
#### scaleService