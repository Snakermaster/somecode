```
使用mixins类可以更好的通过创建、检索、更新、删除来组合视图

```
配置：

    我们需要导入两个包
    from rest_framework import mixins
    # 下面这个用于构建APIView
    from rest_framework import generics
    紧接着在类下面声明
    queryset = 模型名.objects.all()
    serializer_calss = 模型名Serializer


generics.GenericAPIView ---> 构建APIView 
ListModelMixin  ---> 遍历
CreateModelMixin ---> 创建
RetrieveModelMixin ---> 检索
UpdateModelMixin ---> 更新
DestroyModelMixin ---> 删除
