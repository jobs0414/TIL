def seqgen(data): 
    for index in range(0, len(data),2): 
        yield data[index:index+2]

result =seqgen('ABCDEFGHIJKLMN') 
for k in result: 
    print(k,end= ',')
