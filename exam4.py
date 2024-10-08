def plus(x, y):
    print("함수 plus() 호출")
    return x+y

class Calc :
    def plus(self, x, y) :
        print("메소드 plus() 호출")
        return x+y

    def f(self, x, y) :
        r1 = plus(x, y)
        r2 = self.plus(x, y)
        return r1 + r2
    
calc = Calc()
print(plus(10, 20))         # 함수 호출
print(calc.plus(10, 20))    # 메소드 호출
print('-' * 20)

print(calc.f(10, 20))