#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Ecrit par Gregory David
import sys
import logging
import toolbox.configuration as conf
import toolbox.cli
from toolbox.database import connection

if __name__ == "__main__":
    screenLoggerFormat = logging.Formatter('%(levelname)s:%(message)s')
    screenLoggerHandler = logging.StreamHandler(stream=sys.stderr)
    screenLoggerHandler.setFormatter(screenLoggerFormat)
    logging.getLogger().addHandler(screenLoggerHandler)

    if sys.version_info < conf.min_version_python :
        logging.critical("Python %i.%i is required" % (conf.min_version_python[0], conf.min_version_python[1]))
        sys.exit(255)

    command_line = toolbox.cli.CLI()
    command_line.performParsingCLI()

    if command_line.arguments.log_filename is not None:
        fileLoggerFormat = logging.Formatter('%(asctime)s %(filename)s(%(process)s) %(levelname)s:%(message)s')
        fileLoggerHandler = logging.FileHandler(command_line.arguments.log_filename)
        fileLoggerHandler.setFormatter(fileLoggerFormat)
        logging.getLogger().addHandler(fileLoggerHandler)

    logging.getLogger().setLevel(getattr(logging, command_line.arguments.log))
    logging.debug("Command line arguments:" + repr(command_line.arguments))
    logging.shutdown()
