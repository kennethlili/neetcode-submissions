"""
facts:
    TimeMap(): init the data structure
    void set(String key, String value, int timestamp): store the key with the value at the timestamp
    String get(String key, int timestamp): return the value with the latest key at that timestamp
    
questions:
    what ds works best for this question?
        - set the key and the value with a ts
        - get the history
    # alice: ['happy', , 'sad']
    alice:{
    1: happy
    3: sad
    }
    for range(2, -1, -1)
"""
class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = {}
        if timestamp not in self.cache:
            self.cache[key][timestamp] = {}
        self.cache[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        for i in range(timestamp, -1 , -1):
            if i in self.cache[key]:
                return self.cache[key][i]
        return ""
