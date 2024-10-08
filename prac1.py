class Triangle :
    def setTriangle(self, b, h) :
        self.base = b
        self.height = h
        
    def inputTriangle(self) :
        self.base = int(input('밑변 : '))
        self.height = int(input('높이 : '))
        
    def getArea(self) :
        return self.base * self.height / 2

print('***** 삼각형 넓이 구하기 *****')
#b = int(input('밑변 : '))
#h = int(input('높이 : '))

t = Triangle()
t.inputTriangle()
#t.setTriangle(b, h)

print('삼각형의 넓이 :', t.getArea())


