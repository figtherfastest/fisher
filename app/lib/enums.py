
from enum import Enum

class PendingStatus(Enum):
    waiting = 1
    success = 2
    reject = 3
    redraw = 4