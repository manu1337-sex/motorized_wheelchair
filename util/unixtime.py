import time

def getTime(offsetSeconds=0):
    return str(round(time.time() * 1000) + (1000 * offsetSeconds))

def ckTime(time: int):
    return {"currentTimeMillis": time}

never = 4070926800000