def arrangefreq(list1, size):
    answer_list = []
    #calculate frequency
    freq = dict()
    for i in list1:
        if i in freq.keys():
             freq[i]+=1
        else:
            freq[i]=1
     #convert dictonary into list of tuples of values and its frequency 
    freq = list(freq.items())
    #sort the list by frequency, if two values have same frequency(higher frequency comes first) they are sorted by value(smaller values comes first)
    #printing of elements is done in the same for loop
    for i in range(0, len(freq)-1):
        for j in range(i+1,len(freq)):
            if((freq[i][1] < freq[j][1]) or ((freq[i][1] == freq[j][1]) and freq[i][0]>freq[j][0])):
                freq[i],freq[j]=freq[j],freq[i]
        print(str(freq[i][0])*freq[i][1],end="")
        if(i==len(freq)-2):
            print(str(freq[i+1][0])*freq[i+1][1],end="")
#main function
size = int(input("enter size of elements"))
list1 = [int(input()) for i in range(0,size)]
arrangefreq(list1, size)
