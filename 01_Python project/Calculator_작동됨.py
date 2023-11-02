# 계산기 클래스
# -----------------------------------------------------------------------------
class Calculator():

    def __init__(self,_maker, _model):
        self.__maker=_maker
        self.__model=_model

    @property
    def maker(self): self.__maker
    @property
    def model(self): self.__model


    def showInfo(self):
        print(f'====계산기 정보====\n|  제조사: {self.maker}   \n|  모델명: {self.model}   \n{"="*19}')
        print()
    
    @classmethod
    def plus(cls,num1, num2):
        return num1+num2
    @classmethod
    def minus(cls,num1, num2):
        return num1-num2
    @classmethod
    def multi(cls,num1,num2):
        return num1*num2
    @classmethod
    def divide(cls,num1,num2):
        return num1*num2


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# 계산기 프로그램
while True:

    # 계산기 정보
    Cal=Calculator('CASIO','FX-570EX')
    Cal.showInfo()
    
    # 계산기 실행1
    star_end1=input("계산기를 실행하시겠습니까?\n\n1.시작\n2.종료\n번호입력:")
    print()
    if star_end1=="2":
        break
    else:

        # 계산기 실행2
        while True:
            star_end2=input(f"{'-'*30}\n진행하실 과정을 선택하세요.\n\n1.덧셈\n2.뺄셈\n3.곱셈\n4.나눗셈\n5.종료\n입력:")
            print()

            # 덧셈
            if star_end2=="1":
                try:
                    num1,num2=map(float,input(f"{'-'*30}\n수식을 입력하세요(예시: 1+2): ").split("+"))
                    print()
                    print(f'=> 결과: {num1}+{num2}= {Cal.plus(num1,num2)}')
                    print()                    

                except Exception as e:
                    print()
                    print(f'ERROR: {e}\n잘못된 입력입니다.')
                    print()
                    continue

            # 뺄셈
            elif star_end2=="2":
                try:
                    num1,num2=map(float,input(f"{'-'*30}\n수식을 입력하세요(예시: 1-2): ").split("-"))
                    print()
                    print(f'=> 결과: {num1}-{num2}= {Cal.minus(num1,num2)}')
                    print()                    

                except Exception as e:
                    print()
                    print(f'ERROR: {e}\n잘못된 입력입니다')
                    print()
                    continue

            # 곱셈
            elif star_end2=="3":
                try:
                    num1,num2=map(float,input(f"{'-'*30}\n수식을 입력하세요(예시: 1*2): ").split("*"))
                    print()
                    print(f'=> 결과: {num1}*{num2}= {Cal.multi(num1,num2)}')
                    print()                    

                except Exception as e:
                    print()
                    print(f'ERROR: {e}\n잘못된 입력입니다')
                    print()
                    continue
            
            #나눗셈
            elif star_end2=="4":
                try:
                    num1,num2=map(float,input(f"{'-'*30}\n수식을 입력하세요(예시: 1%2): ").split("%"))
                    print()
                    print(f'=> 결과: {num1}%{num2}= {Cal.divide(num1,num2)}')
                    print()                    

                except Exception as e:
                    print()
                    print(f'ERROR: {e}\n잘못된 입력입니다')
                    print()
                    continue
            
            else:
                break
    break
print(f"{'-'*30}\n계산기를 종료합니다.")



