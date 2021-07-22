a = ['a1', 'a2', 'a3']


# 방법1
# for i in range(len(a)):
#     print(i, a[i])

# 방법2
# i = 0
# for v in a:
#     print(i, v)
#     i += 1

# 방법3
for i, v in enumerate(a):
    print(i, v)