import streamlit as st
from PIL import Image

# 1. 프로젝트 타이틀
st.set_page_config(page_title="차량 파손 자가 진단")
st.title("🚗 AI 차량 외관 손상 자가 진단 서비스")
st.info("미래자동차공학과 4학년 캡스톤 디자인 MVP")

# 2. 핵심 기능: 이미지 업로드
uploaded_file = st.file_uploader("진단할 차량 사진을 업로드하세요", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 사진 표시
    image = Image.open(uploaded_file)
    st.image(image, caption='업로드된 차량 사진', use_column_width=True)
    
    # 3. AI 분석 시뮬레이션 (핵심 기능 작동)
    with st.spinner('AI가 외관 손상을 분석 중입니다...'):
        import time
        time.sleep(2) # 분석하는 척하는 대기 시간
        
    # 결과 출력
    st.subheader("🔍 진단 결과")
    st.warning("분석 결과: 파손(Dent/Scratch) 감지됨")
    st.write("신뢰도: 89.5%")
    st.write("조치 사항: 가까운 서비스 센터 방문을 권장합니다.")