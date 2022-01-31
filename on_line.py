def online(p1,p2,p3x):
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = p1[1]-slope*p1[0]
    p3y = slope*p3x + b
    return b
    
if __name__=="__main__":
    p3y=online((0,0),(5,0),4)
    print(p3y)
    