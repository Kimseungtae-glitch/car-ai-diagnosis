# 🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 웹 서비스
> **2026학년도 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP**  
> **기술 자문 및 공동 개발 파트너:** `김승태 (미래자동차학과)` , `Gemini (AI)`

<br>

## 📌 프로젝트 개요 (Project Overview)
본 프로젝트는 무인 카셰어링 서비스 및 미래 자율주행 차량 관제 환경에서 대여 전후의 차량 외관 상태를 사용자가 스스로 진단하고, 이를 **V2X(Vehicle-to-Everything)** 관제 서버와 연동하여 무인 반납 및 사후 관리 프로세스를 자동화하는 **인공지능 기반 통합 검수 플랫폼 프로토타입(MVP)**입니다.

<br>
🌐 서비스 접속 주소 (Live Demo)
본 서비스는 스트림릿 클라우드(Streamlit Cloud)를 통해 전 세계 어디서나 접속 가능한 퍼블릭 환경에 배포되어 있습니다.

웹 서비스 URL: https://car-ai-diagnosis-kfvs9gcyxjgtsocrni6fmy.streamlit.app/

시연용 테스트 계정: ID: seungtae / PW: 1234

<br>

## 🛠️ 기술 스택 (Tech Stacks)
깃허브와 스트림릿 환경에 최적화된 경량화 웹 및 AI 기술 스택을 활용하여 기동성 있는 MVP를 구축했습니다.

| 분류 | 기술 배지 (Tech Badges) |
| :--- | :--- |
| **Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) |
| **AI Engine** | ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| **Tools** | ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) |

<br>

## 🌟 6단계 연동 시나리오 및 핵심 기능 (6-Phase Key Features)

본 서비스는 보안 인증부터 사후 조치까지 총 6단계의 유기적인 자동화 프로토콜로 작동합니다.

### 1️⃣ 🔒 Phase 1: 자율주행 V2X 관제 시스템 연동 로그인
* 무인 차량 단말기 제어를 시뮬레이션하기 위한 Connected Car ID 및 패스워드 인증 시스템 구축
* **🔑 시연용 테스트 계정:** `ID: seungtae` / `PW: 1234`

### 2️⃣ 🚨 Phase 2: 스마트 검수 모드 활성화 (헤드라이트 동기화)
* 관제 시스템 로그인 인증 성공 시, 대기 상태였던 차량의 헤드라이트 그래픽이 켜지며 실시간으로 스마트 검수 UI가 활성화됩니다.

### 3️⃣ 🤖 Phase 3: 실시간 AI 딥러닝 연산 엔진 구동
* Google Teachable Machine 기반으로 사전 학습된 정밀 가중치 모델(`model.json`, `metadata.json`, `weights.bin`) 탑재
* 웹 브라우저 단에서 이미지 픽셀 패턴을 실시간 분석하여 **[정상/파손]** 상태를 완벽 분별하며, 클래스별 일치율을 정량적 수치(%)로 시각화

### 4️⃣ 📊 Phase 4: 실시간 비즈니스 로직 분기
* AI의 상태 진단 데이터 결과에 따라 시스템 백엔드에서 정상 상태와 파손 상태의 제어 프로세스를 즉각 동적 분기합니다.

### 5️⃣ 🔑 Phase 5-A: [정상 판정 시] 디지털 스마트키 제어 시뮬레이션
* 차량 무결성이 검증되면 화면에 **[디지털 스마트키 활성화]** 버튼이 동적 생성됩니다. 클릭 시 사용자의 디바이스로 가상 제어권이 발급되어 도어가 언락(Unlock)되는 제어 단계를 시뮬레이션합니다.

### 6️⃣ 🛠️ Phase 5-B & 6: [파손 판정 시] 긴급 경고 및 외부 정비 인프라 연동
* 스크래치나 손상 감지 시 화면이 즉각 빨간색 경고창으로 전환됩니다. 이와 동시에 사용자의 현장 처리를 돕는 **[현대자동차 사고센터 접수 및 서비스 예약하기]** 버튼이 동적 표출되어, 실제 현대차 정비 서비스 페이지와 실시간 연동됩니다.

<br>

## 💥 5. 개발 과정 및 트러블슈팅 (Troubleshooting)

### 💻 이종(異種) 언어 간 기종 연동 및 가중치 경로 오류 극복
* **문제 상황:** 구글 티처블 머신이 배포하는 기본 코드는 웹 브라우저용 HTML/JavaScript 기반이었으나, 본 프로젝트의 메인 프레임워크는 파이썬 기반의 Streamlit이었습니다. 이로 인해 두 환경을 결합하는 과정에서 연동 에러가 발생했으며, 로컬 환경에서 가중치 파일들(`model.json`, `weights.bin`)을 올바르게 로드하지 못해 웹 화면이 멈추는 현상이 반복되었습니다.
* **해결 방법:** Streamlit의 컴포넌트 API를 활용해 JavaScript와 Python 간의 데이터 브릿지를 구축했습니다. 또한 절대 경로와 상대 경로의 디버깅을 거쳐 로컬 런타임 내에서 AI 연산 엔진이 에러 없이 구동되도록 연동에 성공했습니다.

<br>
## 6. 결론 및 향후 발전 계획 (Future Roadmap)

본 프로젝트는 제한된 기간 내에 비즈니스 모델의 가능성을 검증하기 위해 MVP(최소 기능 제품) 형태로 개발되었으나, 향후 실무 관제 플랫폼으로 도입되기 위해 아래와 같은 2단계 고도화 로드맵을 추진할 계획입니다.

### 🚀 Phase 1: 입력 데이터 예외 처리(Exception Handling) 및 안정성 확보 (단기 과제)
* **문제점:** 현재 모델은 차량이 아닌 엉뚱한 이미지(인물, 풍경 등)가 업로드되어도 이를 필터링하지 못하고 '정상/파손' 중 하나로 강제 분류하는 한계가 있습니다.
* **해결 방안:** 이미지 분류(Classification) 전 단계에 **'차량 객체 인식(Vehicle Detection) 필터 레이어'**를 추가할 예정입니다. 
* **기대 효과:** 업로드된 이미지에서 자동차 형태가 감지되지 않으면 *"올바른 차량 사진을 업로드해 주세요"*라는 경고 메시지와 함께 프로세스를 차단하는 예외 처리 코드를 구현하여 전체 시스템의 오작동률을 최소화합니다.

### 👁️ Phase 2: YOLO 기반의 정밀 객체 탐지(Object Detection) 전환 (장기 과제)
* **문제점:** 구글 Teachable Machine 기반의 1차원적 이미지 분류는 파손의 유무만 판단할 뿐, 정확히 어느 부위가 얼마만큼 찌그러지거나 긁혔는지 공학적인 정밀 측정이 불가능합니다.
* **해결 방안:** 자율주행 인지 기술의 표준인 **YOLO(You Only Look Once)** 알고리즘을 도입하여 시스템을 전면 고도화할 예정입니다.
* **기대 효과:** 
  1. 차량 외관의 파손 부위에 정확한 **Bounding Box(탐지 상자)**를 생성하여 시각화합니다.
  2. 스크래치, 찌그러짐(Dent), 파손(Shattered) 등 손상 유형별로 클래스를 세분화하여 동적 인지를 수행합니다.
  3. 손상의 픽셀 크기 추적 기능을 추가하여 파손 심각도를 등급별로 수량화하고, 이를 기반으로 수리비 견적까지 자동 산출하는 차세대 모빌리티 관제 인프라 플랫폼으로 확장하고자 합니다.

<br>
## 🏃‍♂️ 실행 방법 (How to Run)

### 1) 필수 라이브러리 설치
터미널(Terminal) 또는 명령 프롬프트(CMD)를 열고 아래 명령어를 입력하여 웹 구동에 필요한 라이브러리를 설치합니다.
```bash
pip install streamlit
