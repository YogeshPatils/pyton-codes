def isValid(s):
        pare={')':'(','}':'{',']':'['}
        par=[]
        if len(s)%2==1 or s[0] in (')','}',']') or s[-1] in ('(','{','['):
            return False
        else:
            for i in s:
                if i in ('(','{','['):
                    par.append(i)
                elif not par:
                    return False
                else:
                    if not(par[-1]==pare[i]):
                        return False
                    par.pop()
                        
            return not par
