### 本章主要通过使用超链接建立关系来提高API的内聚性和可发现性

### first

    在views.py中，使用基于函数的常规视图和@api_view创建端点
    @api_view
    def api_root(request,format=None):
        return response({
        'users':reverse(r'user-list',request=request,format=format),
        'snippets':reverse(r'snippet-list',request=request,format=format)
        })
    
### second
我们还需要使用基于类的视图为突出的代码段添加视图

    class SnippetHighlight(generice.GenercAPIView):
        queryset = Snippet.object.all()
        renderer_classes = (renderer.StaticHTMLRenderer,)
        
        def get(self,request,*args,**kwargs):
            snippet = self.get_object()
            return Response(snippet.highlight)

在url中添加新视图

    url(r"^$",views.api_root),
注意突出显示添加网址的格式

    url(r"snippet/(?P<pk>[0-9]+)/highlight/$",views.SnippetHighlight.as_view())
    
### third
处理实体之间的关系是webapi设计中的一个难点,一般使用以下几种方式来处理实体之间的关系：

    * 使用主键
    * 在实体之间使用超链接。
    * 在相关实体上使用唯一的识别段塞字段
    * 使用相关实体的默认字符串表示形式
    * 将相关实体嵌套在父表示中
    * 一些其他自定义表示
    
在这里，我们使用超链接样式来处理关系
超链接样式HyperlinkedModelSerializer 和ModelSerializer 有以下不同：
    
        id默认情况下不包括该字段。
        它包括一个url字段，使用HyperlinkedIdentityField。
        关系使用HyperlinkedRelatedField，而不是PrimaryKeyRelatedField。
现在我们需要重写现有的序列化程序一使用超链接

    
    class SnippetSerializer(serializer.HyperlinkedModelSerializer):
        owner = serializer.ReadOnlyField(source='owner.username')
        hightlight = serializer.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')
        
        class Meta:
            model = Snippet
            fields = ['url','id','highlight','owner','title',
            'code','linenos','language','style']
            
    class UserSerializer(serializer.HyperlinkedSerializer):
        snippets = serializer.HyperlinkedRelatedField(many=True,view_naem='snippet-detail',read_only=True)
        class Meta:
            model = User
            fields = ['url','id','username','snippets']
            
 ### fourth
 最后，确保url模式已命名，如上面添加的"user-detail"和"snippet-detail"等
 
 如果还想设置分页，可在settings目录下添加
 REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

















