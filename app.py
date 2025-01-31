import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# Streamlit 앱 제목
st.title("🎉 생일 축하 이미지 생성기")

# .PY 폴더 경로 설정 (절대 경로)
base_path = r"C:\Users\rkdal\.PY"
template_path = os.path.join(base_path, "image.png")  # 템플릿 이미지 파일 경로
font_path = os.path.join(base_path, "font.ttf")      # 폰트 파일 경로

# 경로 확인 및 파일 존재 여부 확인
if not os.path.exists(template_path):
    st.error(f"템플릿 이미지를 찾을 수 없습니다: {template_path}")
if not os.path.exists(font_path):
    st.error(f"폰트 파일을 찾을 수 없습니다: {font_path}")

# 이름 입력 받기
name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")

# 이미지 생성 버튼
if st.button("이미지 생성"):
    if name.strip() == "":
        st.error("이름을 입력해주세요!")
    else:
        try:
            # 템플릿 이미지 로드
            template_image = Image.open(template_path)
            draw = ImageDraw.Draw(template_image)

            # 폰트 설정
            font_size = 100  # 폰트 크기
            font = ImageFont.truetype(font_path, font_size)

            # 텍스트 위치 및 색상 설정
            text_color = (27, 88, 132)  # 텍스트 색상 (RGB 형식, 검정색은 (0, 0, 0))

            # 텍스트 크기 계산 (가운데 정렬)
            text_bbox = draw.textbbox((0, 0), name, font=font)  # 텍스트의 경계 상자 계산
            text_width = text_bbox[2] - text_bbox[0]  # 텍스트 너비
            text_height = text_bbox[3] - text_bbox[1]  # 텍스트 높이
            image_width, image_height = template_image.size

            # 텍스트 위치 계산 (가로 중앙 정렬, y 좌표는 200으로 고정)
            text_position = ((image_width - text_width) // 3.2, 515)

            # 텍스트 삽입
            draw.text(text_position, name, font=font, fill=text_color)

            # 이미지 저장
            output_image_path = os.path.join(base_path, f"birthday_{name}.png")
            template_image.save(output_image_path)

            # 생성된 이미지 표시 (use_container_width=True 적용)
            st.image(output_image_path, caption=f"{name}님의 생일 축하 이미지", use_container_width=True)

            # 이미지 다운로드 링크 제공
            with open(output_image_path, "rb") as file:
                st.download_button(
                    label="이미지 다운로드",
                    data=file,
                    file_name=f"birthday_{name}.png",
                    mime="image/png"
                )
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {str(e)}")

