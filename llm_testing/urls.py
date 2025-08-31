from django.urls import path
from .views import test_ollama_chat

urlpatterns = [
    path("test-ollama/", test_ollama_chat, name="test_ollama_chat")
]
