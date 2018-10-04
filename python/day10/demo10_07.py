def param(func): 
    def wrapper(): 
        return '<p>' + str(func())  + '</p>'

    return wrapper 


@param
def outname(): 
    return 'python'




def outage(): 
    return 29 


print(outname())
print(outage())

