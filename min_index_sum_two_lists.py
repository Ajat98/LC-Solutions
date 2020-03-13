"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement. 
You could assume there always exists an answer.
Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        d = {}
        for x,i in enumerate(list1):
            if i not in d:
                d[i] = [1, x]
            elif i in d:
                d[i][0] +=1
        
        for j,k in enumerate(list2):
            if k not in d:
                d[k] = [1, j]
            else: 
                d[k][0] +=1
        
        choices = []
        for r in d.keys():
            if d[r][0] == 2:
                choices.append([r, (list1.index(r) + list2.index(r))])
        print(choices)
        
        current_min = 2000
        best_choice = []
        for c in choices:
            total = c[1]
            print(total, c)
            if total <= current_min:
                current_min = total
                best_choice.append(c[0])
                
        return best_choice
