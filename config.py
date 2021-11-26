from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

user_agent = config.get('Network and Connection', 'user_agent')
timeout = config.getint('Network and Connection', 'timeout')

input_file = config.get('Working Files', 'input_keywords')
output_file = config.get('Working Files', 'output_keywords')
log_file = config.get('Working Files', 'log_file')
