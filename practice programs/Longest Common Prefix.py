'''Input: strs = ["flower","flow","flight"]
Output: "fl"'''
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        shortest = len(strs[0])
        for each in strs:
            if len(each) <= shortest:
                shortest=len(each)
        start_of_string = 0
        end_of_string = shortest
        myStr = strs[0]
        check_str = myStr[start_of_string:end_of_string]
        counter = 0
        while counter<len(strs):
            for i in strs:
                if i.__contains__(check_str):
                    counter+=1
                    if counter==len(strs):
                        return check_str
                else:
                    counter=0
                    end_of_string-=1
                    check_str=check_str[start_of_string:end_of_string]
                    i=strs[0]




sol = Solution()
val=sol.longestCommonPrefix(["c","acc","ccc"])
print(val)