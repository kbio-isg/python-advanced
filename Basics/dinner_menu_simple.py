import random

# 리스트 형태 (list)
dinner_menu_list = ['스테이크', '파스타', '피자', '부리또', '짜장면', '된장찌개']
random_menu = dinner_menu_list[random.randint(0, len(dinner_menu_list) - 1)]

print(f"오늘 저녁 메뉴는? {random_menu}")
