def selection_sort(arr):
    """
    Perform selection sort on a list in-place.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the index of the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element in the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage:
if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(unsorted_list)
    print("Sorted list:", sorted_list)
