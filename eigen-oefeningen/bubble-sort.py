def bubble_sort(a):
    count = 0
    for i in range(0,len(a)-1):
        for j in range(len(a)-1,i,-1):
            if(a[j-1] > a[j]):
                a[j],a[j-1] = a[j-1],a[j]
            count+=1

        print(a)
    print(f"Voor een rij van lengte {len(a)} werd het if-statement {count} keer uitgevoerd")


a = [int(_) for _ in input().split()]
bubble_sort(a)


