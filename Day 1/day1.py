#Part 1 Solution
f1 = open("day1Input.txt") 
nums = [] 

for line in f1: 

        line = line.rstrip() 
        nums.append(line)

for i, num in enumerate(nums): 
        for j, num2 in enumerate(nums): 
                if ((int(num) + int(num2)) == int(2020)): 
                        print(int(num) * int(num2))


#Part 2 Solution 
f1 = open("day1Input.txt") 
nums = [] 

for line in f1: 

        line = line.rstrip() 
        nums.append(line)

for i, num in enumerate(nums): 
        for j, num2 in enumerate(nums): 
                for k, num3 in enumerate(nums): 
                        if ((int(num) + int(num2) + int(num3)) == int(2020)): 
                                print(int(num) * int(num2)* int(num3))
