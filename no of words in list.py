#number of words and number of charecter in a string
x="the dog car bus umbrella"
count=0
for ch in x:
    if(ch==' '):
        count+=1
        print(*"number of words in given string:",count)
