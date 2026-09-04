def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        for k in range(len(arr)):

            if i >= len(left):
                arr[k] = right[j]
                j =j+1

            elif j >= len(right):
                arr[k] = left[i]
                i =i+1

            elif left[i] < right[j]:
                arr[k] = left[i]
                i=i+1

            else:
                arr[k] = right[j]
                j=j+1


ticket_prices = [5000, 2000,2000, 8000, 3000,6589,6534,8657]

merge_sort(ticket_prices)

print(ticket_prices)