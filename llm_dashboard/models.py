from django.db import models

# Create your models here.
class Evaluation_results(models.Model):
    eval_title = models.CharField(max_length=20)  # 평가를 진행한 모델 명
    eval_content = models.TextField()             # 평가를 진행한 모델의 기타 설명 
    eval_time = models.DateTimeField(auto_now_add=False) # 모델의 평가 시점 
    eval_author = models.TextField()              # 모델을 평가한 자


    def __str__(self):
        return f"{self.eval_title}[{self.eval_author}]"
    
    class Meta:
        verbose_name = "모델 평가 결과"
        verbose_name_plural = "모델 평가 결과 목록"
