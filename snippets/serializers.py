from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

    owner = serializers.ReadOnlyField(source='owner.username')

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

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
