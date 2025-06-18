class Solution(object):
    def searchRange(self, numbers: list[int], target: int) ->list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findfirst(numbers: list[int],target: int) -> int:
            left: int=0
            right: int=len(numbers)-1
            first: int=-1

            while left<=right:

                mid: int=(left+right)//2

                if numbers[mid]==target:

                    first=mid
                    right=mid-1

                elif numbers[mid]<target:

                    left=mid+1

                else:

                    right=mid-1

            return first

        def findlast(numbers: list[int],target: int) -> int:
            left: int=0
            right: int=len(numbers)-1
            last: int=-1

            while left<=right:

                mid=(left+right)//2

                if numbers[mid]==target:

                    last=mid
                    left=mid+1

                elif numbers[mid]<target:

                    left=mid+1

                else:

                    right=mid-1

            return last

        return [findfirst(numbers,target),findlast(numbers,target)]