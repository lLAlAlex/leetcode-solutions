from collections import defaultdict

class TimeMap:
    
    def __init__(self):
        self.map = defaultdict()

    def set(self, key: str, value: str, timestamp: int):
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int):
        if key not in self.map:
            return ""