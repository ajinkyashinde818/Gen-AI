def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        # Recursion
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        # Merge using for loop
        for k in range(len(arr)):

            # If left array is finished
            if i >= len(left):
                arr[k] = right[j]
                j += 1

            # If right array is finished
            elif j >= len(right):
                arr[k] = left[i]
                i += 1

            # Compare both elements
            elif left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1


arr = [8, 3, 5, 1]

merge_sort(arr)

print(arr)