class Solution(object):
    def removeDuplicates(self, numbers: list[int]) -> int:
        """
        :type numbers: List[int]
        :rtype: int
        """
        duplicate_count: int = 0
        write_index: int = 1

        for read_index in range(1, len(numbers)):
            if numbers[read_index] != numbers[read_index - 1]:
                duplicate_count = 0
                numbers[write_index] = numbers[read_index]
                write_index += 1
            else:
                duplicate_count += 1
                if duplicate_count <= 1:
                    numbers[write_index] = numbers[read_index]
                    write_index += 1

        return write_index
    
sol = Solution()


# Test 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = sol.removeDuplicates(nums1)
assert k1 == 5
assert nums1[:k1] == [1, 1, 2, 2, 3]

# Test 2
nums2 = [1, 2, 3]
k2 = sol.removeDuplicates(nums2)
assert k2 == 3
assert nums2[:k2] == [1, 2, 3]

# Test 3
nums3 = [1, 1, 1, 1]
k3 = sol.removeDuplicates(nums3)
assert k3 == 2
assert nums3[:k3] == [1, 1]

# Test 4
nums4 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k4 = sol.removeDuplicates(nums4)
assert k4 == 7
assert nums4[:k4] == [0, 0, 1, 1, 2, 3, 3]


print("Sprawdzam ")