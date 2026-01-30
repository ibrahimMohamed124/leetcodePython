import math
from typing import List

def productsExceptSelf(nums: List[int]) -> List[int]:
   hashmapNums = {i: val for i, val in enumerate(nums)}
   valuesMatrix = []
   for k in hashmapNums:
        count = 0
        if k == 0:
            k+1
            valuesMatrix.append(math.prod(hashmapNums[k]))
        
        
        
    
   

nums = [1, 2, 4, 6]
print(productsExceptSelf(nums))  
