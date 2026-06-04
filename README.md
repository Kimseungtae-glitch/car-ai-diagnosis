# 🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 웹 서비스
> **2026학년도 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP**
> **기술 자문 및 공동 개발 파트너:** `김승태 (미래자동차학과)` , `Gemini (AI)`

<br>

## 📌 프로젝트 개요 (Project Overview)
본 프로젝트는 무인 카셰어링 서비스 및 미래 자율주행 차량 관제 환경에서 대여 전후의 차량 외관 상태를 사용자가 스스로 진단하고, 이를 **V2X(Vehicle-to-Everything)** 관제 서버와 연동하여 무인 반납 프로세스를 자동화하는 **인공지능 기반 통합 검수 플랫폼 프로토타입(MVP)**입니다.

<br>

## 🛠️ 기술 스택 (Tech Stacks)
프로젝트 구현에 실제 활용된 프론트엔드, 백엔드 및 인공지능 프레임워크 기술 스택입니다.

| 분류 | 기술 배지 (Tech Badges) |
| :--- | :--- |
| **Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) |
| **AI Engine** | ![Google Teachable Machine](https://img.shields.io/badge/Teachable_Machine-4285F4?style=for-the-badge&logo=Google&logoColor=white) ![Gemini](https://img.shields.io/badge/Gemini-9B51E0?style=for-the-badge&logo=Google-Gemini&logoColor=white) |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| **Tools** | ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) |

<br>

## 🌟 핵심 기능 (Key Features)

### 1️⃣ 🔒 자율주행 V2X 관제 시스템 연동 로그인
* 무인 차량 단말기 제어를 시뮬레이션하기 위한 Connected Car ID 및 패스워드 인증 시스템 구축
* **🔑 시연용 테스트 계정:** `ID: seungtae` / `PW: 1234`

### 2️⃣ 🚨 5회 연속 인증 실패 시 긴급 보안 락 (Lock)
* 외부 무단 해킹 및 오접근을 차단하기 위한 보안 세션 인프라 설계
* 5회 연속 패스워드 입력 오류 시, 단말기 접근 권한을 일시적으로 완전 차단하고 관제 센터 안내 메시지 강제 표출 *(시연 편의를 위한 백도어 리셋 버튼 탑재)*

### 3️⃣ 🤖 실시간 AI 딥러닝 연산 엔진
* 구글 티처블 머신(Google Teachable Machine) 기반으로 사전 학습된 정밀 가중치 모델(`model.json`, `metadata.json`, `weights.bin`) 탑재
* 웹 브라우저 단에서 픽셀 패턴을 실시간으로 분석하여 **[정상/파손]** 상태를 완벽 분별
* 분석 결과와 함께 AI 모델의 실시간 클래스별 일치율(가중치 데이터)을 정량적 수치(%)로 투명하게 시각화

### 4️⃣ 📞 관제 시스템 후속 조치 프로세스
* **🟢 정상 판정 시:** 즉시 무인 반납 승인 트리거 작동
* **🔴 파손 판정 시:** 사고 센터 자동 접수 및 V2X 관제 로그 기록 연동 시나리오 구현

<br>

## 🏃‍♂️ 실행 방법 (How to Run)

1. **필수 라이브러리 설치:**
   ```bash
   pip install streamlit
