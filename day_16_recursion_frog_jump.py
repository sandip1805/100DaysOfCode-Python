def frogJump(n):
    if n <= 1: return 1
    return frogJump(n-1) + frogJump(n-2)

def frogJump_bottom_up(n):
    if n == 0 or n == 1: return 1
    nums = [0] * (n+1)
    nums[0] = nums[1] = 1
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

if __name__ == "__main__":
    print("Frog jump on river!!")
    print(frogJump_bottom_up(100))
    print(frogJump(100))
    