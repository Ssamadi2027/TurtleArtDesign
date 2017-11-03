def spiral(t,r,angle1,angle2):
    for times in range(60):
        t.right(angle1)
        t.circle(r)
        t.left(angle2)
    
def triangle(t,length,angle):
    for times in range(3):
        t.forward(length)
        t.right(angle)
    

