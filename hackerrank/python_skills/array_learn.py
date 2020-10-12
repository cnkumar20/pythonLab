def spiral(m,n):
    a = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
    print(a[2][2])
    begin_row = 0
    begin_column =0
    end_row = m
    end_column = n
    flag = False
   #move right:
    while(begin_row < end_row and begin_column < end_column):
        #move right
       for x in range(begin_column,end_column):
           print(a[begin_row][x])
       begin_row +=1
       #move down:
       for x in range(begin_row,end_row-1):
           print("Hello")
           print(a[x][end_column-1])
       end_column -=1
       #move left
       for x in range(end_column-1,begin_column-1,-1):
           print("hello1")
           print(a[end_row-2][x])
       end_row -=1
       #move up
       for x in range(end_row-1,begin_row-1,-1):
           print(a[x][begin_column])
       begin_column +=1
print(spiral(4,4))
