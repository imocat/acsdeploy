#!/usr/bin/env python
# encoding: utf-8


import json
import time
import yaml
from datetime import datetime
from ACSAgent import ACSAgent
import os


class ACSDeploy:

    def __init__(self, configPath, projectName, env):
        self.configs = self.loadConfig(configPath)

        self.projectName = projectName
        self.env = env

        if self.configs.has_key(self.projectName) and self.configs[self.projectName].has_key(self.env):
            projectConfig = self.configs[self.projectName][self.env]

            caFilePath = projectConfig['ca']
            certFilePath = projectConfig['cert']
            keyFilePath = projectConfig['key']

            self.checkFileExists(caFilePath)
            self.checkFileExists(certFilePath)
            self.checkFileExists(keyFilePath)

            print('''
Cluster: %s
Environment: %s
''' % (self.projectName, self.env) )

            self.agent = ACSAgent(
                projectConfig['masterUrl'],
                ca=caFilePath,
                cert=certFilePath,
                key=keyFilePath
            )
        else:
            raise Exception('Project or environment not exists: %s, %s' %
                            (self.projectName, self.env))

    def checkFileExists(self, filePath):
        if not os.path.exists(filePath):
            raise Exception('File not exists: %s' % (filePath))

    def loadConfig(self, configPath):
        self.checkFileExists(configPath)
        return json.load(open(configPath, 'r'))

    def appName(self, appName):
        return appName.upper()

    def loadYaml(self, yamlPath):
        self.checkFileExists(yamlPath)
        return yaml.load(open(yamlPath, 'r'))

    def getApps(self):
        '''
        获取当前容器集群应用列表
        '''
        return self.agent.getApps()

    def getApp(self, appName):
        '''
        获取应用详情
        '''
        appName = self.appName(appName)
        return self.agent.getApp(appName)

    def createApp(self, appName, version, updateMethod, dockerComposePath):
        '''
        创建应用
        '''
        appName = self.appName(appName)
        return self.agent.createApp(appName, version, updateMethod, dockerComposePath)

    def updateApp(self, appName, version, updateMethod, dockerComposePath):
        '''
        更新应用
        '''
        appName = self.appName(appName)
        return self.agent.updateApp(appName, version, updateMethod, dockerComposePath)

    def deploy(self, appName, version, updateMethod, dockerComposePath):
        '''
        部署服务（创建或更新）
        '''
        success, app = self.getApp(appName)

        # 自动生成版本号码
        if version == None or version == '':
            dt = datetime.now()
            version = dt.strftime('%Y%m%d_%H%M%S')

        # 默认标准发布方式
        if updateMethod == None or updateMethod == '':
            updateMethod = 'rolling'

        # 应用不存在时，创建新应用
        if success == False:
            print('Create %s to version %s' % (appName, version))
            return self.createApp(appName, version, updateMethod, dockerComposePath)
        else:
            print('Update %s to version %s' % (appName, version))
            return self.updateApp(appName, version, updateMethod, dockerComposePath)

    def removeApp(self, appName):
        '''
        删除应用
        '''
        appName = self.appName(appName)
        return self.agent.removeApp(appName)

    def killApp(self, serviceName):
        '''
        删除应用
        '''
        return self.agent.killService(serviceName)

    def startApp(self, appName):
        '''
        启动应用
        '''
        appName = self.appName(appName)
        return self.agent.startApp(appName)

    def stopApp(self, appName):
        '''
        停止应用
        '''
        appName = self.appName(appName)
        return self.agent.stopApp(appName)

    def getServices(self):
        '''
        获取当前集群服务列表
        '''
        return self.agent.getServices()

    def getService(self, serviceName):
        '''
        获取服务详情
        '''
        return self.agent.getService(serviceName)

    def startService(self, serviceName):
        '''
        开始服务
        '''
        return self.agent.startService(serviceName)

    def stopService(self, serviceName):
        '''
        停止服务
        '''
        return self.agent.stopService(serviceName)

    def restartService(self, serviceName):
        '''
        重启服务
        '''
        return self.agent.restartService(serviceName)

    def killService(self, serviceName):
        '''
        删除服务
        '''
        return self.agent.killService(serviceName)

    def scaleService(self, serviceName, number):
        '''
        伸缩服务
        '''
        return self.agent.scaleService(serviceName, number)
