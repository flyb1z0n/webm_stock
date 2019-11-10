from thread_monitor import ThreadMonitor
from board_monitor import BoardMonitor

bm = BoardMonitor().start(config.BOARD_MONITOR_DELAY_SECONDS)
tm = ThreadMonitor().start(config.BOARD_MONITOR_DELAY_SECONDS)
