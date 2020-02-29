import logging


class Log:
    def __init__(self, logger_name, level="info"):
        self._log_levels = {
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "critical": logging.critical
        }

        log_level = self._log_levels.get(level, logging.INFO)
        logger = logging.getLogger(logger_name)
        logger.setLevel(level=log_level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        self._logger = logger
        self._logger_name = logger_name
        self._handlers = {"console": handler}
        self._formatter = formatter

        self.import_log_funcs()

    def add_file_output(self, filename: str, mode="a"):
        if filename not in self._handlers:
            handler = logging.FileHandler(filename, mode=mode)
            handler.setFormatter(self._formatter)
            self._handlers[filename] = handler
            self._logger.addHandler(handler)

    def import_log_funcs(self):
        log_funcs = [
            'debug', 'info', 'warning', 'error', 'critical'
        ]

        for func_name in log_funcs:
            func = getattr(self._logger, func_name)
            setattr(self, func_name, func)


if __name__ == '__main__':
    log = Log('simple_log', level="debug")
    log.add_file_output("foo.txt", mode="w")
    log.info('This is a log info')
    log.debug('Debugging')
    log.warning('Warning exists')
    log.error("An error occurs")
    log.critical("Critical")
    log.info('Finish')
