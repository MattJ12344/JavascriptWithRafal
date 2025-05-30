class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findfirst(nums,target):
            left=0
            right=len(nums)-1
            first=-1

            while left<=right:

                mid=(left+right)//2

                if nums[mid]==target:

                    first=mid
                    right=mid-1

                elif nums[mid]<target:

                    left=mid+1

                else:

                    right=mid-1

            return first

        def findlast(nums,target):
            left=0
            right=len(nums)-1
            last=-1

            while left<=right:

                mid=(left+right)//2

                if nums[mid]==target:

                    last=mid
                    left=mid+1

                elif nums[mid]<target:

                    left=mid+1

                else:

                    right=mid-1

            return last

        return [findfirst(nums,target),findlast(nums,target)]