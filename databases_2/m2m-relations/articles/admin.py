from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Tag_list


class TagListInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dataList = form.cleaned_data
            print(dataList)
            if dataList['mainTag'] == True:
                i += 1
        if i > 1:
            raise ValidationError('Основной раздел должен быть только один')
        return super().clean()


class TagListInLine(admin.TabularInline):
    model = Tag_list
    formset = TagListInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagListInLine]
