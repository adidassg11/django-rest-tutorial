from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    """
    # Fields and functions all replaced by ModelSerializer w/ Meta class!
    id = serializers.IntegerField(read_only=True)
    ...

    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...
    """
