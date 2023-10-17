def count_down(num):
    count = num
    
    if count == 0:
        return num
    return str(count) + " " + str(count_down(num-1))
    
    # while count<=num:
    #     list.append(count)
    #     count+=1
    # return list

print(count_down(8))

def count_up(num):
    count = num
    
    if count == 0:
        return num
    return str(count_up(num-1)) + " " + str(count) 

print(count_up(8))