def firstBadVersion(self, n):
        lo=1
        hi=n
        while lo<=hi:
            mid=lo+(hi-lo)/2
            if isBadVersion(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo
#happy coding 😊
