# first approch using builtin function split()
s = 'hello world '
list=s.split()
n=len(list)
l=list[n-1]
a=len(l)
print(a,'eeeeee')

# second approch without built in function,o(n),o(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s='hai hellow'
        i,length = len(s) -1,0

        while s[i] == " ":
            i-=1
        while i>0 and s[i]!=" ":
            length+=1
            i-=1
        return length 
