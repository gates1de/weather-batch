from logging import getLogger, StreamHandler, INFO, ERROR

def instantiate_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setLevel(ERROR)
    logger = getLogger(__name__)
    logger.setLevel(INFO)
    logger.setLevel(ERROR)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
