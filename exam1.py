class Car :
    # 인스턴스 메소드 : 매개변수로 self가 있는 함수
    def set(self) :
        # 인스턴스 변수 : 변수명 앞에 self. 이 있는 변수
        # => 인스턴스 변수가 포함되어있는 함수가 호출되어야만
        #    메모리에 만들어짐
        self.model = 'E-Class'
        self.color = 'blue'
        self.speed = 10
        print(self)
        
    def drive(self) :
        self.speed = 20
        
    def output(self) :
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

# 객체 생성
myCar = Car()
#myCar.output()  # 에러, 아직 인스턴스 변수가 존재하지 않기 때문
print('-' * 20)

myCar.set()  # myCar.set(myCar)
print(myCar)
# 저장된 데이터 확인
myCar.output()
print('-' * 20)

# 저장된 데이터 확인
print('모델 :', myCar.model)
print('색상 :', myCar.color)
print('속도 :', myCar.speed)
print('-' * 20)

# 데이터 변경
myCar.drive()
myCar.output()
print('-' * 20)
# 객체명.변수명으로 인스턴스 변수를 직접 사용할 수도 있다.
myCar.model = 'F-Class'
myCar.color = 'red'
myCar.speed = 50
myCar.output()
print('-' * 20)

# 인스턴스 변수 추가
myCar.maker = 'Benz'
print('제조사 :', myCar.maker)
print('모델 :', myCar.model)
print('색상 :', myCar.color)
print('속도 :', myCar.speed)
print('-' * 20)
