def swap_first_last(num):
    t=num
    if num<10:
        return(num)
    g=1
    d=num%10
    while t>=10:
        t//=10
        g*=10
    fd=num//g
    if d==fd:
        return(num)
    nofl=(num%g)//10
    return((d*g)+nofl*10+fd)
