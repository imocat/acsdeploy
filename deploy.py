#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from json import dumps
from acsdeploy import ACSDeploy
from time import time
from optparse import OptionParser


def main():
    appDir = os.path.dirname((os.path.abspath(sys.argv[0])))
    configPath = 'config.json'

    os.chdir(appDir)

    parser = OptionParser(usage="usage: %prog [options]")

    parser.add_option("-c", "--config",
                      action="store",
                      type='string',
                      default=configPath,
                      help="config.json path"
                      )

    parser.add_option("-p", "--project",
                      action="store",
                      type='string',
                      default=None,
                      help="project name"
                      )

    parser.add_option("-a", "--app",
                      action="store",
                      type='string',
                      default=None,
                      help="app name"
                      )

    parser.add_option("-e", "--env",
                      action="store",
                      type='string',
                      default='test',
                      help="environment"
                      )

    parser.add_option("-f", "--file",
                      action="store",
                      type='string',
                      default='docker-compose.yml',
                      help="docker-compose.yml"
                      )

    parser.add_option("-m", "--publish_method",
                      action="store",
                      type='string',
                      default='',
                      help="publish method: standard or blue-green"
                      )

    (options, args) = parser.parse_args()

    if options.project == None or options.file == None or options.env == None or options.app == None:
        parser.print_help()
        exit(1)

    project = ACSDeploy(options.config,options.project, options.env)
    print project.deploy(options.app, '', options.publish_method, options.file)

if __name__ == '__main__':
    main()
