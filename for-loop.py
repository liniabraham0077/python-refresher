obj = [1, "a", 2, "lini"]

for i in obj:
    print(i)

# range j to j-1
total = 0;
for j in range(1, 6):
    print(j)
    total = total + j
print("{} {}".format("total is", total))

# increment loop by 2
val=[1,2,3,4,5]
print(len(val))
for i in range(0,len(val),2):
    print(val[i])

print("print from 0 to 4 (j-1)")
for j in range(5):
    print(j)

print("print from 1 to 4 (j-1)")
for j in range(1,5):
    print(j)

print("print from 1 to 7 (j-1) incrementing by 2")
for j in range(1,8,2):
    print(j)
