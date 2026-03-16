import logging
import os


def get_logger():

    logger = logging.getLogger("automation_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "automation.log")

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger