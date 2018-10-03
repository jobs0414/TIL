class InstanceCounter: 
    count =0 

    def __init__(self): 
        InstanceCounter.count += 1 

    @classmethod
    def print_instance_count(cls): 
        print(cls.count)


if __name__ == '__main__': 
    a = InstanceCounter() 
    a.print_instance_count

    b= InstanceCounter() 
    b.print_instance_count: 
    