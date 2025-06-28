import os
import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger with the specified name.
    
    Args:
        name (str): The name of the logger.
        
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    # Create a console handler and set its level to INFO
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create a file handler and set its level to DEBUG
    os.makedirs('logs', exist_ok=True)  # Ensure the logs directory exists
    fh = logging.FileHandler('logs/app.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


