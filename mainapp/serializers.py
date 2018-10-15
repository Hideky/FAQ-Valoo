from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        """Restrict POST request to username and question field."""
        return Question.objects.create(username=validated_data['username'], question=validated_data['question'])

    class Meta:
        model = Question
        fields = ('id', 'username', 'date', 'question', 'answer', 'hidden')