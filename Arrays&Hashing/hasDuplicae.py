def hasDuplicate(list):
    for i in range(len(list) - 1):
        for j in range(len(list)):
            if i != j and list[i] == list[j]:
                return True
    return False
            

list = [1,2,3,3]

print(hasDuplicate(list))
