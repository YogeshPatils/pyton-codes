'''
3 2 (3-- no of integers in the array, 2 is no of set elements set_A and set_B)
1 5 3 -- integer array
3 1   -- set_A
5 7   -- set_B

You gain  1 unit of happiness for elements  and  in set_A . You lose 1 unit for  in set_B . The element is not in set  then it wont change the happiness calculation.
'''
n_m=list(map(int,input().split()))
int_array=list(map(int,input().split()))
happy=0
set_A=set(map(int,input().split()))
set_B=set(map(int,input().split()))
for j in int_array:
    if j in set_A:
        happy+=1
    elif j in set_B:
        happy-=1
print(happy)
