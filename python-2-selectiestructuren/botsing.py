x1r1 = int(input())
y1r1 = int(input())
x2r1 = int(input())
y2r1 = int(input())
x1r2 = int(input())
y1r2 = int(input())
x2r2 = int(input())
y2r2 = int(input())


minx = x1r1 if(x1r1<x2r1) else x2r1
maxx = x1r1 if(x1r1>=x2r1) else x2r1
miny = y1r1 if (y1r1<y2r1) else y2r1
maxy = y1r1 if (y1r1>=y2r1) else y2r1

if x1r2<maxx and x1r2>minx and y1r2<maxy and y1r2>miny:
    print('botsing')
elif x1r2<maxx and x1r2>minx and y2r2<maxy and y2r2>miny:
    print('botsing')
elif x2r2<maxx and x2r2>minx and y2r2<maxy and y2r2>miny:
    print('botsing')
elif x2r2<maxx and x2r2>minx and y1r2<maxy and y1r2>miny:
    print('botsing')
elif (x1r1==x1r2 or x1r1==x2r2) and (x2r1==x2r2 or x2r1==x1r2) and (y1r1==y1r2 or y1r1==y2r2) and (y2r1==y2r2 or y2r1==y1r2):
    print('botsing')
elif (x2r2==maxx and x1r2==minx) or (x1r2==maxx and x2r2==minx):
    if (y1r2<maxy and y1r2>miny) or (y2r2<maxy and y2r2>miny):
        print('botsing')
    else:
        print('geen botsing')
    
elif (y2r2==maxy and y1r2==miny) or (y1r2==maxy and y2r2==miny):
    if (x1r2<maxx and x1r2>minx) or (x2r2<maxx and x2r2>minx):
        print('botsing')
    else:
        print('geen botsing')
    
else:
    print('geen botsing')