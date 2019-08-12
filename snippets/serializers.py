from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']

    """
    # Fields and functions all replaced by ModelSerializer w/ Meta class!
    id = serializers.IntegerField(read_only=True)
    ...

    def create(self, validated_data):
        # json parsing
        ...

    def update(self, instance, validated_data):
        ...
    """

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
