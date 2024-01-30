def binary_search(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1
    mid = 0
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if sorted_array[mid] < target:
            low = mid + 1
        elif sorted_array[mid] > target:
            high = mid - 1
        else:
            # Element found
            return iterations, sorted_array[mid]

    # If the target is not found, return the upper bound
    upper_bound = None
    if low < len(sorted_array):
        upper_bound = sorted_array[low]

    return iterations, upper_bound


if __name__ == "__main__":
    # Example usage
    sorted_float_array = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

    # Searching for the element 4.7 in the sorted array
    iterations, upper_bound = binary_search(sorted_float_array, 4.7)

    if upper_bound is not None:
        print(f"Element not found. Upper bound: {upper_bound}. Iterations: {iterations}")
    else:
        print(f"Element found. Iterations: {iterations}")