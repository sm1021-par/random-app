import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 메뉴 추천", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 카테고리별 점심 메뉴 데이터
menus = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "제육볶음",
        "비빔밥",
        "순대국밥",
        "불고기",
        "칼국수",
    ],
    "중식": ["짜장면", "짬뽕", "볶음밥", "마라탕", "탕수육 세트"],
    "일식": ["돈가스", "초밥", "라멘", "우동", "규동(소고기덮밥)"],
    "양식/분식": [
        "파스타",
        "수제버거",
        "떡볶이 & 순대",
        "김밥 & 라면",
        "샌드위치",
    ],
}

# 음식 종류 필터링 (다중 선택)
selected_categories = st.multiselect(
    "포함할 음식 종류를 선택하세요:",
    options=list(menus.keys()),
    default=list(menus.keys()),
)

# 추천 버튼
if st.button("🎲 오늘의 점심 메뉴 뽑기!", type="primary"):
  # 아무것도 선택하지 않았을 경우 전체 메뉴를 대상으로 설정
  target_categories = (
      selected_categories if selected_categories else list(menus.keys())
  )

  # 선택된 카테고리의 메뉴들을 하나의 리스트로 합치기
  candidate_menus = []
  for category in target_categories:
    candidate_menus.extend(menus[category])

  # random.choice()로 메뉴 1개 무작위 추출
  chosen_menu = random.choice(candidate_menus)

  # 결과 출력 및 시각 효과
  st.balloons()
  st.success(
      f"오늘의 추천 메뉴는 **{chosen_menu}** 입니다! 맛있게 드세요 😋"
  )
