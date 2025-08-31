from django.contrib import admin
from .models import Evaluation_results

@admin.register(Evaluation_results)
class Evaluation_results_admin(admin.ModelAdmin):
    list_display  = ('id', 'eval_title', 'eval_author', 'eval_time') # 어드민 페이지에 보일 컬럼
    search_fields = ('eval_title', 'eval_author', 'eval_time')  # 검색창 내 필터
    list_filter = ("eval_time",'eval_author') # 우측 리스트 필터
    ordering = ("-eval_time",)

    