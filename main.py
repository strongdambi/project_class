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
        self.password = self.hash_password(password)

    def hash_password(self, password):  # 비밀번호 해시화
        m = hashlib.sha256()
        m.update(password.encode('utf-8'))
        return m.hexdigest()

    def check_password(self, password):  # 해쉬화된 비밀번호 확인
        m = self.hash_password(password)
        return m == self.password

    def display(self):
        print(f"Name: {self.name}, ID: {self.username}")
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
m1 = Member("Alice", "alt", "비밀번호1")
m2 = Member("bob", "uncle1", "비밀번호2")
m3 = Member("jay", "jet5", "비밀번호3")

p1 = Post("bg_game", "game is good", m1)
p2 = Post("tekken_game", "game is bad", m2)
p3 = Post("python", "study is easy", m3)
p4 = Post("out", "movie is bad", m1)
p5 = Post("21", "movie is soso", m2)
p6 = Post("flask", "study is so difficult", m3)
p7 = Post("basketball", "sports is hard", m1)
p8 = Post("baseball", "sports is cool", m2)
p9 = Post("ping-pong", "sports is funny ", m3)

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

while True:
    print("\n[작업 목록]\n1. 계정 추가\n2. 유저 목록\n3. 게시글 목록\n4. 게시글 작성\n5. 게시글 삭제\n그외. 종료")  # 작업 5를 추가해 글 삭제 기능을 구현
    select = input("원하는 작업을 선택하세요: ")
    if select == '1':  # 계정 생성
        print("\n[계정 생성]")
        name = input("이름: ")
        username = input("ID: ")
        password = input("PS: ")
        members.append(Member(name, username, password))
        print("계정 생성 완료!")

        time.sleep(0.3)  # 0.3초 간 정지
        logging.info("The password has been hashed!")  # 암호화 확인 로그 메시지
        time.sleep(0.3)  # 0.3초 간 정지

    elif select == '2':  # 유저 목록 확인
        print("\n[유저 목록]")
        user_table = []
        for member in members:
            user_table.append([member.name, member.username])
        print(tabulate(user_table,
                       stralign='center',
                       headers=['Name', 'ID'],
                       tablefmt='fancy_grid')
              )

    elif select == '3':  # 글 목록 확인
        post_table = []
        for post in posts:
            post_table.append([post.title, post.author.username, post.content])
        print(tabulate(post_table,
                       stralign='center',
                       headers=['Title', 'Author', 'Contnet'],
                       tablefmt='fancy_grid')
              )
        # word 검색
        post_search = input("키워드를 입력하세요. ")
        print("\n키워드를 포함한 게시글 입니다.")
        post_search_table = []
        for post in posts:
            if post_search in post.content:
                post_search_table.append([post.title, post.author.username, post.content])
        if post_search_table:
            print(tabulate(post_search_table,
                           stralign='center',
                           headers=['Title', 'Author', 'Contnet'],
                           tablefmt='fancy_grid')
                  )
        else:
            print("키워드를 포함한 게시글이 없습니다.")

        # username 검색
        post_user_search = input("ID를 입력하세요. ")
        print(f"\n{post_user_search}가 포스팅한 게시글 입니다.")
        post_user_search_table = []
        for post in posts:
            if post_user_search == post.author.username:
                post_user_search_table.append([post.title, post.author.username, post.content])
        if post_user_search_table:
            print(tabulate(post_user_search_table,
                           headers=['Title', 'Author', 'Contnet'],
                           stralign='center',
                           tablefmt='fancy_grid'))
        else:
            print("조회된 게시글이 없습니다.")

    elif select == '4':  # 게시글 작성
        while True:
            id_input = input("ID를 입력해주세요. ")
            member_matched = None
            for member in members:
                if id_input == member.username:
                    member_matched = member
                    break
            if member_matched:
                while True:
                    ps_input = input("패스워드를 입력해주세요. ")
                    if member_matched.check_password(ps_input):  # 인풋 == 해싱된 비밀번호 확인
                        print("게시글을 작성해주세요.")
                        title = input("\n제목: ")
                        content = input("내용: ")
                        posts.append(Post(title, content, member_matched))
                        print("\n게시글 작성을 완료했습니다.")
                        break
                    else:
                        print("패스워드가 일치하지 않습니다.")
                break
            else:
                print("ID가 존재하지 않습니다. ")

    elif select == '5':  # 게시글 삭제
        del_title = input("삭제할 게시글의 제목을 입력하세요. ")
        post_matched = None
        for post in posts:
            if del_title == post.title:
                post_matched = post
                break
        if post_matched:
            while True:
                id_input = input("ID를 입력해주세요. ")
                if id_input == post_matched.author.username:
                    while True:
                        ps_input = input("패스워드를 입력해주세요. ")
                        if post_matched.author.check_password(ps_input):  # 인풋 == 해싱된 비밀번호 확인
                            posts.remove(post_matched)
                            print(f'{post_matched.title}이 삭제되었습니다.')
                            break
                        else:
                            print("패스워드가 일치하지 않습니다.")
                    break
                else:
                    print("아이디가 일치하지 않습니다.")
        else:
            print("삭제할 게시글이 없습니다.")

    else:  # 위에 없는 내용이 입력될 시 종료
        print("종료합니다.")
        break
