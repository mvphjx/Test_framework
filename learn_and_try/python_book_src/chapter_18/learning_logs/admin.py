from django.contrib import admin

from learn_and_try.python_book_src.chapter_18.learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
