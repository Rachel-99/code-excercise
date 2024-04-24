import logging as log

def configure_logger():
    log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s: %(levelname)s [%(filename)s: line %(lineno)s] %(message)s',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        log.FileHandler('logs.log'),
                        log.StreamHandler()
                    ])
    return log.getLogger(__name__)