import logging

logging.basicConfig(
    filename="app_logs.log",  # Common log file for all scripts
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",  # Format includes filename
)

logger = logging.getLogger(__name__)