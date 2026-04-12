import collections

class TimeMap:
    """
    DRY RUN EXAMPLE:
    1. set("foo", "bar", 1)  -> meta_store["foo"] = [[1, "bar"]]
    2. get("foo", 3)         -> target is 3. 
                               - check mid (index 0, time 1). 
                               - 1 <= 3 is True. res = "bar", left = 1.
                               - loop ends. returns "bar".
    3. set("foo", "bar2", 4) -> meta_store["foo"] = [[1, "bar"], [4, "bar2"]]
    4. get("foo", 5)         -> target is 5.
                               - mid 0: 1 <= 5 (True). res = "bar", left = 1.
                               - mid 1: 4 <= 5 (True). res = "bar2", left = 2.
                               - loop ends. returns "bar2".
    """

    def __init__(self):
        
        self.meta_store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.meta_store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.meta_store:
            return ""
        
        values = self.meta_store[key]
        left, right = 0, len(values) - 1
        res = ""
        
        
        while left <= right:
            mid = (left + right) // 2
            
            # values[mid][0] is the TIME, values[mid][1] is the VALUE
            if values[mid][0] <= timestamp:
                res = values[mid][1]  
                left = mid + 1        
            else:
                right = mid - 1       
                
        return res