'''
this function returns the index of the fisrt occurrence of the given needle string
'''
def strStr(haystack, needle):
        
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
