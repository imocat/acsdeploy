#!/usr/bin/env python

import json
from ACSAgent import ACSAgent


class ACSProject:

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
        return self.agent.getApps()

    def getApp(self, appName):
        appName = self.appName(appName)
        return self.agent.getApp(appName)

    def createApp(self, appName, version, updateMethod, dockerComposePath):
        appName = self.appName(appName)
        return self.agent.createApp(appName, version, updateMethod, dockerComposePath)

    def updateApp(self, appName, version, updateMethod, dockerComposePath):
        appName = self.appName(appName)
        return self.agent.updateApp(appName, version, updateMethod, dockerComposePath)

    def deploy(self, appName, version, updateMethod, dockerComposePath):
        err, app = self.getApp(appName)

        if not updateMethod:
            updateMethod = 'rolling'

        if err == False:
            return self.createApp(appName, version, updateMethod, dockerComposePath)
        else:
            return self.updateApp(appName, version, updateMethod, dockerComposePath)

    def removeApp(self, appName):
        appName = self.appName(appName)
        return self.agent.removeApp(appName)

    def startApp(self, appName):
        appName = self.appName(appName)
        return self.agent.startApp(appName)

    def stopApp(self, appName):
        appName = self.appName(appName)
        return self.agent.stopApp(appName)

    def getServices(self):
        return self.agent.getServices()

    def getService(self, serviceName):
        return self.agent.getService(serviceName)

    def startService(self, serviceName):
        return self.agent.startService(serviceName)

    def stopService(self, serviceName):
        return self.agent.stopService(serviceName)

    def restartService(self, serviceName):
        return self.agent.restartService(serviceName)

    def killService(self, serviceName):
        return self.agent.killService(serviceName)

    def scaleService(self, serviceName, number):
        return self.agent.scaleService(serviceName, number)
