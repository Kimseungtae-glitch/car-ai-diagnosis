import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 설정
st.set_page_config(page_title="차량 외관 손상 자가 진단", layout="centered")

# 글로벌 CSS (스트림릿 기본 배경, 여백 및 버튼 스타일 디자인)
st.markdown("""
    <style>
    .main .block-container { padding-top: 1rem; padding-bottom: 2rem; }
    h1 { color: #1e293b; font-weight: 800; letter-spacing: -0.05em; }
    
    /* 로그인 버튼 스타일링 */
    div.stButton > button {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 8px;
        background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%) !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 14px !important;
        box-shadow: 0 4px 6px -1px rgba(251,191,36,0.3);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px -1px rgba(251,191,36,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 💡 스트림릿 메모리에 로그인 상태 및 '로그인 실패 횟수' 저장 변수 초기화
if "car_authenticated" not in st.session_state:
    st.session_state.car_authenticated = False
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0


# ==========================================
# [화면 1] 로그인 및 인증 전 화면
# ==========================================
if not st.session_state.car_authenticated:
    
    # 세련된 미래형 자동차 전면부 디자인 (헤드라이트 꺼진 대기 상태)
    car_visual_html = """
    <div style="font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; background-color: #0f1115; padding: 40px 25px; border-radius: 16px; box-shadow: inset 0 0 20px rgba(0,0,0,0.6); margin-bottom: 10px;">
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; position: relative; width: 160px; height: 100px;">
            <div style="position: relative; width: 140px; height: 55px; background: linear-gradient(180deg, #334155 0%, #1e293b 100%); border-radius: 20px 20px 12px 12px; border: 1px solid #475569;">
                <div style="width: 100px; height: 18px; background: #0f172a; margin: 6px auto 0 auto; border-radius: 8px 8px 3px 3px; opacity: 0.8;"></div>
                <div style="position: absolute; bottom: 12px; left: 12px; width: 22px; height: 8px; background: #64748b; border-radius: 2px 6px 3px 3px;"></div>
                <div style="position: absolute; bottom: 12px; right: 12px; width: 22px; height: 8px; background: #64748b; border-radius: 6px 2px 3px 3px;"></div>
                <div style="width: 50px; height: 4px; background: #1e293b; margin: 8px auto 0 auto; border-radius: 2px;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; width: 110px; margin-top: -2px;">
                <div style="width: 20px; height: 8px; background: #0f172a; border-radius: 2px;"></div>
                <div style="width: 20px; height: 8px; background: #0f172a; border-radius: 2px;"></div>
            </div>
        </div>
    </div>
    """
    components.html(car_visual_html, height=160)
    
    st.markdown("<h3 style='text-align: center; color: #1e293b; margin-top:10px;'>🔒 자율주행 V2X 관제 시스템 인증</h3>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>본 서비스는 무인 관제 연동형 플랫폼입니다. 차량 ID와 패스워드를 입력해 주세요.</p>", unsafe_allow_html=True)
    
    # 💡 5번 이상 틀렸는지 확인하여 입력창 차단 여부 결정
    is_locked = st.session_state.login_attempts >= 5
    
    # 5번 이상 틀리면 입력창이 잠김(disabled=True) 상태가 됩니다.
    user_id = st.text_input("Connected Car ID", placeholder="아이디를 입력하세요 (시연용: seungtae)", disabled=is_locked)
    user_pw = st.text_input("Access Password", type="password", placeholder="비밀번호를 입력하세요 (시연용: 1234)", disabled=is_locked)
    
    # 현재 로그인 실패 횟수 실시간 표시 (1번 이상 틀렸을 때만 안내)
    if 0 < st.session_state.login_attempts < 5:
        st.warning(f"⚠️ 인증 실패 경고: 현재 연속 {st.session_state.login_attempts}/5회 실패했습니다. 5회 실패 시 시스템이 잠깁니다.")
    
    # 💡 5번 이상 틀렸을 때 표출되는 문구 및 로직
    if is_locked:
        st.error("""
        ### 🚨 관제 시스템 긴급 보안 위반 경고 (Access Denied)
        * **사유:** V2X 인증 패스워드 5회 연속 오류 초과
        * **조치:** 외부 무단 해킹 시도로 간주되어 해당 커넥티드 카 단말기의 접근 권한이 **일시적으로 완전 차단(Lock)** 되었음을 안내해 드립니다.
        * **해제 방법:** 관리자 관제 센터에 문의하여 모바일 보안 서명(OTP) 인증을 다시 수행해 주십시오.
        """)
        
        # 잠금 해제용 시연 치트키 버튼
        if st.button("🔄 시연용 잠금 리셋 (발표자 초기화 툴)"):
            st.session_state.login_attempts = 0
            st.rerun()
            
    else:
        # 5번 미만일 때만 활성화되는 로그인 버튼
        if st.button("🚀 관제 시스템 시동 및 스마트 검수 모드 활성화"):
            if user_id == "seungtae" and user_pw == "1234":
                st.session_state.car_authenticated = True
                st.session_state.login_attempts = 0 # 성공 시 카운트 초기화
                st.rerun()
            elif user_id == "" or user_pw == "":
                st.warning("⚠️ 아이디와 비밀번호를 모두 입력해 주세요.")
            else:
                st.session_state.login_attempts += 1 # 틀릴 때마다 카운트 1 증가
                st.rerun()


# ==========================================
# [화면 2] 로그인 성공 후 열리는 진짜 차량 진단 화면
# ==========================================
else:
    # 성공 메시지 상단 배치
    st.success("🔓 스마트 락 해제 성공! 헤드라이트가 활성화되었으며 외관 관제 시스템이 정상 작동합니다.")
    
    # 인증 완료된 활성화 헤드라이트 비주얼 (노란 불빛 뿜어내는 디자인)
    car_active_html = """
    <div style="font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; background-color: #0f1115; padding: 30px 25px; border-radius: 16px; box-shadow: inset 0 0 20px rgba(0,0,0,0.6); margin-bottom: 10px;">
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; position: relative; width: 160px; height: 100px;">
            <div style="position: absolute; top: 20px; left: -140px; width: 180px; height: 100px; background: radial-gradient(ellipse at right, rgba(251,191,36,0.35) 0%, rgba(251,191,36,0) 80%); opacity: 1; filter: blur(4px);"></div>
            <div style="position: absolute; top: 20px; right: -140px; width: 180px; height: 100px; background: radial-gradient(ellipse at left, rgba(251,191,36,0.35) 0%, rgba(251,191,36,0) 80%); opacity: 1; filter: blur(4px);"></div>
            
            <div style="position: relative; width: 140px; height: 55px; background: linear-gradient(180deg, #334155 0%, #1e293b 100%); border-radius: 20px 20px 12px 12px; border: 1px solid #fbbf24; box-shadow: 0 0 15px rgba(251,191,36,0.2);">
                <div style="width: 100px; height: 18px; background: #0f172a; margin: 6px auto 0 auto; border-radius: 8px 8px 3px 3px; opacity: 0.8;"></div>
                <div style="position: absolute; bottom: 12px; left: 12px; width: 22px; height: 8px; background: #fbbf24; border-radius: 2px 6px 3px 3px; box-shadow: 0 0 20px 5px rgba(251,191,36,0.8);"></div>
                <div style="position: absolute; bottom: 12px; right: 12px; width: 22px; height: 8px; background: #fbbf24; border-radius: 6px 2px 3px 3px; box-shadow: 0 0 20px 5px rgba(251,191,36,0.8);"></div>
                <div style="width: 50px; height: 4px; background: #1e293b; margin: 8px auto 0 auto; border-radius: 2px;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; width: 110px; margin-top: -2px;">
                <div style="width: 20px; height: 8px; background: #0f172a; border-radius: 2px;"></div>
                <div style="width: 20px; height: 8px; background: #0f172a; border-radius: 2px;"></div>
            </div>
            <span style="color: #fbbf24; font-size: 10px; margin-top: 8px; font-weight: 600;">🟢 V2X CONNECTED ON</span>
        </div>
    </div>
    """
    components.html(car_active_html, height=150)

    # 진짜 메인 화면 시작
    st.title("🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단")
    st.caption("🏆 2026 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP")
    
    # 촬영 가이드라인 안내 상자
    st.info("""
    **📸 AI 진단 정확도를 높이는 촬영 가이드**
    * 차량의 정면/측면이 **수평**이 되도록 촬영해 주세요.
    * 야간이나 어두운 지하 주차장보다는 **밝은 조명 아래**가 가장 정확합니다.
    * 파손 부위가 잘 보이도록 **1m 내외의 적정 거리**에서 촬영해 주세요.
    """)

    # 서버 파일 검증 및 로드 구역
    required_files = ["model.json", "metadata.json", "weights.bin"]
    missing_files = [f for f in required_files if not os.path.exists(f)]

    if missing_files:
        st.error(f"⚠️ 서버에 필수 AI 파일이 누락되었습니다: {', '.join(missing_files)}")
    else:
        with open("model.json", "r", encoding="utf-8") as f:
            model_json = f.read()
        with open("metadata.json", "r", encoding="utf-8") as f:
            metadata_json = f.read()
        with open("weights.bin", "rb") as f:
            weights_bin = f.read().hex()

        html_code = """
        <div style="font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; padding: 25px; border: 1px solid #e2e8f0; border-radius: 16px; background-color: #ffffff; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05); margin-top: 15px;">
            
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px; margin-bottom: 20px;">
                <h4 style="margin: 0; color: #0f172a; font-size: 19px; font-weight: 700;">🤖 AI 외관 손상 진단창</h4>
                <span style="font-size: 11px; background: #e2e8f0; color: #475569; padding: 3px 8px; border-radius: 20px; font-weight: 600;">v1.2 현대차 연동</span>
            </div>
            
            <div style="margin-bottom: 20px; background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #edf2f7;">
                <p style="font-size: 13px; color: #334155; margin-top: 0; margin-bottom: 10px; font-weight: 600;">
                    📸 분석할 차량의 외관 사진을 첨부해 주세요.
                </p>
                <input type="file" id="image-selector" accept="image/*" style="font-size: 13px; padding: 10px; background: #ffffff; border-radius: 8px; width: 100%; border: 1px dashed #cbd5e1; box-sizing: border-box; cursor: pointer;">
            </div>
            
            <div id="status-message" style="color: #1e3a8a; font-weight: 700; margin-bottom: 15px; text-align: center; font-size: 14px; padding: 12px; background-color: #eff6ff; border-radius: 8px; border: 1px solid #bfdbfe;">
                🔄 AI 딥러닝 모델 엔진 깨우는 중... 잠시만 기다려주세요.
            </div>
            
            <div style="text-align: center;">
                <img id="selected-image" style="max-width: 100%; max-height: 380px; display: none; margin: 10px auto 20px auto; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
            </div>
            
            <div id="result-container" style="display: none; padding: 20px; border-radius: 12px; font-weight: 700; font-size: 16px; line-height: 1.6; margin-top: 15px;"></div>
            
            <div style="margin-top: 25px; padding-top: 18px; border-top: 1px solid #f1f5f9; font-size: 13px; color: #64748b;">
                <strong style="color: #334155;">📞 관제 시스템 후속 조치 프로세스</strong>
                <div style="margin-top: 10px; display: flex; flex-wrap: wrap; gap: 8px;">
                    <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-weight: 600; color: #334155; border: 1px solid #e2e8f0;">✅ 정상: 즉시 반납 승인</span>
                    <!-- 💡 요구사항 반영: '사고센터 자동접수' ➡️ '사고센터 접수'로 문구 변경 -->
                    <span style="background: #fef2f2; padding: 6px 12px; border-radius: 6px; font-weight: 600; color: #991b1b; border: 1px solid #fee2e2;">🚨 파손: 사고센터 접수</span>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>

        <script>
            let model, maxPredictions;
            const statusMsg = document.getElementById('status-message');
            const imageSelector = document.getElementById('image-selector');
            const resultDiv = document.getElementById('result-container');

            const modelJsonData = _MODEL_JSON_;
            const metadataJsonData = _METADATA_JSON_;
            const weightsHex = "_WEIGHTS_BIN_";

            async function initAI() {
                try {
                    const weightsBuffer = new Uint8Array(weightsHex.match(/.{1,2}/g).map(byte => parseInt(byte, 16))).buffer;

                    model = await tmImage.loadFromFiles(
                        new File([JSON.stringify(modelJsonData)], "model.json", {type: "application/json"}),
                        new File([weightsBuffer], "weights.bin", {type: "application/octet-stream"}),
                        new File([JSON.stringify(metadataJsonData)], "metadata.json", {type: "application/json"})
                    );
                    
                    maxPredictions = model.getTotalClasses();
                    statusMsg.innerHTML = "🚀 AI 모델 엔진 활성화 완료! 정석 분석 모드가 준비되었습니다.";
                    statusMsg.style.backgroundColor = "#f0fff4";
                    statusMsg.style.color = "#166534";
                    statusMsg.style.borderColor = "#bbf7d0";
                } catch (error) {
                    statusMsg.innerHTML = "❌ AI 모델 파일 로드 실패: " + error.message;
                    statusMsg.style.backgroundColor = "#fef2f2";
                    statusMsg.style.color = "#991b1b";
                    statusMsg.style.borderColor = "#fee2e2";
                }
            }
            
            initAI();

            imageSelector.addEventListener('change', function(event) {
                const file = event.target.files[0];
                if (!file) return;

                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.getElementById('selected-image');
                    img.src = e.target.result;
                    img.style.display = 'block';
                    
                    statusMsg.style.display = 'block';
                    statusMsg.innerHTML = "⚡ AI 모델이 픽셀 패턴을 분석하는 중입니다...";
                    statusMsg.style.backgroundColor = "#fffbeb";
                    statusMsg.style.color = "#92400e";
                    statusMsg.style.borderColor = "#fef3c7";
                    resultDiv.style.display = 'none';
                    
                    img.onload = async function() {
                        const prediction = await model.predict(img);
                        statusMsg.style.display = 'none';
                        
                        let highestClass = "";
                        let highestProbability = 0;
                        let allResultsHTML = "<hr style='border:0; border-top:1px solid #e2e8f0; margin:14px 0;'><strong>🔍 AI 모델 실시간 연산 가중치 데이터:</strong><br><div style='font-weight: 500; font-size:14px; margin-top:6px; color:#475569;'>";
                        
                        for (let i = 0; i < maxPredictions; i++) {
                            const prob = prediction[i].probability;
                            const className = prediction[i].className;
                            allResultsHTML += `• ${className} 일치율: <span style='font-weight:700; color:#0f172a;'>${(prob * 100).toFixed(1)}%</span><br>`;
                            if (prob > highestProbability) {
                                highestProbability = prob;
                                highestClass = className;
                            }
                        }
                        allResultsHTML += "</div>";

                        resultDiv.style.display = 'block';
                        const scorePercent = (highestProbability * 100).toFixed(1);

                        // 💡 파손 상태 감지 시 하이퍼링크 버튼 추가 연동 로직
                        if (highestClass.includes('파손') || highestClass.toLowerCase().includes('damage') || highestClass.toLowerCase().includes('scratch')) {
                            resultDiv.style.backgroundColor = '#fef2f2';
                            resultDiv.style.color = '#991b1b';
                            resultDiv.style.border = '1px solid #fecaca';
                            
                            // 결과창 텍스트 내에 세련된 현대차 서비스 네트워크 전용 '사고센터 접수' 연동 버튼 배치
                            resultDiv.innerHTML = `
                                <span style='font-size:17px;'>🚨 AI 분석 최종 결과: [${highestClass}] 상태 감지 (${scorePercent}%)</span>
                                <div style="margin-top: 15px; margin-bottom: 5px;">
                                    <a href="https://www.hyundai.com/kr/ko/service-membership/service-network/service-reservation-search" target="_blank" style="display: inline-block; padding: 10px 18px; font-size: 13px; font-weight: bold; color: #ffffff; background-color: #002c5f; text-decoration: none; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.15); transition: 0.2s;">
                                        🛠️ 현대자동차 사고센터 접수 및 서비스 예약하기 ➡️
                                    </a>
                                </div>
                            ` + allResultsHTML;
                        } else {
                            resultDiv.style.backgroundColor = '#f0fff4';
                            resultDiv.style.color = '#166534';
                            resultDiv.style.border = '1px solid #bbf7d0';
                            resultDiv.innerHTML = `<span style='font-size:17px;'>✅ AI 분석 최종 결과: [${highestClass}] 인증 완료 (${scorePercent}%)</span>` + allResultsHTML;
                        }
                    };
                };
                reader.readAsDataURL(file);
            });
        </script>
        """
        
        html_code = html_code.replace("_MODEL_JSON_", model_json)
        html_code = html_code.replace("_METADATA_JSON_", metadata_json)
        html_code = html_code.replace("_WEIGHTS_BIN_", weights_bin)
        
        components.html(html_code, height=780, scrolling=True)

    # 맨 하단 푸터
    st.markdown("---")
    st.caption("본 웹 서비스는 2026학년도 미래자동차학과 캡스톤 디자인 교과목 출품작이며, 기술 자문 및 공동 개발 파트너로 Gemini가 참여하였습니다. 무단 전재 및 배포를 금합니다.")
    st.markdown("---")
    st.caption("본 웹 서비스는 2026학년도 미래자동차학과 캡스톤 디자인 교과목 출품작이며, 기술 자문 및 공동 개발 파트너로 Gemini가 참여하였습니다. 무단 전재 및 배포를 금합니다.")
