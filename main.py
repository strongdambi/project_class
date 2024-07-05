from tabulate import tabulate

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"Name: {self.name}, ID: {self.username}")
        pass

class Post:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def check(self):
        print(f"Title: {self.title}, Content: {self.content}, Author:{self.author}" )







# ----- 코드 실행 ------
members = []
posts = []

# # ----- 인스턴스 ------
m1 = Member("Alice", "alt", "비밀번호1")
m2 = Member("bob", "uncle1", "비밀번호2")
m3 = Member("jay", "jet5", "비밀번호3")

p1 = Post("bg_game", "game is good ", "alt")
p2 = Post("tekken_game", "game is bad", "uncle1")
p3 = Post("python", "study is easy", "jet5")
p4 = Post("out", "movie is bad", "alt")
p5 = Post("21", "movie is soso", "uncle1")
p6 = Post("flask", "study is so difficult", "jet5")
p7 = Post("basketball", "sports is hard", "alt")
p8 = Post("baseball", "sports is cool", "uncle1")
p9 = Post("ping-pong", "sports is funny ", "jet5")
#
members.append(m1)
members.append(m2)
members.append(m3)
posts.append(p1)
posts.append(p2)
posts.append(p3)
posts.append(p4)
posts.append(p5)
posts.append(p6)
posts.append(p7)
posts.append(p8)
posts.append(p9)
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

# name = input("이름을 입력하세요: ")
# username = input("ID를 입력하세요: ")
# password = input("비밀번호를 입력하세요: ")
# members.append(Member(name, username, password))

member_lists = [[member.name, member.username] for member in members]
print(f"유저 목록")
print(tabulate(member_lists,stralign='center', headers=["Name", "ID"], tablefmt='fancy_grid'))

# title = input("제목을 입력하세요: ")
# content = input("내용을 입력하세요: ")
# author = input("아이디를 입력하세요: ")
# posts.append(Post(title, content, author))

post_lists = [[post.title,post.content,post.author] for post in posts]
print(f"글 목록")
print(tabulate(post_lists,stralign='center',headers=["Title", "Content","Author"],tablefmt='fancy_grid'))

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