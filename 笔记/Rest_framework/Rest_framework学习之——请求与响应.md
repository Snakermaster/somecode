*** 
在上一章节序列化中，rest_framework为我们提供了一种新的数据获取方式
在这一节中，我们将接触到REST框架的核心
***
```
请求对象：
    REST框架引入了Request，Request的核心功能是request.data属性，类似于request.POST,但对于web API 更为游泳

响应对象：
    REST框架还引入了一个Response对象，该对象TemplateResponse采用未呈现的内容并使用内容协商来确定返回给客户端的正确内容类型。

状态代码：
    在视图中使用数字HTTP状态代码并不总能显示读数，如果错误代码错误，很容易注意到。REST框架为每个状态代码提供更明确的标识符，例如HTTP_400_BAD_REQUEST在status模块中
包装API视图:

REST框架提供了两个可用于编写API视图的包装器。

@api_view用于处理基于函数的视图的装饰器。
该APIView班与基于类的视图工作。
这些包装器提供了一些功能，例如确保Request在视图中接收实例，以及向Response对象添加上下文以便可以执行内容协商。

包装器还提供行为，例如405 Method Not Allowed在适当时返回响应，以及处理使用格式错误的输入进行ParseError访问时发生的任何异常request.data。

```
在视图前添加：
    
    api_view([请求方式])
    
将data = JSONParser().parser(request)删除，

serializer = 模型名Serialiser(data=data)
改为

serializer = 模型名Serializer(data=request.data)

所有JsonResponse()转换为Response()

### 在url中添加可选格式后缀
即在视图参数中加入format=None即可

### 在urls.py中添加一组urlpatterns

    from rest_framework.urlpatterns import form_suffix_patterns
    '''
    urlpatterns = format_suffix_pattern(urlpatterns)

