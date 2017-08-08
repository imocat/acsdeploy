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
        print('Environment variables PROJECT/APP_NAME/ENV required')
        exit(0)

    appName = appName.replace('/','-').upper()

    appDir = os.path.dirname((os.path.abspath(sys.argv[0]))) or None

    projectDir = sys.argv[1] or None

    if not os.path.exists(projectDir):
        print('Not exists file [%s]' % projectDir)
        exit(1)

    for dirs, root, files in os.walk(projectDir):
        break

    # test.yml or stage.yml
    dockerComposeYamlFile = os.path.join(projectDir, '%s.yml' % (envName))
    
    if os.path.exists(dockerComposeYamlFile):
        cmd = 'python %s/deploy.py --project %s --app %s --env %s --file %s' % (
            appDir, projectName, appName, envName, dockerComposeYamlFile)

        print(cmd)
        if os.system(cmd) != 0:
            exit(1)
    else:
        print('Not found file [%s.yml], Skip deployment' % (dockerComposeYamlFile) )

if __name__ == '__main__':
    main()
