class Calc :
    # 스테틱 메소드 : self 없이 만들어진 함수
    # 클래스명.함수명() 으로 사용
    # 객체 생성없이 사용
    @staticmethod
    def plus(x, y) :
        print('staticmethod 호출')
        return x + y
    @staticmethod
    def minus(x, y) :
        return x - y
    
''' 
    # 같은 블럭에서는 같은 이름의 함수를 사용하는 것은 피해야함
    def plus(self, x, y) :
        print('instancemethod 호출')
        return x + y
'''    
print(Calc.plus(10, 20))
print(Calc.minus(10, 20))
print('-' * 20)

calc = Calc()
print(calc.plus(10, 20))
print(calc.minus(10, 20))
