# program of average of list

def average (list):
    return sum(list)/len(list)

list = [15,12,34,45,13]
average = average(list)

print(" The average of list is ", round(average,2))