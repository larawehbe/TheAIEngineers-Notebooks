def outputList(nums):
    output = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    output.append([nums[i], nums[j], nums[k]])
    return output

inputList = [-1,0,1,2,-1,-4]
result = outputList(inputList)
print (f"output : {result}")
