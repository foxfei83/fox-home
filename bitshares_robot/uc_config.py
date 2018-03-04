import logging

# 配置日志文件和日志级别
# logging.basicConfig(filename='log/logger.log', level=logging.DEBUG)

# create logger
global logger
logger = logging.getLogger('bts_robot_logger')

# set default log level
logger.setLevel(logging.INFO)

# set logging file and level
ch = logging.FileHandler('log/logging.log')
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

