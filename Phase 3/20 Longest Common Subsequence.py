class Solution:
    def lcs(self, n, m, str1, str2):
        def tabulationApproach():
            cache = [[0] * (m + 1) for i in range(n + 1)]
            for index1 in range(n - 1, -1, -1):
                for index2 in range(m - 1, -1, -1):
                    if str1[index1] == str2[index2]:
                        cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                    else:
                        choice1 = cache[index1 + 1][index2]
                        choice2 = cache[index1][index2 + 1]
                        cache[index1][index2] = max(choice1, choice2)
 
            return cache[0][0]
 
        return tabulationApproach()