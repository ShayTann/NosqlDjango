from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Topic,Comment,SupportEvolution

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['author','date', 'body', 'score','subreddit','positivity','negativity','number_comments','clustering1','clustering2']
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['author','date', 'body', 'score','topic']

class SupportEvolutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = SupportEvolution
        fields = ['hour','positivity','negativity']