class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps,mapt={},{}
        for c1, c2 in zip(s, t):
            if ((c1 in maps and maps[c1]!=c2) or (c2 in mapt and mapt[c2]!=c1)):
                return False
            maps[c1]=c2
            mapt[c2]=c1
        return True
      
