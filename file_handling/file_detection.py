# os와 python이 상호작용하기 위한 라이브러리
import os

file_path = "./test/test.txt"           # 상대 경로 사용
                                        # C:\\Users\\HP\\Desktop\\test.txt 와 같은 절대 경로도 사용 가능
                                        # 단 절대 경로에서 \ 는 특수문자이므로 escape 문자를 사용해 \\ 로 작성
                                        # 또는 C:/Users/HP/Desktop/test.txt 처럼 작성

if os.path.exists(file_path):           # bool 값 반환
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file! Not a directory(folder)")
    elif os.path.isdir(file_path):
        print("that is a directory(folder)")
else:
    print("That location doesn't exist")