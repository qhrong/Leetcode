class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        # Merge sort
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  # Finding the mid of the array
                L = arr[:mid]  # Dividing the array elements
                R = arr[mid:]  # into 2 halves

                mergeSort(L)  # Sorting the first half
                mergeSort(R)  # Sorting the second half

                i = j = k = 0

                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1

            return arr

        min_val = mergeSort(A)[0]

        res = 0
        while min_val // 10 >= 1: # Dividt by 10 each time and add the remainder to res
            res += min_val % 10
            min_val = min_val // 10
        res = res + min_val

        if res % 2 == 0:
            return 1
        else:
            return 0