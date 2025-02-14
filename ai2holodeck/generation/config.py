import os 

class GlobalConfig:
    VERBOSE = os.getenv("VERBOSE", False)

