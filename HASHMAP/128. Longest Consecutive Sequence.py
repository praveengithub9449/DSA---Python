
def longestConsecutive(nums):
        if not  nums:
                return 0
        nums_set=set(nums)
        longest=1
        for num in nums_set:
                if num-1  not in nums_set:
                        cur=num
                        print(cur)
                        cur_longest=1


        while cur+1 in nums_set:
                cur += 1
                cur_longest += 1
        longest =max (longest,cur_longest )
        return longest





nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))



