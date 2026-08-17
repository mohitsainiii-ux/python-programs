def eveninlist(n):
    for i in n:
        assert i % 2 == 0

n = [2, 4, 6, 8]
eveninlist(n)
print(n)
print("All Even Numbers")