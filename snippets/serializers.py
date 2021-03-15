from snippets.models import Snippet
from rest_framework import serializers
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    last_login = serializers.ReadOnlyField(source='owner.last_login')
    highlighted = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ["url","id", "title", "code", "linenos", "language", "style","owner","last_login", "highlighted"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets']