class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k

        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        self.push(val)

        if len(self.heap) - 1 > self.k:
            self.pop()
        
        return self.heap[1]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] <= self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

        
    def pop(self):
        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap) and
                self.heap[i * 2 + 1] < self.heap[i * 2] and
                self.heap[i] > self.heap[i * 2 + 1]):
                # Swap w right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break
        return res

        

        



        
