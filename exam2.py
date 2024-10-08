class Car :
    # 클래스 변수
    # 객체가 여러개 만들어져도 변수는 1개만 생성됨
    # => 모든 객체가 공통으로 사용하는 변수
    maker = 'Benz'     
    
    def set(self) :        
        self.model = 'E-Class'
        self.color = 'blue'
        self.speed = 10
        
    def output(self) :
        print('제조사 :', Car.maker)
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

print('제조사 :', Car.maker)
print('-' * 20)

myCar = Car()
myCar.set()
myCar.output()
