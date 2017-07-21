#!/usr/bin/env python

from json import dumps
from acsdeploy.ACSProject import ACSProject
from time import time

if __name__ == '__main__':
    version = str(time())

    # project = ACSProject('./config.json', 'doupai', 'test')
    # print(help(project))

    # print project.deploy('test-web', version, 'blue-green', './test-web.yml')
    # print project.stopApp('test-web')
    # print project.startApp('test-web')
    # print project.getServices()
    # print project.getService('TEST-WEB_test-web')
    # print project.stopService('TEST-WEB_test-web')
    # print project.startService('TEST-WEB_test-web')
    # print project.restartService('TEST-WEB_test-web')
    # print project.scaleService('TEST-WEB_test-web',2)
