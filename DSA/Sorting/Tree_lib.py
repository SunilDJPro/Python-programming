from sortedcontainers import SortedList

def tree_sort(arr):
    sorted_list = SortedList(arr)
    return sorted_list

# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = tree_sort(arr)
    print("Sorted array:", sorted_arr)
