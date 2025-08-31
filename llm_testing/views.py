from django.shortcuts import render
from django.http import JsonResponse
import requests

def test_ollama_chat(request):

    response_text = None 

    if request.method == "POST":
        user_input = request.POST.get("user_input","") # user_input 필드의 값을 가지고 옴

        response = requests.post(
            "http://localhost:11434/api/chat",
            headers = {"Content-Type":'application/json'},
            json={
                "model":'gpt-oss:20b',
                "messages":[
                    {"role": "system", 
                     "content": "주어진 질문에 대해 한글로 간단하고 명확한 답변을 제공해주세요."},
                    {"role": "user", "content": user_input}
                    ],
                    "options":{
                        'temperature':1.0,
                        'num_predict':100
                    },
                    "stream":False
            }
        )

        if response.status_code == 200:
            response_data = response.json()
            response_text = response_data.get("message", {}).get("content","[응답없음]")
        else: 
            response_text = f"[오류] 상태 코드: {response.status_code}"
    
    return render(request=request, 
                  template_name='llm_testing/testing.html',
                  context=
                  {'response':response_text}
                  )