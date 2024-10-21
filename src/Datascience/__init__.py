import os
import sys
import logging

# Set up logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s : %(message)s]"

# Logging Directory
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler(sys.stdout)   # Log to console
    ]
)

# Create a logger instance
logger = logging.getLogger("datasciencelogger")