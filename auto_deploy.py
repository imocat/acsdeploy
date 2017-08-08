#!/usr/bin/env python
# encoding: utf-8

import os
import sys


def main():

    if len(sys.argv) < 2:
        print('Usage: %s [file path]' % (sys.argv[0]))
        exit(1)

    projectName = os.getenv('PROJECT') or None
    appName = os.getenv('APP_NAME') or None
    envName = os.getenv('ENV') or None

    if projectName == None or appName == None or envName == None:
        print('environment variables PROJECT/APP_NAME/ENV required')
        exit(0)

    appName = appName.replace('/','-').upper()

    appDir = os.path.dirname((os.path.abspath(sys.argv[0]))) or None

    projectDir = sys.argv[1] or None
    dockerComposeYamlFiles = []

    if not os.path.exists(projectDir):
        print('%s not exists' % projectDir)
        exit(1)

    for dirs, root, files in os.walk(projectDir):
        break

    for file in files:
        if file == 'docker-compose.yml':
            # if file.find('.yml') != -1 or file.find('.yaml') != -1:
            dockerComposeYamlFiles.append(os.path.join(projectDir, file))

    for yamlFile in dockerComposeYamlFiles:
        cmd = 'python %s/deploy.py --project %s --app %s --env %s --file %s' % (
            appDir, projectName, appName, envName, yamlFile)

        print(cmd)
        if os.system(cmd) != 0:
            exit(1)

if __name__ == '__main__':
    main()
