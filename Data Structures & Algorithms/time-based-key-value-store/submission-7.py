class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # dictionary k -> v is name -> (timestamp, value)
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        # get array based on key
        if key not in self.map or self.map[key][0][0] > timestamp:
            return ""

        arr = self.map[key]
        # binary search in array
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (r + l) // 2
            if timestamp > arr[mid][0]:
                l = mid + 1
            elif timestamp < arr[mid][0]:
                r = mid - 1
            else:
            # if found exactly, return the exact value
                return arr[mid][1]

        if timestamp >= arr[r][0]:
            return arr[r][1]
        else:
            return arr[r-1][1] if r - 1 >= 0 else ""