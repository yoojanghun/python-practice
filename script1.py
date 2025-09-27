from script2 import *       # script2 가 출력됨

print(__name__)             # __main__ 이 출력됨

print()

def favorite_food(food):
    print(f"your favorite food: {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("goodbye")

if __name__ == "__main__":      # script2에서 script1을 import할 때, main()함수는 실행시키지 않는다는 뜻
    main()