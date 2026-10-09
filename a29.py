class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def display(self):
        print('total value:',self.stock)
    def rentbike(self,q):

        if q<=0:
            print('enter more than 0')
        elif q>self.stock:
            print('enter less quantity')
        else:
            self.stock=self.stock-q
            print('total prices',q*100)
            print('total value',self.stock)

while True:
    obj=bikeshop(200)
    a=int(input('''
   1 display bike
   2 rent bike
   3 exit
    '''))

    if a==1:
        obj.display()
    elif a==2:
        b=int(input('enter the quantity'))
        obj.rentbike(b)
    else:
        break













