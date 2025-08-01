
nums = [45, 32, 24, 34, 45, 46, 58]
sum = 0

for num in nums:
    print(num)
    sum += num
    if sum > 100:
        print(f"The summary of the numbers is more than 100: {sum}")
        print(f"The loop breaks at {num}")
        print(sum)
        break

