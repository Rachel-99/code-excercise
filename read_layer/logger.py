import logging as log

log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: line %(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('errors.log'),
                    log.StreamHandler()
                ]
                )