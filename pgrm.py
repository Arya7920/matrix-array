n=int(input("enter n matrix "))  #3 row
m=int(input("enter m matrix "))  #4 colom

maxval=n*m   #12

a = [[0 for x in range(m)] for x in range(n)] # array creation
i=0
j=0
def islimit(ii,jj):# -1 1
    if((ii<0) or (ii>=n)):
        return True
    if((jj<0) or (jj>=m)):
        return True
    return False

def movetopright(ii,jj):# 0 0
    if(islimit(ii-1,jj+1)):
        return False
    return True

def movedownleft(ii,jj):
    if(islimit(ii+1,jj-1)):
        return False
    return True

def down(ii,jj):
    if(islimit(ii+1,jj+0)):
        return False
    return True

def right(ii,jj):
    if(islimit(ii+0,jj+1)):
        return False
    return True

a[i][j]=1 # setting (0,0) as 1 

count=2 
while(50):

    
    if(movetopright(i,j)):
        i=i-1
        j=j+1
        a[i][j]=count
        count=count+1
        continue
    else:
        while(True):
            if(movedownleft(i,j)):
                i=i+1
                j=j-1
                
            else:
                break
    if(down(i,j)):
        i=i+1
        j=j+0
        a[i][j]=count
        count=count+1
    else:
        if(right(i,j)):
            i=i+0
            j=j+1
            a[i][j]=count
            count=count+1
        else:
            break
    
res=""
for i in range(n):
    for j in range(m):
        res=res+str(a[i][j])+"  "
    print(res)
    res=""
