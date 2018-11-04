from rest_framework import serializers
from common.models import District, Agent
from common.models import HouseType
from common.models import Estate


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('distid', 'name', 'intro')


class HouseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseType
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estate
        fields = ('estateid', 'district', 'name')


# 使用django-rest-framework第一步编写序列化器
class AgentDetailSerializer(serializers.ModelSerializer):
    # 如果属性需要通过代码来获取就定义为SerializerMethodField
    # 获取estates属性的方法应该命名为get_estates
    estates = serializers.SerializerMethodField()


    @staticmethod
    def get_estates(agent):
        ret_value = []
        # 对于多对一外键关联(ForeignKey)可以用select_related提前加载关联属性
        # 通过这种方式可以使用内连接或左外连接直接获取关联属性避免1+N查询问题
        items = agent.estates.all().select_related('district')
        for item in items:
            ret_value.append({"estateid": item.estateid,
                              "name": item.name,
                              "district": DistrictSerializer(item.district).data})
        return ret_value

    class Meta:
        model = Agent
        fields = ('agentid', 'name', 'tel', 'certificated', 'estates')


# class AgentListSerializer(serializers.ModelSerializer):
#
#     estates = EstateSerializer()
#     district = DistrictSerializer()
#
#     class Meta:
#         model = Agent
#
#         fields = "__all__"
