rowData = "1"
print(rowData)

for i in range(10):
    output = ""
    index = 0
    while index < len(rowData):
        current = rowData[index]    # 1
        count = 1
        # 현재하고 다음숫자가 같은지 비교 
        while index+1 < len(rowData) and current == rowData[index+1]:
            count += 1
            index += 1

        output += current + str(count) 
        index += 1
    print(output)
    rowData = output

