from Library.models import BookList
from rest_framework import serializers

''' Taking Executive Login Details '''
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = '__all__'

