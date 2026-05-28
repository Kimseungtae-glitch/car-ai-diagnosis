import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="차량 외관 손상 자가 진단", layout="centered")

st.title("🚗 AI 이미지 인식 기반 자율주행 차량 외관 손상 자가 진단 서비스")
st.caption("Future Automotive Engineering - Capstone Project MVP")
st.write("서버에 내장된 딥러닝 가중치를 활용하여 실시간으로 외관 상태를 정석 분석합니다.")

# 서버 내 파일 존재 여부 확인
required_files = ["model.json", "metadata.json", "weights.bin"]
missing_files = [f for f in required_files if not os.path.exists(f)]

if missing_files:
    st.error(f"⚠️ 서버에 필수 AI 파일이 누락되었습니다: {', '.join(missing_files)}")
else:
    # 파일들을 텍스트와 바이너리 형태로 브라우저에 직접 주입하여 보안(CORS) 벽을 허무는 정석 코드
    with open("model.json", "r", encoding="utf-8") as f:
        model_json = f.read()
    with open("metadata.json", "r", encoding="utf-8") as f:
        metadata_json = f.read()
    with open("weights.bin", "rb") as f:
        weights_bin = f.read().hex()  # 바이너리 파일을 안전하게 넘기기 위해 hex로 변환

    html_code = f"""
    <div style="font-family: 'Malgun Gothic', sans-serif; padding: 20px; border: 2px solid #e2e8f0; border-radius: 12px; background-color: #ffffff;">
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
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>

    <script>
        let model, maxPredictions;
        const statusMsg = document.getElementById('status-message');
        const imageSelector = document.getElementById('image-selector');
        const resultDiv = document.getElementById('result-container');

        // 서버가 가져온 파일 데이터를 메모리에 직접 태워 보안 에러를 원천 차단합니다.
        async function initAI() {{
            try {{
                const modelJsonData = {model_json};
                const metadataJsonData = {metadata_json};
                
                // hex 데이터를 다시 바이너리(ArrayBuffer)로 복원
                const weightsHex = "{weights_bin}";
                const weightsBuffer = new Uint8Array(weightsHex.match(/.{{1,2}}/g).map(byte => parseInt(byte, 16))).buffer;

                // 구글 서버 통신 없이 브라우저 메모리 내부에서 직접 뇌를 구성
                model = await tmImage.loadFromFiles(
                    new File([JSON.stringify(modelJsonData)], "model.json", {{type: "application/json"}}),
                    new File([weightsBuffer], "weights.bin", {{type: "application/octet-stream"}}),
                    new File([JSON.stringify(metadataJsonData)], "metadata.json", {{type: "application/json"}})
                );
                
                maxPredictions = model.getTotalClasses();
                statusMsg.innerHTML = "🚀 AI 정석 모델 로딩 완료! 진짜 딥러닝 연산이 가능합니다.";
                statusMsg.style.backgroundColor = "#f0fff4";
                statusMsg.style.color = "#22543d";
            } catch (error) {{
                statusMsg.innerHTML = "❌ AI 모델 파일 로드 실패: " + error.message;
                statusMsg.style.backgroundColor = "#fff5f5";
                statusMsg.style.color = "#c53030";
            }}
        }}
        
        initAI();

        imageSelector.addEventListener('change', function(event) {{
            const file = event.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {{
                const img = document.getElementById('selected-image');
                img.src = e.target.result;
                img.style.display = 'block';
                
                statusMsg.style.display = 'block';
                statusMsg.innerHTML = "⚡ 진짜 AI 모델이 픽셀 패턴을 분석하는 중입니다...";
                statusMsg.style.backgroundColor = "#feebc8";
                statusMsg.style.color = "#dd6b20";
                resultDiv.style.display = 'none';
                
                img.onload = async function() {{
                    // 진짜 티처블머신 뇌가 사진을 보고 분석하는 함수
                    const prediction = await model.predict(img);
                    statusMsg.style.display = 'none';
                    
                    let highestClass = "";
                    let highestProbability = 0;
                    let allResultsHTML = "<hr style='border:0; border-top:1px solid #cbd5e0; margin:12px 0;'><strong>🔍 AI 모델 내부 연산 데이터 (실시간):</strong><br><div style='font-weight: normal; font-size:14px; margin-top:5px; color:#4a5568;'>";
                    
                    for (let i = 0; i < maxPredictions; i++) {{
                        const prob = prediction[i].probability;
                        const className = prediction[i].className;
                        allResultsHTML += `• ${className} 가중치 확률: <strong>${(prob * 100).toFixed(1)}%</strong><br>`;
                        if (prob > highestProbability) {{
                            highestProbability = prob;
                            highestClass = className;
                        }}
                    }}
                    allResultsHTML += "</div>";

                    resultDiv.style.display = 'block';
                    const scorePercent = (highestProbability * 100).toFixed(1);

                    // 클래스 이름에 따라 색상 분기
                    if (highestClass.includes('파손') || highestClass.toLowerCase().includes('damage') || highestClass.toLowerCase().includes('scratch')) {{
                        resultDiv.style.backgroundColor = '#fff5f5';
                        resultDiv.style.color = '#c53030';
                        resultDiv.style.border = '1px solid #fed7d7';
                        resultDiv.innerHTML = `🚨 AI 실시간 분석: [${highestClass}] 상태 감지 (${scorePercent}%)` + allResultsHTML;
                    } else {{
                        resultDiv.style.backgroundColor = '#f0fff4';
                        resultDiv.style.color = '#22543d';
                        resultDiv.style.border = '1px solid #c6f6d5';
                        resultDiv.innerHTML = `✅ AI 실시간 분석: [${highestClass}] 상태 인증 (${scorePercent}%)` + allResultsHTML;
                    }}
                }};
            }};
            reader.readAsDataURL(file);
        }});
    </script>
    """
    components.html(html_code, height=650, scrolling=True)