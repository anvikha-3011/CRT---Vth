'''
input : [12,45,36,89,75,63,20]
output : [12,36,20]
'''
arr = list(map(int,input().split()))
res = []
for ele in arr:
    if ele % 2 == 0:
        res.append(ele)
print(res)
