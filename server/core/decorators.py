import logging, os, datetime

def task(file_name):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            # Configurar o caminho do arquivo de log
            log_dir = os.path.join(os.path.dirname(__file__), '..', 'jobs', 'log', file_name)
            os.makedirs(log_dir, exist_ok=True)
            log_filename = datetime.datetime.now().strftime('%d%m%Y-%H%M%S.log')
            log_filepath = os.path.join(log_dir, log_filename)

            # Configurar o FileHandler
            file_handler = logging.FileHandler(log_filepath)
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            # Adicionar o FileHandler ao logger
            logger = logging.getLogger(file_name)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)

            logger.info(f"Task {func.__name__} is starting.")
            try:
                await func(*args, **kwargs)
                logger.info(f"Task {func.__name__} completed successfully.")
            except Exception as e:
                logger.error(f"Task {func.__name__} failed with error: {e}")
                raise
            finally:
                # Remover o FileHandler após a execução
                logger.removeHandler(file_handler)
                file_handler.close()
        return wrapper
    return decorator