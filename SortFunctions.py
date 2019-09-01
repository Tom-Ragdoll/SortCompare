def bubble_sort(nums, length):
    for i in range(length - 1):
        for j in range(length - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def selection_sort(nums, length):
    for i in range(length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


def insertion_sort(nums, length):
    for i in range(length - 1):
        curNum, preIndex = nums[i+1], i
        while preIndex >= 0 and curNum < nums[preIndex]:
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = curNum
    return nums


def shell_sort(nums, length):
    gap = 1
    while gap < length // 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, length):
            curNum, preIndex = nums[i], i - gap
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex]
                preIndex -= gap
            nums[preIndex + gap] = curNum
        gap //= 3
    return nums


def heap_sort(nums, length):

    def adjustheap(num, i, size):
        leftchild = 2 * i + 1
        rightchild = 2 * i + 2
        largest = i
        if leftchild < size and num[leftchild] > num[largest]:
            largest = leftchild
        if rightchild < size and num[rightchild] > num[largest]:
            largest = rightchild
        if largest != i:
            num[largest], num[i] = num[i], num[largest]
            adjustheap(num, largest, size)

    def builtheap(num, size):
        for index in range(len(num)//2)[::-1]:
            adjustheap(num, index, size)

    builtheap(nums, length)
    for i in range(len(nums))[::-1]:
        nums[0], nums[i] = nums[i], nums[0]
        adjustheap(nums, 0, i)

    return nums


def merge_sort(nums, length):

    def merge(left, right):
        i, j, result = 0, 0, []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]
        return result

    if length <= 1:
        return nums
    mid = length // 2
    left = merge_sort(nums[:mid],mid)
    right = merge_sort(nums[mid:],length-mid)

    return merge(left, right)


def quick_sort(nums, left, right):

    def partition(nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    if left < right:
        pivotIndex = partition(nums, left, right)
        quick_sort(nums, left, pivotIndex - 1)
        quick_sort(nums, pivotIndex + 1, right)
    return nums


def counting_sort(nums):
    bucket = [0] * (max(nums) + 1)
    for num in nums:
        bucket[num] += 1
    i = 0
    length=len(bucket)
    for j in range(length):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


def bucket_sort(nums, defaultBucketSize = 5):
    maxVal, minVal = max(nums), min(nums)
    bucketSize = defaultBucketSize
    bucketCount = (maxVal - minVal) // bucketSize + 1
    buckets = []
    for i in range(bucketCount):
        buckets.append([])
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)
    nums.clear()
    for bucket in buckets:
        bucket.sort()
        nums.extend(bucket)
    return nums



def radixSort(nums):
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))
    buckets = [[] for row in range(mod)]
    while mostBit:
        for num in nums:
            buckets[num // div % mod].append(num)
        i = 0
        for bucket in buckets:
            while bucket:
                nums[i] = bucket.pop(0)
                i += 1
        div *= 10
        mostBit -= 1
    return nums
