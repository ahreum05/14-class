class Gugudan:
    def setGugudan(self, s, e):
        self.s = s
        self.e = e
        
    def dispGugudan(self):
        for i in range(self.s, self.e + 1):  # 단
            for j in range(1, 10):           # 1~9
                print("{}*{}={:2}".format(i, j, i*j), end=" ")
            print()

gugudan = Gugudan()

s = int(input('시작단 : '))
e = int(input('끝단 : '))

gugudan.setGugudan(s, e)
gugudan.dispGugudan()