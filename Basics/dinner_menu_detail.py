import random

# 딕셔너리 형태 (dict) - value 개수가 다를 수 있음
dinner_menu_dict = {
    '스테이크': {'가격': 25000, '칼로리': 550, '종류': '양식'},
    '파스타': {'가격': 12000, '칼로리': 480, '종류': '이탈리안', '조리시간': 15},
    '피자': {'가격': 18000, '칼로리': 600},
    '부리또': {'가격': 9000, '칼로리': 520, '종류': '멕시칸'},
    '짜장면': {'가격': 5500, '칼로리': 650, '종류': '중국음식'},
    '된장찌개': {'가격': 8000, '칼로리': 380, '종류': '한식', '추천': True}
}

# 랜덤하게 메뉴 선택
selected_menu = random.choice(list(dinner_menu_dict.keys()))
menu_info = dinner_menu_dict[selected_menu]

print(f"오늘 저녁 메뉴는? {selected_menu}")

# get() 메서드로 안전하게 접근 - key가 없으면 '정보 없음' 표시
print(f"  가격: {menu_info.get('가격', '정보 없음')}원")
print(f"  칼로리: {menu_info.get('칼로리', '정보 없음')}kcal")
print(f"  종류: {menu_info.get('종류', '정보 없음')}")
print(f"  조리시간: {menu_info.get('조리시간', '정보 없음')}")
print(f"  추천: {menu_info.get('추천', '정보 없음')}")
