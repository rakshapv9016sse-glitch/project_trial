nums=[0,1,0,3,12]
result=[]
for num in nums:
    if num!=0:
        result.append(num)
zero_count=nums.count(0)
result+=[0]*zero_count
print(result)
