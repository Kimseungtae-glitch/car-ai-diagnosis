import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="차량 외관 손상 자가 진단", layout="centered")

st.title("🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 서비스")
st.caption("Future Automotive Engineering - Capstone Project MVP")
st.write("서버에 내장된 딥러닝 모델 가중치를 기반으로 실시간 외관 손상을 판별합니다.")

# 서버에 파일 3개가 잘 올라갔는지 검증하는 로직
required_files = ["model.json", "metadata.json", "weights.bin"]
missing_files = [f for f in required_files if not os.path.exists(f)]

if missing_files:
    st.error(f"⚠️ 서버에 필수 AI 모델 부품 파일이 누락되었습니다: {', '.join(missing_files)}")
else:
    # 서버에 저장된 3개 파일을 자바스크립트가 자동으로 로드하도록 설계된 정석 HTML/JS
    html_code = """
    <div style="font-family: 'Malgun Gothic', sans-serif; padding: 20px; border: 2px solid #e2e8f0; border-radius: 12px; background-color: #ffffff;">
        <h4 style="margin-top:0; color: #1a202c; font-size: 18px; border-bottom: 2px solid #edf2f7; padding-bottom: 10px;">🤖 AI 외관 손상 실시간 진단창</h4>
        
        <div style="margin-bottom: 20px;">
            <span style="font-size: 14px; font-weight: bold; color: #4a5568;">📸 진단할 차량 사진을 업로드해 주세요</span>
            <input type="file" id="image-selector" accept="image/*" style="font-size: 14px; padding: 8px; background: #edf2f7; border-radius: 6px; width: 100%; border: 1px dashed #cbd5e0; margin-top: 5px; cursor: pointer;">
        </div>
        
        <div style="text-align: center;">
            <img id="selected-image" style="max-width: 100%; max-height: 350px; display: none; margin: 0 auto 20px auto; border-radius: 8px;">
        </div>
        
        <div id="status-message" style="color: #4a5568; font-weight: bold; margin-bottom: 15px; text-align: center; font-size: 14px; padding: 10px; background-color: #ebf8ff; border-radius: 6px;">
            🔄 AI 엔진 초기화 중... 잠시만 기다려주세요.
        </div>
        <div id="result-container" style="display: none; padding: 18px; border-radius: 8px; font-weight: bold; font-size: 16px; line-height: 1.6;"></div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>

    <script>
        let model, maxPredictions;
        const statusMsg = document.getElementById('status-message');
        const imageSelector = document.getElementById('image-selector');

        // 사용자가 파일을 올릴 필요 없이, 웹사이트가 켜지자마자 서버에 있는 파일 3개를 자동으로 로딩합니다.
        async function initAI() {
            try {
                // 상대 경로를 통해 서버의 app.py 옆에 있는 파일들을 직접 읽어옵니다.
                model = await tmImage.load('./model.json', './metadata.json');
                // weights.bin 파일은 구조상 자동 매칭되거나 불러와집니다.
                maxPredictions = model.getTotalClasses();
                statusMsg.innerHTML = "🚀 AI 엔진 구동 완료! 사진을 업로드하면 즉시 진단합니다.";
                statusMsg.style.backgroundColor = "#f0fff4";
                statusMsg.style.color = "#22543d";
            } catch (error) {
                statusMsg.innerHTML = "❌ AI 모델 파일 로딩 실패. 서버 경로를 확인하세요.";
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
                statusMsg.innerHTML = "⚡ AI 분석 진행 중...";
                document.getElementById('result-container').style.display = 'none';
                
                img.onload = async function() {
                    const prediction = await model.predict(img);
                    statusMsg.style.display = 'none';
                    
                    let highestClass = "";
                    let highestProbability = 0;
                    let allResultsHTML = "<hr style='border:0; border-top:1px solid #cbd5e0; margin:12px 0;'><strong>🔍 상세 분석 결과:</strong><br><div style='font-weight: normal; font-size:14px; margin-top:5px; color:#4a5568;'>";
                    
                    for (let i = 0; i < maxPredictions; i++) {
                        const prob = prediction[i].probability;
                        const className = prediction[i].className;
                        allResultsHTML += `• ${className}: <strong>${(prob * 100).toFixed(1)}%</strong><br>`;
                        if (prob > highestProbability) {
                            highestProbability = prob;
                            highestClass = className;
                        }
                    }
                    allResultsHTML += "</div>";

                    const resultDiv = document.getElementById('result-container');
                    resultDiv.style.display = 'block';
                    const scorePercent = (highestProbability * 100).toFixed(1);

                    if (highestClass.includes('파손') || highestClass.toLowerCase().includes('damage') || highestClass.toLowerCase().includes('scratch')) {
                        resultDiv.style.backgroundColor = '#fff5f5';
                        resultDiv.style.color = '#c53030';
                        resultDiv.style.border = '1px solid #fed7d7';
                        resultDiv.innerHTML = `🚨 AI 최종 판단: [${highestClass}] 상태 감지 (${scorePercent}%)` + allResultsHTML;
                    } else {
                        resultDiv.style.backgroundColor = '#f0fff4';
                        resultDiv.style.color = '#22543d';
                        resultDiv.style.border = '1px solid #c6f6d5';
                        resultDiv.innerHTML = `✅ AI 최종 판단: [${highestClass}] 상태 인증 (${scorePercent}%)` + allResultsHTML;
                    }
                };
            };
            reader.readAsDataURL(file);
        });
    </script>
    """
    components.html(html_code, height=650, scrolling=True)