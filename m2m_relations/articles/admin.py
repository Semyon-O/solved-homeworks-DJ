from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        input_datas = []
        for form in self.forms:
            input_datas.append(form.cleaned_data)

        tags_objs = list(filter(lambda d: 'is_main' in d and d['is_main'], input_datas))
        if len(tags_objs) >= 2:
            raise ValidationError('Главный тег может быть только один')

        if len(tags_objs) < 1:
            raise ValidationError('Выберете тег, который будет главным')

        name_tags = set(list(tag['tag'].name for tag in input_datas))
        if len(input_datas) != len(name_tags):
            raise ValidationError('У вас есть теги, которые повторяются. Уберите лишние')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
