# Day 10 - Maximum Subarray
# Using Kadane's Algorithm

# Take numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
    print("Please enter at least one number.")

else:
    # Initialize running sum and maximum sum
    current_sum = numbers[0]
    max_sum = numbers[0]

    # Track the start and end of the maximum subarray
    current_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(numbers)):

        # Decide whether to start a new subarray
        # or continue the current subarray
        if numbers[i] > current_sum + numbers[i]:
            current_sum = numbers[i]
            current_start = i
        else:
            current_sum += numbers[i]

        # Update maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = current_start
            best_end = i

    # Get the maximum subarray
    max_subarray = numbers[best_start:best_end + 1]

    print("\nResults:")
    print("Maximum Sum:", max_sum)
    print("Maximum Subarray:", max_subarray)
    print("Start Index:", best_start)
    print("End Index:", best_end)