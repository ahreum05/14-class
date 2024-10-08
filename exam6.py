# 독립된 py 파일에 포함된 변수, 함수, 클래스를 사용하기 위해서는
# import를 해야만 한다.

# 방법1
# import 모듈명
import calcurator
calc = calcurator.Calc()

print(calc.plus(10, 20))
print(calc.minus(10, 20))
print('-' * 20)

# 방법2
# from 모듈명 import 클래스명
from calcurator import Calc
calc = Calc()

print(calc.plus(10, 20))
print(calc.minus(10, 20))
print('-' * 20)
