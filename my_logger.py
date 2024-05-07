import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
        handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ])
logging.warning('An example message.')
logging.warning('Another message')

def input_error_loger(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception:
            logging.warning("Can not add user")
    
    return wrapper
