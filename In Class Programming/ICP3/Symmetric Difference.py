print("This program takes two sets and returns the difference.")
input1 = [int(x) for x in input ("Please input set 1 seperated by spaces: ").split()]
input2 = [int(x) for x in input ("Please input set 2 seperated by spaces: ").split()]
set1 = set(input1)
set2 = set(input2)
diff = set()
diff.update((set1 - set2))
print(diff)