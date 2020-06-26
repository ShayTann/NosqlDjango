import graphene
from graphene_django.types import DjangoObjectType
from .models import Topic,Comment,SupportEvolution
from django.db.models import Sum
class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
class SupportEvolutionType(DjangoObjectType):
    class Meta:
        model = SupportEvolution

class Query(graphene.ObjectType):
    all_topics = graphene.List(TopicType)
    all_comments = graphene.List(CommentType)
    all_supportevolutions = graphene.List(SupportEvolutionType)

    def resolve_all_comments(self,info,**kwargs):
        return Comment.objects.all()

    def resolve_all_topics(self, info,**kwargs):
        return Topic.objects.all()

    def resolve_all_supportevolutions(self, info,**kwargs):
        return SupportEvolution.objects.all()

schema = graphene.Schema(query=Query)
