import logging
import sys


def get_logger(name="debug"):
    file_handler = logging.FileHandler(filename=f"./logs/{name}.log", encoding="utf-8")
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)

    handlers = [file_handler, stream_handler]
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
        handlers=handlers,
    )

    logger = logging.getLogger()

    return logger
