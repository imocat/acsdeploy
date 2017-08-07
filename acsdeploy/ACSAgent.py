#!/usr/bin/env python
# encoding: utf-8

from json import dumps
from APIRequest import APIRequest


class ACSAgent(APIRequest):

    def getContents(self, path):
        f = open(path, 'r')
        content = f.read()
        f.close()
        return content

    def getApps(self):
        return self.get('/projects/')

    def getApp(self, appName):
        return self.get('/projects/%s' % appName)

    def stopApp(self, appName):
        return self.post('/projects/%s/stop?t=10' % (appName))

    def startApp(self, appName):
        return self.post('/projects/%s/start?t=10' % (appName))

    def killApp(self, appName):
        return self.post('/projects/%s/kill' % (appName))

    def createApp(self, appName, version, updateMethod, dockerCompose):
        templateData = self.getContents(dockerCompose)
        data = {
            "name": appName,
            "default_update_method": updateMethod,
            "version": version,
            "template": templateData,
            "latest_image": True
        }
        return self.post('/projects/', dumps(data))

    def updateApp(self, appName, version, updateMethod, dockerCompose):
        templateData = self.getContents(dockerCompose)
        data = {
            "name": appName,
            "default_update_method": updateMethod,
            "version": version,
            "template": templateData,
            "latest_image": True
        }
        return self.post('/projects/%s/update' % (appName), dumps(data))

    def removeApp(self, appName):
        return self.delete('/projects/%s' % (appName))

    def getServices(self):
        return self.get('/services/')

    def getService(self, serviceName):
        return self.get('/services/%s' % (serviceName))

    def startService(self, serviceName):
        return self.post('/services/%s/start' % (serviceName))

    def stopService(self, serviceName):
        return self.post('/services/%s/stop' % (serviceName))

    def restartService(self, serviceName):
        return self.post('/services/%s/restart' % (serviceName))

    def killService(self, serviceName):
        return self.post('/services/%s/kill' % (serviceName))

    def scaleService(self, serviceName, number):
        data = {
            "type": "scale_to",
            "value": number
        }
        return self.post('/services/%s/scale' % (serviceName), dumps(data))
