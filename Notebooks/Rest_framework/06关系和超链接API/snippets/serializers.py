```
#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2018/10/2 15:02
# @Author  : 邵心
# @Software: PyCharm
```

from rest_framework import serializers
from .models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User



class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')


    class Meta:
        model = Snippet
        fields = ['url','id','highlight','title',
                  'code','linenos','language','style','owner']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail',read_only=True)


    class Meta:
        model = User
        fields = ('url','id','username','snippets')




