from django.conf.urls import patterns, include, url
from django.contrib import admin
from kaushue.models import Question, Connection
from rest_framework import routers, serializers, viewsets


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title')


# Serializers define the API representation.
class QuestionSerializer(serializers.ModelSerializer):
    reference = ReferenceSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Question
        fields = ('id', 'title', 'content', 'reference')


class ConnectionSerializer(serializers.Serializer):
    class NaiveSerializer(serializers.ModelSerializer):

        class Meta:
            model = Question
            fields = ('id', )

    from_question = NaiveSerializer()
    to_question = NaiveSerializer()
    logic = serializers.ReadOnlyField()

    class Meta:
        model = Connection
        fields = ('from_question', 'to_question', 'logic')


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'connections', ConnectionViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include('kaushue.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
