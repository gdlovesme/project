from django.contrib import admin

# здесь регистрируются модели для их отображения в админ панели
from post.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)