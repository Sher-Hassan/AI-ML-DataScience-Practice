import logging

## Logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[  # Handlers are the components that determine where your log messages actually go.
        logging.FileHandler("app1.log"),  # Writes log messages to app1.log file
        logging.StreamHandler()  # Outputs log messages to console (stdout)
    ]
)