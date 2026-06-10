# 🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 웹 서비스
> **2026 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP**

<div align="center">
  <!-- 핵심 협업 및 개발 툴 배지 이미지 -->
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75FF?style=for-the-badge&logo=googlegemini&logoColor=white" />
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" />
  <br>
  <!-- 기술 스택 배지 이미지 -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Teachable%20Machine-4285F4?style=for-the-badge&logo=google&logoColor=white" />
</div>

<br>

*본 프로젝트는 대화형 AI 'Gemini'와 프로젝트 파트너로서 공동 기획 및 기술 자문을 통해 프로그래밍 비전공자가 단기간에 빌드해 낸 무인 모빌리티 관제 프로토타입입니다.*

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

## ✨ 3. 전체 관제 프로세스 및 핵심 기능 (6-Phase Scenario)

본 서비스는 사용자가 차량에 탑승하기 전부터 진단 후 사후 조치까지의 전 과정을 총 6단계의 유기적인 자동화 프로토콜로 처리합니다.

### 🔒 Phase 1: 관제 시스템 보안 인증 (Authentication)
* 무인 자율주행 차량 및 카셰어링 인프라의 핵심인 보안을 위해, 지정된 Connected Car ID 및 Access Password 입력을 통한 단말기 동기화 인증 단계를 거칩니다.

### 📸 Phase 2: 스마트 검수 모드 활성화 (System Activation)
* 로그인 인증 성공 시, 대기 상태였던 차량 관제 그래픽이 실시간으로 동기화되며 사용자가 스마트폰으로 촬영한 차량 외관 사진을 업로드할 수 있는 대화형 UI 가 구동됩니다.

### 🧠 Phase 3: AI 이미지 패턴 연산 및 분석 (Deep Learning Analytics)
* 임베딩된 딥러닝 가중치 엔진이 업로드된 고해상도 차량 이미지의 픽셀 패턴을 실시간 연산하여, 정밀한 정상/파손 확률(Probability) 가중치를 도출합니다.

### 📊 Phase 4: 실시간 비즈니스 로직 분기 (Decision Making)
* AI 분석 데이터를 바탕으로 시스템이 무결성 검증을 완료합니다. 정상 차량 시나리오와 손상 차량 시나리오로 실시간 시스템 분기가 안전하게 이루어집니다.

### 🔑 Phase 5-A: [정상 판정 시] 디지털 스마트키 활성화 (Vehicle Control)
* 외관이 정상으로 판정되면 화면에 **[디지털 스마트키 활성화]** 버튼이 동적 생성됩니다. 사용자가 이를 클릭하면 스마트폰 디바이스로 가상 차량 제어권이 발급되어 도어가 언락(Unlock)되는 시뮬레이션을 수행합니다.

### 🚨 Phase 5-B: [파손 판정 시] 긴급 경고 시스템 작동 (Incident Alert)
* 스크래치 및 찌그러짐 등 차량 외관 손상이 감지되는 즉시 관제 화면이 붉은색 경고창으로 전환되며, 시스템 백엔드에 파손 로그가 기록되는 긴급 상황 모드가 발동합니다.

### 🛠️ Phase 6: 인프라 연동 및 외부 사후 관리 (External API Connected)
* 파손 경고와 동시에, 사용자가 즉각 처리를 할 수 있도록 **[현대자동차 사고센터 접수 및 서비스 예약하기]** 인프라 연동 버튼이 동적으로 표출되며, 클릭 시 실제 현대차 정비 네트워크 예약 시스템으로 다이렉트 연동됩니다.

---

## 🚀 4. 실행 방법 (How to Run)

본 프로젝트를 로컬 환경에서 구동하기 위한 절차입니다.

### 1) 필수 라이브러리 설치
터미널(Terminal) 또는 명령 프롬프트(CMD)를 열고 아래 명령어를 입력하여 웹 구동에 필요한 라이브러리를 설치합니다.
```bash
pip install streamlit
💥 5. 개발 과정 및 트러블슈팅 (Troubleshooting)
💻 로컬 개발 환경 구축과 기종 간 코드 연동 장벽
문제 상황: 구글 티처블 머신이 제공하는 웹 배포 코드는 브라우저용 HTML/JavaScript 기반이었으나, 프로젝트의 메인 프레임워크는 파이썬 기반의 Streamlit이었습니다. 이로 인해 두 언어의 환경을 깨지지 않게 결합하는 과정에서 연동 에러가 발생했습니다.

해결 방법: Streamlit의 컴포넌트 API를 활용해 이종 언어 간 가상 브릿지를 구축했습니다. 가중치 파일(model.json, weights.bin)을 로컬 경로에서 정확히 로드하지 못해 웹이 멈추는 현상은 절대/상대 경로 디버깅을 통해 파이썬 런타임 내에서 AI 연산 엔진이 정상 작동하도록 해결했습니다.
