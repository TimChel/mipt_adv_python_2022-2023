with open("Test.txt", mode="w+") as f:
    f.write('something string63356')
    f.seek(0)
    f.write('new string')
    # print(f.readline())
    # print(f.tell())
    # print(f.readline())
    # print(f.tell())
    # f.seek(4)
    # print(repr(f.read(1)))
    # for x in f:
    #     print(x, end="")
print()