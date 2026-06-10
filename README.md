# 🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 웹 서비스
> **2026 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP**  
> *본 프로젝트는 대화형 AI 'Gemini'와 공동 기획 및 기술 자문을 통해 개발된 무인 모빌리티 관제 프로토타입입니다.*

---

## 📌 1. 프로젝트 기획 배경 (Introduction)
카셰어링 서비스 및 무인 자율주행 로보택시 시대가 도래함에 따라 **'차량 외관 관리의 사각지대'**가 주요 문제로 부각되고 있습니다. 이전 이용자의 차량 파손 신고 누락으로 인해 발생하는 면책금 분쟁과 사후 검수 비용을 절감하고자, 사용자가 스마트폰 사진 한 장으로 외관을 실시간 검수하고 후속 제어까지 자동 연동하는 **V2X 관제 플랫폼**을 제안합니다.

---

## 🛠️ 2. 기술 스택 및 아키텍처 (Tech Stack)
* **Frontend / Backend:** Python Streamlit
* **AI Engine:** Google Teachable Machine (Deep Learning Image Classification)
* **Runtime Files:** `model.json`, `metadata.json`, `weights.bin`
* **Infrastructure Layer:** JavaScript/HTML Embedded Communication Bridge

---

## ✨ 3. 핵심 기능 (Core Features & Scenario)

### 🔒 Phase 1: 관제 시스템 보안 인증
* 무인 관제 연동형 플랫폼으로서, 승인된 Connected Car ID 및 Access Password 인증을 거쳐야 스마트 검수 모드가 활성화됩니다.

### 📸 Phase 2: AI 이미지 패턴 분석 및 실시간 분기
이미지 데이터 가중치를 연산하여 최상위 일치율(Probability)을 도출하고 비즈니스 로직을 자동 분기합니다.

* **✅ 정상 판정 시:** AI의 무결성 검증 완료 후, 화면에 **[디지털 스마트키 활성화 (차량 도어 열기)]** 버튼이 동적 생성됩니다. 클릭 시 스마트폰으로 가상 키가 발급되어 도어가 언락(Unlock)되는 시뮬레이션을 수행합니다.
* **🚨 파손 판정 시:** 스크래치 및 외관 손상 감지 즉시 경고 시스템이 작동하며, **[현대자동차 사고센터 접수 및 서비스 예약하기]** 버튼이 생성되어 외부 API 예약 페이지와 실시간 연동됩니다.

---

## 🚀 4. 실행 방법 (How to Run)

본 프로젝트를 로컬 환경에서 구동하기 위한 절차입니다.

### 1) 필수 라이브러리 설치
터미널(Terminal) 또는 명령 프롬프트(CMD)를 열고 아래 명령어를 입력하여 웹 구동에 필요한 라이브러리를 설치합니다.
```bash
pip install streamlit
