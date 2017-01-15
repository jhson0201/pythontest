
import random

한식=["양촌리", "한그릇잡수고가요", "삼거리횟집"]

중식=["북경반점", "양꼬치엔칭다오", "라이라이해~"]

일식=["이럇샤이마세", "회전초밥", "가츠우동"]

a=input("한식, 중식, 일식 중에 뭘로 드릴까요? ")

if a == "한식":
    print(random.choice(한식))

elif a == "중식":
    print(random.choice(중식))

else:
    print(random.choice(일식))
