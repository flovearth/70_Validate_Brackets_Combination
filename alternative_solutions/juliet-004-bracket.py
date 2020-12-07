def brackets():
    entry = str(input('please enter something with brackets: '))
    a= {'(':')', '{':'}', '[':']'}
    b= [')', '}', ']', '(', '[', '{']
    #c= ['(', '[', '{']
    d= []
    if entry == "" or '':
        return True
    for i in entry:
        if i in b:
            d.append(i)
    n = len(d)
    while n > 1:
        if d[0] not in a.keys():
            return False
        elif a[d[0]] == d[-1]:
            return True
        elif d[0] in a.keys():
            if d[1] != a[d[0]]:
                d.pop(1)
                n = n-1
            elif d[1] == a[d[0]]:
                del d[:2]
                n = n-2
    if len(d)==0:
        return True
    else:
        return False
brackets()