import random

class RandomizedSet:

    # check whether exists in O(1), use hashmap
    # remove from hashmap O(1)
    # insert from hashmap O(1)

    def __init__(self):
        self.index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        remove_index = self.index[val]
        last_value = self.nums[-1]

        self.nums[remove_index] = last_value
        self.index[last_value] = remove_index

        self.nums.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()