import logging
logging.basicConfig(
filename ='app.log',
filemode = 'w',
level = logging.DEBUG,
FORMAT = '%(asctime)s -%(name)- %(levelname)s - %(message)s',
datfmt = '%Y-%m-%d %H:%M:%S'
)