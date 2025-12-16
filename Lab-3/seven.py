# wap to count the frequency of each element in a list using a dictionary using a dictionary

def count_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency