#!/usr/bin/env python
# encoding: utf-8

import json
from ACSAgent import ACSAgent


class ACSDeploy:

    def __init__(self, configPath, projectName, env):
        self.configs = self.loadConfig(configPath)

        self.projectName = projectName
        self.env = env

        if self.configs.has_key(self.projectName) and self.configs[self.projectName].has_key(self.env):
            projectConfig = self.configs[self.projectName][self.env]

            print('''
project: %s
env: %s
''' % (self.projectName, self.env) )

            self.agent = ACSAgent(
                projectConfig['masterUrl'],
                ca=projectConfig['ca'],
                cert=projectConfig['cert'],
                key=projectConfig['key']
            )

    def loadConfig(self, configPath):
        return json.load(open(configPath, 'r'))

    def appName(self, appName):
        return appName.upper()

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
        err, app = self.getApp(appName)

        if not updateMethod:
            updateMethod = 'rolling'

        if err == False:
            return self.createApp(appName, version, updateMethod, dockerComposePath)
        else:
            return self.updateApp(appName, version, updateMethod, dockerComposePath)

    def removeApp(self, appName):
        '''
        删除应用
        '''
        appName = self.appName(appName)
        return self.agent.removeApp(appName)

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