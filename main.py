import sys
from app import build_app
from logger import configure_logger

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        orchestrator = build_app()
        orchestrator.start(file_path)
    else:
        logger = configure_logger()
        logger.error("No input received.")
