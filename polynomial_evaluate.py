'''
2 15
x**4 - x + 1
'''
x_k=input().split()
x_k=tuple(map(int,x_k))
exp=input().strip()
exp_list=exp.split()
n=len(exp_list)
i=0
p_x=0
while i<n:
    if '0'<=exp_list[i][0]<='9' and i>1 and exp_list[i-1]=='-':
        if '**' in exp_list[i]:
            p_x=p_x-int(exp_list[i][0])*x_k[0]**int(exp_list[i][-1])
        elif len(exp_list[i])>1 and exp_list[i][1].isalpha():
            p_x=p_x-int(exp_list[i][0])*x_k[0]
        else:
            p_x=p_x-int(exp_list[i])

    elif exp_list[i][0].isalpha() and exp_list[i-1]=='-':
        if '**' in exp_list[i]:
            p_x=p_x-x_k[0]**int(exp_list[i][-1])
        elif exp_list[i].isalpha():
            p_x=p_x-x_k[0]
    
    elif '0'<=exp_list[i][0]<='9':
        if '**' in exp_list[i]:
            p_x=p_x+int(exp_list[i][0])*x_k[0]**int(exp_list[i][-1])
        elif len(exp_list[i])>1 and exp_list[i][1].isalpha():
            p_x=p_x+int(exp_list[i][0])*x_k[0]
        else:
            p_x=p_x+int(exp_list[i])

    elif exp_list[i][0].isalpha():
        if '**' in exp_list[i]:
            p_x=p_x+x_k[0]**int(exp_list[i][-1])
        elif exp_list[i].isalpha():
            p_x=p_x+x_k[0]
    i+=2 
if p_x==x_k[-1]:
    print(True)
else:
    print(False)
