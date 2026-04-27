import bisect
class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        mid = n // 2
    
    
        if n % 2 != 0:
            return float(self.arr[mid])
        else:
            return (self.arr[mid - 1] + self.arr[mid]) / 2.0
        
        