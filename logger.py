import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个StreamHandler，用于输出信息到控制台
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# 创建一个FileHandler，用于写入错误到文件
file_handler = logging.FileHandler('errors.log')
file_handler.setLevel(logging.ERROR)

# 定义日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将handlers添加到logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

