for hang in range(1, 10):
    #print(dan, " 단")
    for dan in range(2, 10):
        print("%d*%d=%2d" % (dan, hang, (dan*hang)), end='\t')
    print()