#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging import getLogger, DEBUG
from logging.handlers import SysLogHandler

def send_test(host = 'localhost', port = 514):
    my_logger = getLogger('MyLogger')
    my_logger.setLevel(DEBUG)

    handler = SysLogHandler(address = (host, port))
    my_logger.addHandler(handler)

    my_logger.debug('Test send [debug]')
    my_logger.critical('Test send [critical]')

def main():
    send_test()
    print("sent")

if __name__ == "__main__":
    main()