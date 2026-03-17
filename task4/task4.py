import sys
for i in range(1,len(sys.argv)): 
    with open(file = sys.argv[i], mode = "r", encoding = "utf-8") as f:
        list=f.readlines()
    list=[int (x) for x in list]  
    med = sorted(list)[len(list) // 2]  
    steps = sum(abs(j-med) for j in list)
    if steps > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу.")
    else:
        print(steps)  
