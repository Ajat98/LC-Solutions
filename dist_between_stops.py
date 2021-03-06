"""
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops
where distance[i] is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.
Example 1:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
Example 2:
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
"""

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        n = len(distance)
            
        clockwise_dist = 0
        i = start
        while i!= destination:
            clockwise_dist += distance[i]
            i = (i+1) % n
            
        CC_dist = 0
        k = start
        while k!= destination:
            k = (k-1) % n
            CC_dist += distance[k]
        
        return min(clockwise_dist, CC_dist)
            
        
