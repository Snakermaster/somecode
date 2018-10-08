```
#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2018/9/30 12:54
# @Author  : 邵心
# @Software: PyCharm
```

from rest_framework import permissions



class IsOwnerReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return obj.owner == request.user


