def arrangefreq(list, size):
    #calculate frequency
    freq = dict()
    for i in list:
        if i in freq.keys():
             freq[i]+=1
        else:
            freq[i]=1
    #sorting of list if freq[i] < freq[j] -> swap or if freq[i]=freq[j] then if i>j -> swap
    for i in range(0, size-1):
        for j in range(i+1, size):
            if(freq[list[i]] < freq[list[j]]):
                list[i] , list[j] = list[j], list[i]
            if((freq[list[i]]==freq[list[j]]) and (list[i]>list[j])):
                list[i],list[j] = list[j], list[i]
    print(list)
size = int(input("enter size of elements"))
list = [int(input()) for i in range(0,size)]
arrangefreq(list, size)
