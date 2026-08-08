class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.arr = nums

    def add(self, val: int) -> int:
        # add then sort each value in stream of vals then find k largest
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
