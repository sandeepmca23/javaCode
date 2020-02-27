
# Read the variable from STDIN
a = int(input())
lis = []


def evenOdd(ele1, ele2):
    lis2 = []
    if ((ele2-ele1) == 9):
        for temp in range(ele1, ele2+1):
            lis2.append(temp)
        lis.append(lis2)
    elif ((ele2-ele1) > 10):
        lis.append("Out of Range")
    else:
        lis.append("Difference Not in Range")


for temp in range(a):
    text = input().split()
    evenOdd(int(text[0]), int(text[1]))
for temp2 in lis:    
  print(temp2)

