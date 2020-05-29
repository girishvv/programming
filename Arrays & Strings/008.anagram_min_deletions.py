# -*- coding: utf-8 -*-
def findMinDeletions(a,b):
    #print(a,b)
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    m = len(a)
    n = len(b)
    hm_a = {}
    hm_b = {}

    for ch in a:
        if ch not in hm_a:
            hm_a[ch] = 1
        else:
            hm_a[ch] +=1
    for ch in b:
        if ch not in hm_b:
            hm_b[ch] = 1
        else:
            hm_b[ch] +=1

    cmn_cnt = 0

    for ch in hm_a.keys():
        if ch in hm_b.keys():
            cmn_cnt += min(hm_a[ch],hm_b[ch])
    return m + n -(2*cmn_cnt)

a = "tttttttttttttttttttttttttttttttttttttsssssssssssssssss"
b = "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
print(findMinDeletions(a,b))


