# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally (예외, 에러 처리를 위한 기본 문법)

# try:
#     # 에러가 발생할 가능성이 있는 코드
# except:
#     # 에러가 발생했을 때 실행되는 코드
# finally:
#     # 에러가 나든 안 나든 항상 실행되는 코드

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't devide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:                               # Exception은 모든 에러를 잡음
    print("Something went wrong!")
finally:
    print("Do some cleanup here")               # 파일 닫기와 같은 cleanup code 실행