from django.contrib import admin
from documents.models import Title, SubTitle, Content, Keyword

# Register your models here.
admin.site.register(Title)
admin.site.register(SubTitle)
admin.site.register(Content)
admin.site.register(Keyword)

