class Rectangle:
    def init(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def lt(self,other):
        return self.area()>other.area()
    l1=int(input("enter the length of first rectangle:"))
    w1=int(input("enter the width of first rectangle:"))
    rectangle1=(11,w1)
    l2=int(input("enter the length of second rectangle :"))
    w2=int(input("enter the width of second rectangle:"))
    rectangle2=(12,w2)
    if rectangle1<rectangle2:
        print("area of rectangle 1 is smaller")
    else:
        print("area of rectangle 2 is smaller")
