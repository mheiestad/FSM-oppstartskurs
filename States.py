from enum import Enum

class States(Enum):
    DISARMED = 0
    ARMING = 1
    TAKEOFF = 2
    HOVER = 3
    FLYING = 4
    LANDING = 5
    LANDED = 6
    