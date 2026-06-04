🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 웹 서비스
2026학년도 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP

개발 참여자: 김승태 (미래자동차학과), Gemini (AI 기술 자문)

본 프로젝트는 무인 카셰어링 서비스 및 미래 자율주행 차량 관제 환경에서 대여 전후의 차량 외관 상태를 사용자가 스스로 진단하고, 이를 V2X(Vehicle-to-Everything) 관제 서버와 연동하여 무인 반납 프로세스를 자동화하는 인공지능 기반 통합 검수 플랫폼 프로토타입(MVP)입니다.

🌟 핵심 기능 (Key Features)
1. 🔒 자율주행 V2X 관제 시스템 연동 로그인
무인 차량 단말기 제어를 연출하기 위한 Connected Car ID 및 Access Password 기반의 인증 시스템 구축

시연용 테스트 계정: ID: seungtae / PW: 1234

2. 🚨 5회 연속 인증 실패 시 긴급 보안 락(Lock)
외부 무단 해킹 및 오접근을 차단하기 위한 보안 로직 설계

5회 연속 패스워드 입력 오류 시, 단말기 접근 권한을 일시적으로 완전 차단하고 관제 센터 안내 메시지 표출 (시연용 리셋 버튼 포함)

3. 🤖 HTML5/JavaScript 연동 실시간 AI 딥러닝 연산 엔진
Google Teachable Machine 기반으로 학습된 정밀 가중치 모델(model.json, metadata.json, weights.bin) 탑재

웹 브라우저 단에서 픽셀 패턴을 실시간으로 분석하여 [정상/파손] 상태를 완벽 분별

분석 결과와 함께 AI 모델의 실시간 클래스별 일치율(가중치 데이터)을 정량적 수치(%)로 투명하게 시각화

4. 📞 관제 시스템 후속 조치 프로세스
정상 판정 시: 즉시 무인 반납 승인 트리거 작동

파손 판정 시: 사고 센터 자동 접수 및 V2X 관제 로그 기록 연동 시나리오 구현

🛠️ 기술 스택 (Tech Stacks)
Frontend & Backend Framework: Streamlit (Python 기반 Web App Framework)

AI Engine: TensorFlow.js, Teachable Machine Image Library

Languages: Python, JavaScript, HTML5, CSS3

Environment: VS Code, GitHub

🏃‍♂️ 실행 방법 (How to Run)
필수 라이브러리 설치:

Bash
pip install streamlit
스트림릿 로컬 서버 구동:

Bash
streamlit run app.py
🚀 향후 과제 및 상용화 로드맵 (Future Work)
딥러닝 모델의 고도화: 현재 프로토타입의 단순 이미지 분류(Classification) 단계를 넘어, 파손 부위의 미세 위치와 픽셀을 정밀 추적하는 YOLO 기반 객체 탐지(Object Detection) 및 인스턴스 세그멘테이션(Instance Segmentation) 기술 도입 예정

V2X 차량 센서 데이터 매칭: 차량 내부 섀시/바디에 탑재된 충격 감지 센서(G-Sensor)의 로그 발생 타임스탬프와 사용자가 촬영한 사진 데이터를 결합하여 사고 시점의 신뢰성을 완벽히 검증하는 통합 관제 모듈 확장
