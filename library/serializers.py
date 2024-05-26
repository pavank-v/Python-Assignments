from rest_framework import serializers

from .models import SearchHistory

#Serializer for serializing the book details
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ['title', 'cover_image', 'amazon_url', 'flipkart_url', 'good_reads_review']