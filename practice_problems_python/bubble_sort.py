# 0(n^2)
def bubbleSort(num_list):
    for x in range(len(num_list)):
        for i in range(len(num_list) - 1):
            # print num_list
            if num_list[i] > num_list[i + 1]:
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp

    return num_list

# one way to improve the above sort would be to do a check if elements need to be
# swapped. If no swapping is required then we do have to do all the passes and hte list
# since the list is sorted already


def bubbleSortV2(num_list):
    sorted = False
    num_of_passes = len(num_list) - 1

    while num_of_passes > 0 and not sorted:
        sorted = True
        for i in range(len(num_list) - 1):
            # print num_list
            if num_list[i] > num_list[i + 1]:
                sorted = False
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp

        num_of_passes = num_of_passes - 1

    return num_list


num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
num_list2 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
print bubbleSort(num_list2)
print bubbleSortV2(num_list2)
