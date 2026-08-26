#loop search from last
class Solution(object):
    def lengthOfLastWord(self, s):
        length=0
        a= len(s)-1
        while a>=0 and s[a]== ' ':
            a -=1
        while a>=0 and s[a]!= ' ':
            length+=1
            a-=1
        return length
#with split
class Solution(object):
    def lengthOfLastWord(self, s):
        word= s.split()
        return len(word[-1])
#using strip before split clears the white space if there at last
class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        word= s.split()
        return len(word[-1])


