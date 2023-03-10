class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        Sum = 0;
        count = 0;
        numsBit = []
        Map = defaultdict(int)
        Map[0] = 1
        
        
        for num in nums:
            if num%2 == 0:
                numsBit.append(0)
            else:
                numsBit.append(1)
        
        for i in range(len(numsBit)):
            Sum += numsBit[i]
            
            if Sum-k in Map:
                count += Map[Sum-k]
                
            Map[Sum] += 1
            
        return count
            