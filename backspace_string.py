class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        S_after = ''
        T_after = ''
        
        for i in range(len(S)):
            if S[i] != '#':
                S_after += S[i]
            elif S[i] == '#':
                try:
                    S_after = S_after[:-1]
                except(IndexError):
                    S_after = ''
        
        for k in range(len(T)):
            if T[k] != '#':
                T_after += T[k]
            elif T[k] == '#':
                try:
                    T_after = T_after[:-1]
                except(IndexError):
                    T_after = ''
       
        
        return S_after == T_after
