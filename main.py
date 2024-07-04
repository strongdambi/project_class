# ----- 코드 정의 ------ branch
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"이름: {self.name}, ID: {self.username}")
        pass


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# ----- 코드 실행 ------
members = []
posts = []

# # ----- 인스턴스 ------
# m1 = Member("이름1", "아이디1", "비밀번호1")
# m2 = Member("이름2", "아이디2", "비밀번호2")
# m3 = Member("이름3", "아이디3", "비밀번호3")
# p1 = Post("제목1", "내용1", "아이디1")
# p2 = Post("제목2", "내용2", "아이디2")
# p3 = Post("제목3", "내용3", "아이디3")
# p4 = Post("제목4", "내용4", "아이디4")
# p5 = Post("제목5", "내용5", "아이디5")
# p6 = Post("제목6", "내용6", "아이디6")
# p7 = Post("제목7", "내용7", "아이디7")
# p8 = Post("제목8", "내용8", "아이디8")
# p9 = Post("제목9", "내용9", "아이디9")
#
# members.append(m1)
# members.append(m2)
# members.append(m3)
# posts.append(p1)
# posts.append(p2)
# posts.append(p3)
# posts.append(p4)
# posts.append(p5)
# posts.append(p6)
# posts.append(p7)
# posts.append(p8)
# posts.append(p9)
#
# for post in posts:
#     if post.author == '아이디1':
#         print(post.title)
#
# word = input("단어 입력: ")
# for post in posts:
#     if word in post.content:
#         print(post.title)

# ----- input을 이용하여 Member, Post 인스턴스 생성 ------

name = input("이름을 입력하세요: ")
username = input("ID를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")
members.append(Member(name, username, password))

title = input("제목을 입력하세요: ")
content = input("내용을 입력하세요: ")
author = input("아이디를 입력하세요: ")
posts.append(Post(title, content, author))

# # 여기서부터 아래 끝까지 드래그 한 후 ctrl+/ 하고 보시면 잘 보입니다!!
#
# # ----- hashlib 라이브러리를 써서 회원 비밀번호를 해시화 ------
# import hashlib
#
# # Prompt the user to enter a string
# user_input = input("Enter a string to hash: ")
#
# # Create a hash object for SHA-256
# hash_object = hashlib.sha256()
#
# # Update the hash object with the user's input (encoded to bytes)
# hash_object.update(user_input.encode())
#
# # Get the hexadecimal representation of the hash
# hash_hex = hash_object.hexdigest()
#
# # Print the hash
# print(f"The SHA-256 hash of '{user_input}' is: {hash_hex}")
#
# # ----- hashlib 라이브러리를 써서 회원 비밀번호를 해시화 ------
# from tabulate import tabulate
#
# data = [
#     {"Name": "Alice", "Age": 30, "City": "New York"},
#     {"Name": "Bob", "Age": 24, "City": "Los Angeles"},
#     {"Name": "Charlie", "Age": 29, "City": "Chicago"}
# ]
#
# print(tabulate(data, headers="keys", tablefmt="grid"))