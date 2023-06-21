k = int(input())
nums = list(map(int, input().split()))
S = sum(nums)
check = [1 for _ in range(0, S+1)]
check[0] = 0
def go(current, total):
    if total > S:
        return
    if current == k:
        if total > 0 and total <= S:
            check[total] = 0
    else:
        
        go(current + 1, total + nums[current])
        go(current + 1, total - nums[current])
        go(current + 1, total)

go(0, 0)
print(sum(check))
    

    
            

