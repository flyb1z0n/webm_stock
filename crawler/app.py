import logging
from dynaconf import settings
from .scanners.board_monitor import BoardMonitor
from .scanners.thread_monitor import ThreadMonitor


def init():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(threadName)s] - %(levelname)s [%(filename)s:%(lineno)d] - %(message)s")
    logging.info('Initialization finished.')


def start_monitoring():
    logging.info('Starting Monitors.')

    # BoardMonitor(settings.BOARD_URL, settings.BOARD_MONITOR_DELAY_SECONDS).start()
    ThreadMonitor(settings.THREAD_URL,
                  settings.THREAD_MONITOR_THREAD_REQUEST_DELAY_SECONDS,
                  settings.THREAD_FAIL_COUNT_LIMIT,
                  settings.FILE_MEDIA_EXTENSIONS
                  ).start()

    logging.info('Monitors have been started.')


def run():
    init()
    start_monitoring()
