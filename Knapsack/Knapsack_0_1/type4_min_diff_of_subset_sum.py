class Solution(object):
    def __init__(self, array):
        self.array = array
        self.N = len(array)
        self.arr_total = sum(array)
        self.min_diff = float("inf")

    def min_diff_subsets(self):
        self._hypothesis(self.array, self.N, 0)
        print(self.min_diff)
    
    def _hypothesis(self, array, N, subset_sum):
        if N == 0:
            self.min_diff = min(abs(2*subset_sum - self.arr_total), self.min_diff)
            return

        self._hypothesis(array[:-1], N-1, subset_sum + array[-1]) 
        self._hypothesis(array[:-1], N-1, subset_sum ) 
        


array = [1,6,11,5]
solution = Solution(array)
solution.min_diff_subsets()  


