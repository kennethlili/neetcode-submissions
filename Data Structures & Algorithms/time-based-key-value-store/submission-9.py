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
    Bound: [0, timestamp]
    find the max value that exist in the cahce
"""


class TimeMap:
    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        # if timestamp not in self.cache:
        #     self.cache[key] = []
        self.cache[key].append({"timestamp": timestamp, "value": value})

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        NINF = float('-inf')
        # for i in range(len(self.cache[key])):
        #     item = self.cache[key][i]
        #     if item["timestamp"] < timestamp:
        #         res = item["value"]
        #     elif item["timestamp"] == timestamp:
        #         return item["value"]
        #     else:
        #         break
        left, right = 0, len(self.cache[key])-1
        idx = NINF
        while left <= right:
            mid = (left + right) // 2
            currTs = self.cache[key][mid]['timestamp'] 
            if currTs < timestamp:
                idx = max(mid, idx)
                left = mid + 1
            elif currTs > timestamp:
                right  = mid - 1
            else:
                return self.cache[key][mid]['value'] 



        return "" if idx == NINF else self.cache[key][idx]['value'] 
