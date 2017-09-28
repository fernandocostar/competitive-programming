n, m = map(int, input().split(" "))
nums = [int(x) for x in input().split(" ")]
result = True
for k in range(n-1):
		result = result and nums[k+1]-nums[k] <= m
result = result and (nums[0] <= m and 42195 - nums[-1] <= m)
print("S") if result else print("N")

