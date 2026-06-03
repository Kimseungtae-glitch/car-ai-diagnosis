import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="차량 외관 손상 자가 진단", layout="centered")

# 상단 헤더 디자인 고도화
st.title("🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 서비스")
st.caption("🏆 2026 미래자동차학과 캡스톤 디자인 우수 프로젝트 MVP")
st.write("본 서비스는 카셰어링 이용자를 위한 무인 반납 및 외관 손상 실시간 정석 진단 플랫폼입니다.")

# 1. 이용자를 위한 AI 촬영 가이드라인 추가 (시각적 완성도 업)
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

    html_code = """
    <div style="font-family: 'Malgun Gothic', sans-serif; padding: 20px; border: 2px solid #e2e8f0; border-radius: 12px; background-color: #ffffff; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
        <h4 style="margin-top:0; color: #1a202c; font-size: 18px; border-bottom: 2px solid #edf2f7; padding-bottom: 10px;">🤖 AI 외관 손상 진단창 (정석 구동)</h4>
        
        <div style="margin-bottom: 20px;">
            <p style="font-size: 14px; color: #4a5568; margin-bottom: 10px;">📸 <strong>진단할 차량 사진을 업로드해 주세요.</strong></p>
            <input type="file" id="image-selector" accept="image/*" style="font-size: 14px; padding: 8px; background: #edf2f7; border-radius: 6px; width: 100%; border: 1px dashed #cbd5e0; cursor: pointer;">
        </div>
        
        <div style="text-align: center;">
            <img id="selected-image" style="max-width: 100%; max-height: 350px; display: none; margin: 0 auto 20px auto; border-radius: 8px;">
        </div>
        
        <div id="status-message" style="color: #4a5568; font-weight: bold; margin-bottom: 15px; text-align: center; font-size: 14px; padding: 10px; background-color: #ebf8ff; border-radius: 6px;">
            🔄 AI 딥러닝 모델 엔진 깨우는 중... 잠시만 기다려주세요.
        </div>
        <div id="result-container" style="display: none; padding: 18px; border-radius: 8px; font-weight: bold; font-size: 16px; line-height: 1.6;"></div>
        
        <div style="margin-top: 25px; padding-top: 15px; border-top: 1px solid #edf2f7; font-size: 13px; color: #718096;">
            <strong>📞 진단 후 후속 조치 프로세스 안내</strong>
            <div style="margin-top: 8px; display: flex; gap: 10px;">
                <span style="background: #edf2f7; padding: 6px 12px; border-radius: 4px; font-weight: bold; color: #4a5568;">정상 판정 시 ➡️ 즉시 반납 완료</span>
                <span style="background: #fff5f5; padding: 6px 12px; border-radius: 4px; font-weight: bold; color: #c53030;">파손 판정 시 ➡️ 사고 접수 센터 (1588-XXXX)</span>
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
                statusMsg.style.color = "#22543d";
            } catch (error) {
                statusMsg.innerHTML = "❌ AI 모델 파일 로드 실패: " + error.message;
                statusMsg.style.backgroundColor = "#fff5f5";
                statusMsg.style.color = "#c53030";
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
                statusMsg.style.backgroundColor = "#feebc8";
                statusMsg.style.color = "#dd6b20";
                resultDiv.style.display = 'none';
                
                img.onload = async function() {
                    const prediction = await model.predict(img);
                    statusMsg.style.display = 'none';
                    
                    let highestClass = "";
                    let highestProbability = 0;
                    let allResultsHTML = "<hr style='border:0; border-top:1px solid #cbd5e0; margin:12px 0;'><strong>🔍 AI 모델 내부 연산 데이터 (실시간):</strong><br><div style='font-weight: normal; font-size:14px; margin-top:5px; color:#4a5568;'>";
                    
                    for (let i = 0; i < maxPredictions; i++) {
                        const prob = prediction[i].probability;
                        const className = prediction[i].className;
                        allResultsHTML += `• ${className} 가중치 확률: <strong>${(prob * 100).toFixed(1)}%</strong><br>`;
                        if (prob > highestProbability) {
                            highestProbability = prob;
                            highestClass = className;
                        }
                    }
                    allResultsHTML += "</div>";

                    resultDiv.style.block = 'block';
                    resultDiv.style.display = 'block';
                    const scorePercent = (highestProbability * 100).toFixed(1);

                    if (highestClass.includes('파손') || highestClass.toLowerCase().includes('damage') || highestClass.toLowerCase().includes('scratch')) {
                        resultDiv.style.backgroundColor = '#fff5f5';
                        resultDiv.style.color = '#c53030';
                        resultDiv.style.border = '1px solid #fed7d7';
                        resultDiv.innerHTML = `🚨 AI 실시간 분석: [${highestClass}] 상태 감지 (${scorePercent}%)` + allResultsHTML;
                    } else {
                        resultDiv.style.backgroundColor = '#f0fff4';
                        resultDiv.style.color = '#22543d';
                        resultDiv.style.border = '1px solid #c6f6d5';
                        resultDiv.innerHTML = `✅ AI 실시간 분석: [${highestClass}] 상태 인증 (${scorePercent}%)` + allResultsHTML;
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
    
    components.html(html_code, height=720, scrolling=True)

# 3. 맨 하단 공식 프로젝트 푸터(Footer) 추가
st.markdown("---")
st.caption("본 웹 서비스는 2026학년도 미래자동차학과 캡스톤 디자인 교과목 출품작이며, 기술 자문 및 공동 개발 파트너로 Gemini가 참여하였습니다. 무단 전재 및 배포를 금합니다.")
