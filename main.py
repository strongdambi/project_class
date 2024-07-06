import hashlib  # hashlib 모듈 설치
import logging  # logging 모듈 설치
import time  # time 모듈 설치
from tabulate import tabulate

logging.basicConfig(
    format='%(asctime)s :%(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
)  # 로그 포멧팅 레벨 설정


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
# ----- members 리스트를 돌면서 회원들의 이름을 모두 프린트 ------
# for member in members:
#     member.display()
#
# ----- for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 ------
# for post in posts:
#     if post.author == '아이디1':
#         print(post.title)
#
# ----- for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 ------
# word = input("단어 입력: ")
# for post in posts:
#     if word in post.content:
#         print(post.title)

# ----- input을 이용하여 Member, Post 인스턴스 생성 ------

name = input("이름을 입력하세요: ")
username = input("ID를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

m = hashlib.sha256()  # hashlib 코드 작성
m.update(password.encode("utf-8"))
hash_password = m.hexdigest()
members.append(Member(name, username, hash_password))  # append (password > hash_password 로 변경)

member_lists = [[member.name, member.username] for member in members]
print(tabulate(member_lists, headers=["Name", "ID"], tablefmt='fancy_grid'))

time.sleep(0.3)  # 0.3초 간 정지
logging.info("The password has been hashed")  # 로그 메세지
time.sleep(0.3)  # 0.3초 간 정지

title = input("제목을 입력하세요: ")
content = input("내용을 입력하세요: ")
author = input("아이디를 입력하세요: ")
posts.append(Post(title, content, author))
