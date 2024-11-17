n=int(input())
out_list={}
for i in range(n):
    word=input()
    if word not in out_list:
        out_list[word]=1
    else:
        out_list[word]=out_list[word]+1
print(len(out_list))
print(*out_list.values())

'''
4
bcdef
abcdefg
bcde
bcdef

o/p
3
2 1 1

explanaition- 
no of distinct words (bcdef abcdefg bcde) 3
their occurrence in order {bcdef:2, abcdefg:1, bcde:1} 2 1 1
