import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 설정
st.set_page_config(page_title="차량 외관 손상 자가 진단", layout="centered")

# 글로벌 CSS (스트림릿 기본 배경과 여백 정리)
st.markdown("""
    <style>
    .main .block-container { padding-top: 1rem; padding-bottom: 2rem; }
    h1 { color: #1e293b; font-weight: 800; letter-spacing: -0.05em; }
    </style>
""", unsafe_allow_html=True)

# 1. 전등 대신 '미래형 자동차 헤드라이트' 애니메이션 인터페이스
car_lamp_html = """
<div style="font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; background-color: #0f1115; padding: 35px 25px; border-radius: 16px; margin-bottom: 25px; box-shadow: inset 0 0 20px rgba(0,0,0,0.6);">
    <div style="display: flex; align-items: center; gap: 35px; position: relative; max-width: 550px; width: 100%; flex-wrap: wrap; justify-content: center;">
        
        <div id="carGroup" onclick="toggleCarLight()" style="position: relative; width: 160px; height: 90px; cursor: pointer; z-index: 10; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            
            <div id="leftGlow" style="position: absolute; top: 15px; left: -140px; width: 180px; height: 100px; background:決 radial-gradient(ellipse at right, rgba(251,191,36,0.3) 0%, rgba(251,191,36,0) 80%); transform: perspective(200px) rotateY(-30deg); opacity: 0; pointer-events: none; transition: 0.4s; filter: blur(5px);"></div>
            <div id="rightGlow" style="position: absolute; top: 15px; right: -140px; width: 180px; height: 100px; background: radial-gradient(ellipse at left, rgba(251,191,36,0.3) 0%, rgba(251,191,36,0) 80%); transform: perspective(200px) rotateY(30deg); opacity: 0; pointer-events: none; transition: 0.4s; filter: blur(5px);"></div>
            
            <div style="position: relative; width: 140px; height: 50px; background: linear-gradient(180deg, #334155 0%, #1e293b 100%); border-radius: 20px 20px 12px 12px; border: 1px solid #475569;">
                
                <div style="width: 100px; height: 16px; background: #0f172a; margin: 6px auto 0 auto; border-radius: 8px 8px 3px 3px; opacity: 0.8; border-bottom: 1px solid #334155;"></div>
                
                <div id="lightL" style="position: absolute; bottom: 10px; left: 10px; width: 22px; height: 8px; background: #64748b; border-radius: 2px 6px 3px 3px; transition: 0.3s;"></div>
                
                <div id="lightR" style="position: absolute; bottom: 10px; right: 10px; width: 22px; height: 8px; background: #64748b; border-radius: 6px 2px 3px 3px; transition: 0.3s;"></div>
                
                <div style="width: 50px; height: 4px; background: #1e293b; margin: 8px auto 0 auto; border-radius: 2px; border: 1px solid #334155;"></div>
            </div>
            
            <div style="display: flex; justify-content: space-between; width: 110px; margin-top: -2px;">
                <div style="width: 20px; height: 8px; background: #0f172a; border-radius: 2px;"></div>
                <div style="width: 20px; height: 8px; background: #0f172a; border-radius: 2px;"></div>
            </div>
            
            <span style="color: #64748b; font-size: 10px; margin-top: 8px; font-weight: 600; letter-spacing: -0.03em;">👆 차량 전면 클릭</span>
        </div>
        
        <div id="loginForm" style="background: rgba(255,255,255,0.02); backdrop-filter: blur(15px); padding: 18px 22px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.06); width: 260px; color: white; opacity: 0.2; transition: all 0.5s; box-sizing: border-box;">
            <h3 style="text-align: center; margin-top: 0; margin-bottom: 12px; font-weight: 600; font-size: 15px; color: #64748b;" id="welcomeText">🔒 자율주행 V2X 인증</h3>
            <div style="margin-bottom: 10px;">
                <label style="display: block; font-size: 11px; color: #64748b; margin-bottom: 4px;">Connected Car ID</label>
                <input type="text" placeholder="Future_Auto_SeungTae" disabled style="width: 100%; padding: 8px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; color: #64748b; font-size: 12px; box-sizing: border-box; outline: none;">
            </div>
            <button style="width: 100%; padding: 10px; border: none; border-radius: 6px; background: linear-gradient(135deg, #475569 0%, #334155 100%); color: #94a3b8; font-weight: bold; font-size: 12px; transition: 0.3s;" id="loginBtn">시동을 켜서 검수를 시작하세요</button>
        </div>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script>
    let isCarOn = false;
    function toggleCarLight() {
        isCarOn = !isCarOn;
        
        // 클릭 시 차량이 통통 튀는 스마트키 연동 애니메이션 효과
        gsap.to("#carGroup", {y: -4, duration: 0.1, yoyo: true, repeat: 1});
        
        const glowL = document.getElementById("leftGlow");
        const glowR = document.getElementById("rightGlow");
        const lightL = document.getElementById("lightL");
        const lightR = document.getElementById("lightR");
        const form = document.getElementById("loginForm");
        const welcome = document.getElementById("welcomeText");
        const btn = document.getElementById("loginBtn");
        
        if (isCarOn) {
            // 헤드라이트 On 효과
            glowL.style.opacity = "1";
            glowR.style.opacity = "1";
            lightL.style.background = "#fbbf24";
            lightL.style.boxShadow = "0 0 20px 5px rgba(251,191,36,0.8)";
            lightR.style.background = "#fbbf24";
            lightR.style.boxShadow = "0 0 20px 5px rgba(251,191,36,0.8)";
            
            // 로그인 카드 활성화 효과
            form.style.opacity = "1";
            form.style.background = "rgba(255,255,255,0.06)";
            form.style.border = "1px solid rgba(251,191,36,0.4)";
            form.style.boxShadow = "0 10px 25px rgba(251,191,36,0.1)";
            welcome.innerHTML = "✅ V2X 커넥티드 카 연동 완료";
            welcome.style.color = "#fbbf24";
            btn.innerHTML = "차량 외관 무인 자가 진단 시작";
            btn.style.background = "linear-gradient(135deg, #fbbf24 0%, #d97706 100%)";
            btn.style.color = "#000000";
        } else {
            // 헤드라이트 Off 효과
            glowL.style.opacity = "0";
            glowR.style.opacity = "0";
            lightL.style.background = "#64748b";
            lightL.style.boxShadow = "none";
            lightR.style.background = "#64748b";
            lightR.style.boxShadow = "none";
            
            // 로그인 카드 비활성화 효과
            form.style.opacity = "0.2";
            form.style.background = "rgba(255,255,255,0.02)";
            form.style.border = "1px solid rgba(255,255,255,0.06)";
            form.style.boxShadow = "none";
            welcome.innerHTML = "🔒 자율주행 V2X 인증";
            welcome.style.color = "#64748b";
            btn.innerHTML = "시동을 켜서 검수를 시작하세요";
            btn.style.background = "linear-gradient(135deg, #475569 0%, #334155 100%)";
            btn.style.color = "#94a3b8";
        }
    }
</script>
"""

# 자동차 램프 컴포넌트 출력
components.html(car_lamp_html, height=200)

# 타이틀 및 메인 기능 안내 구역
st.title("🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단")
st.caption("🏆 2026 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP")

# 2. 촬영 가이드라인 안내 상자
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
            <span style="font-size: 11px; background: #e2e8f0; color: #475569; padding: 3px 8px; border-radius: 20px; font-weight: 600;">v1.0 정석 구동</span>
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
                <span style="background: #fef2f2; padding: 6px 12px; border-radius: 6px; font-weight: 600; color: #991b1b; border: 1px solid #fee2e2;">🚨 파손: 사고 센터 자동 접수</span>
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
                statusMsg.innerHTML = "🚀 AI 정석 모델 로딩 완료! 진짜 딥러닝 연산이 가능합니다.";
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
                statusMsg.innerHTML = "⚡ 진짜 AI 모델이 픽셀 패턴을 분석하는 중입니다...";
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

                    if (highestClass.includes('파손') || highestClass.toLowerCase().includes('damage') || highestClass.toLowerCase().includes('scratch')) {
                        resultDiv.style.backgroundColor = '#fef2f2';
                        resultDiv.style.color = '#991b1b';
                        resultDiv.style.border = '1px solid #fecaca';
                        resultDiv.innerHTML = `<span style='font-size:17px;'>🚨 AI 분석 최종 결과: [${highestClass}] 상태 감지 (${scorePercent}%)</span>` + allResultsHTML;
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
    
    components.html(html_code, height=750, scrolling=True)

# 맨 하단 푸터
st.markdown("---")
st.caption("본 웹 서비스는 2026학년도 미래자동차학과 캡스톤 디자인 교과목 출품작이며, 기술 자문 및 공동 개발 파트너로 Gemini가 참여하였습니다. 무단 전재 및 배포를 금합니다.")
