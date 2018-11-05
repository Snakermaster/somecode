```
#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2018/9/30 12:02
# @Author  : 邵心
# @Software: PyCharm
```

from rest_framework import serializers
from .models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User



class SnippetSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id','title','code','linenos','language','style','owner']



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())


    class Meta:
        model = User
        fields = ('id','username','snippets')




