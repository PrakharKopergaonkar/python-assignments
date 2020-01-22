def arrangefreq(list, size):
    maxoflist = max(list)
    #calculate frequency
    freq = [0 for i in range(0, maxoflist+1)]
    for i in list:
        freq[i]+=1
    #sorting of list 
    for i in range(0, size-1):
        for j in range(i+1, size):
            if(freq[list[i]] < freq[list[j]]):
                list[i] , list[j] = list[j], list[i]
            if(freq[list[i]]==freq[list[j]]):
                if(list[i]>list[j]):
                    list[i],list[j] = list[j], list[i]
    print(list)
size = int(input("enter size of elements"))
list = [int(input()) for i in range(0,size)]
arrangefreq(list, size)
