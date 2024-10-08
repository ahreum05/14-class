class HelloWorld :
    message = "Python!!!"   # 클래스 변수
    
    def setEng(self) :
        self.message = "Hello Python"  # 인스턴스 변수
        
    def setKor(self) :
        self.message = "안녕하세요 파이썬"
        
    def setKor2(self) :
        message = "파이썬 파이팅!!"    # 지역변수

    def sayHello(self) :
        global message
        message = '테스트'
        print(HelloWorld.message)   # 클래스 변수
        print(self.message)         # 인스턴스 변수
        print(message)              # 전역 변수
  
# 전역변수
message = "test"
        
hello = HelloWorld()
hello.setEng()
hello.sayHello()
print('-' * 20)

print(message)


        
