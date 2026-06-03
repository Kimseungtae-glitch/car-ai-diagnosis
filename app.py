import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 설정 및 다크모드 방지용 스타일 주입
st.set_page_config(page_title="차량 외관 손상 자가 진단", layout="centered")

# 글로벌 CSS 주입 (스트림릿 기본 폰트 및 배경 깔끔하게 정리)
st.markdown("""
    <style>
    .main .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1 { color: #1e293b; font-weight: 800; letter-spacing: -0.05em; }
    </style>
""", unsafe_allow_html=True)

# 상단 타이틀 구역 디자인
st.title("🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단")
st.caption("🏆 2026 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP")
st.markdown("<p style='color: #475569; font-size: 15px; margin-bottom: 25px;'>본 서비스는 카셰어링 이용자를 위한 무인 반납 및 외관 손상 실시간 정석 진단 플랫폼입니다.</p>", unsafe_allow_html=True)

# 1. 가이드라인 박스 디자인 고도화
st.info("""
**📸 AI 진단 정확도를 높이는 촬영 가이드**
* 차량의 정면/측면이 **수평**이 되도록 촬영해 주세요.
* 야간이나 어두운 지하 주차장보다는 **밝은 조명 아래**가 가장 정확합니다.
* 파손 부위가 잘 보이도록 **1m 내외의 적정 거리**에서 촬영해 주세요.
""")

# 서버 내 파일 존재 여부 확인
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

    # 인공지능 진단창 내부 HTML/CSS 전면 리디자인
    html_code = """
    <div style="font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; padding: 25px; border: 1px solid #e2e8f0; border-radius: 16px; background-color: #ffffff; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05); margin-top: 15px;">
        
        <!-- 진단창 헤더 -->
        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px; margin-bottom: 20px;">
            <h4 style="margin: 0; color: #0f172a; font-size: 19px; font-weight: 700;">🤖 AI 외관 손상 진단창</h4>
            <span style="font-size: 11px; background: #e2e8f0; color: #475569; padding: 3px 8px; border-radius: 20px; font-weight: 600;">v1.0 정석 구동</span>
        </div>
        
        <!-- 파일 업로드 구역 -->
        <div style="margin-bottom: 20px; background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #edf2f7;">
            <p style="font-size: 13px; color: #334155; margin-top: 0; margin-bottom: 10px; font-weight: 600;">
                📸 분석할 차량의 외관 사진을 첨부해 주세요.
            </p>
            <input type="file" id="image-selector" accept="image/*" style="font-size: 13px; padding: 10px; background: #ffffff; border-radius: 8px; width: 100%; border: 1px dashed #cbd5e1; box-sizing: border-box; cursor: pointer;">
        </div>
        
        <!-- 실시간 상태 및 이미지 표시 구역 -->
        <div id="status-message" style="color: #1e3a8a; font-weight: 700; margin-bottom: 15px; text-align: center; font-size: 14px; padding: 12px; background-color: #eff6ff; border-radius: 8px; border: 1px solid #bfdbfe; transition: all 0.3s ease;">
            🔄 AI 딥러닝 모델 엔진 깨우는 중... 잠시만 기다려주세요.
        </div>
        
        <div style="text-align: center;">
            <img id="selected-image" style="max-width: 100%; max-height: 380px; display: none; margin: 10px auto 20px auto; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
        </div>
        
        <!-- 결과창 구역 -->
        <div id="result-container" style="display: none; padding: 20px; border-radius: 12px; font-weight: 700; font-size: 16px; line-height: 1.6; margin-top: 15px; box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);"></div>
        
        <!-- 하단 비즈니스 프로세스 가이드 -->
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

# 맨 하단 공식 프로젝트 푸터(Footer)
st.markdown("---")
st.caption("본 웹 서비스는 2026학년도 미래자동차학과 캡스톤 디자인 교과목 출품작이며, 기술 자문 및 공동 개발 파트너로 Gemini가 참여하였습니다. 무단 전재 및 배포를 금합니다.")
