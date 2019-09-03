import logging


class Log:
    def __init__(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(level=logging.DEBUG)
        handler = logging.StreamHandler()
        formater = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'
        )
        handler.setFormatter(formater)
        logger.addHandler(handler)
        self.logger = logger

        self.import_log_funcs()

    def import_log_funcs(self):
        log_funcs = [
            'debug', 'info', 'warning', 'error', 'critical', 'exception'
        ]

        for func_name in log_funcs:
            func = getattr(self.logger, func_name)
            setattr(self, func_name, func)


if __name__ == '__main__':
    log = Log('simple_log')
    log.info('This is a log info')
    log.debug('Debugging')
    log.warning('Warning exists')
    log.info('Finish')
