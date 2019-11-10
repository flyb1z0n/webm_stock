import config
from thread_monitor import ThreadMonitor
from board_monitor import BoardMonitor

bm = BoardMonitor(config.BOARD_MONITOR_DELAY_SECONDS).start()
tm = ThreadMonitor(config.THREAD_MONITOR_THREAD_REQUEST_DELAY_SECONDS).start()
