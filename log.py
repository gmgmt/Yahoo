import logging
import time

class Log(object):
    ''' '''
    def __init__(self,name):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='../logs/%s.log'%(name),
                            filemode='a')

    def info(self, msg):
        logging.info(msg)

    def error(self, msg):
        logging.error(msg)

    def debug(self, msg):
        logging.debug(msg)

