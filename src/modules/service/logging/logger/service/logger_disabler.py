import uvicorn


class LoggerDisabler:

    @staticmethod
    def disable_uvicorn_logging():
        log_config = dict(uvicorn.config.LOGGING_CONFIG)
        log_config["loggers"]["uvicorn"] = {"handlers": []}
        log_config["loggers"]["uvicorn.error"] = {"handlers": []}
        log_config["loggers"]["uvicorn.access"] = {"handlers": []}
