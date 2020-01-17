class Solution:
    def climbStairs(self, n: int) -> int:
        # n is num of steps to top of stairs
        # can climb in 1 or two steps, how many distinct ways to top
        
        if n == 1:
            return 1
        
        steps = [0 for i in range(n)] #initialize list up n with 0 as all values
        steps[0] = 1
        steps[1] = 2
        print(steps)
        
        #fib sequence
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1] 
