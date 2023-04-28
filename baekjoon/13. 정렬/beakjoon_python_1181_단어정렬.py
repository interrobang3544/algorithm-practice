N=int(input())
word_list=[]

for i in range(0,N):
    word_list.append(input())
    
word_list=list(set(word_list))
word_list.sort()
word_list.sort(key=len)

for word in word_list:
    print(i)