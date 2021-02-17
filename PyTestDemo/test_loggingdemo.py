import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)

    # it will invokes the files name in which we want to store the logs
    filehandler = logging.FileHandler("logfile.log")
    logger.addHandler(filehandler)
    # This will prepare log format
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    # Creation of link between the log formatter and file handler
    filehandler.setFormatter(formatter)
    logger.setLevel(logging.INFO)

    # Type of logs we can generate
    logger.debug("Debugging any module")
    logger.info("Information relatyed with any type")
    logger.warning("It will show any kind of warning messages")
    logger.error("error related with any execution")
    logger.critical("It will show any major error")
