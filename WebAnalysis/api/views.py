from django.contrib.auth.models import User, Group
from django.db.models import Count
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TopicSerializer,CommentSerializer
from .models import Topic,Comment,SupportEvolution
import pymongo
from django.db.models import Sum
from textblob import TextBlob #Sentiment analysis
from sklearn.feature_extraction.text import TfidfVectorizer  #Pour clustering Kmeans
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all() 
    qry2 = SupportEvolution.objects.all()
    comment_content = []
    for doc in qry2 : #Je reset total positivity et negativity chaque fois pour refaire le calcule par la suite
        doc.positivity = 0 
        doc.negativity = 0 
        doc.save()
    #Sentiment analysis
    for element in queryset :
        positivity = 0
        negativity = 0
        
        counting = 0
        comments = Comment.objects.filter(topic=element.body) # là je filtre les commentaires de ce topic afin de les analyser avec txt blob et avoir le taux de positivity et negativity 
        
        for comment in comments:
            comment_content.append(comment.body)
            tmp_blob = TextBlob(comment.body)
            if tmp_blob.sentiment.polarity > 0 :
                positivity += 1
            else : 
                negativity += 1
            counting += 1
        element.positivity= positivity
        element.number_comments = counting
        element.negativity = negativity
        
        #Add positivty and negativity to model of evolution in 24h
        if SupportEvolution.objects.filter(hour=element.date.hour).exists():

            tmp = SupportEvolution.objects.get(hour=str(element.date.hour))
            tmp.positivity += element.positivity 
            tmp.negativity += element.negativity
            tmp.save()
        
        #Kmeans text clustering
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(comment_content)
        model = KMeans(n_clusters=2, init='k-means++', max_iter=100, n_init=1)
        model.fit(X)
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        if (str(element.clustering1) == ""): #Pour éviter la répitition
            for ind in order_centroids[0, :10]:
                element.clustering1 += ","+str(terms[ind])
            for ind in order_centroids[1, :10]:
                    element.clustering2 += ","+str(terms[ind])
        element.save()
    print("Updated ! c'est bon pour le sentiment analysing et clustering 'Kmeans'")
    serializer_class = TopicSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer