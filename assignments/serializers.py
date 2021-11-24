from typing import OrderedDict
from rest_framework import serializers

from .models import Assignment, Question, Choice, SpecifiedAssignment
from accounts.models import User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)
   
    class Meta:
        model = Question
        fields = ('id', 'question', 'choices', 'order')


class AssignmentSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    doctor = StringSerializer(many=False)

    class Meta:
        model = Assignment
        fields = ('__all__')

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions

    def create(self, request):
        data = request.data

        assignment = Assignment()
        doctor = User.objects.get(username=data['doctor'])
        assignment.doctor = doctor
        assignment.title = data['title']
        assignment.save()

        order = 1
        for q in data['questions']:
            newQ = Question()
            newQ.question = q['title']
            newQ.order = order
            newQ.save()

            for c in q['choices']:
                newC = Choice()
                newC.title = c
                newC.save()
                newQ.choices.add(newC)

            newQ.answer = Choice.objects.get(title=q['answer'])
            newQ.assignment = assignment
            newQ.save()
            order += 1
        return assignment


class SpecifiedAssignmentSerializer(serializers.ModelSerializer):
    patient = StringSerializer(many=False)
    
    class Meta:
        model = SpecifiedAssignment
        fields = ('__all__')

    def create(self, request):
        data = request.data

        assignment = Assignment.objects.get(id=data['asntId'])
        patient = User.objects.get(username=data['username'])

        specified_asnt = SpecifiedAssignment()
        specified_asnt.assignment = assignment
        specified_asnt.patient = patient

        questions = [q for q in assignment.questions.all()]
        answers = [data['answers'][a] for a in data['answers']]

        answered_correct_count = 0
        for i in range(len(questions)):
            if questions[i].answer.title == answers[i]:
                answered_correct_count += 1
            i += 1

        grade = answered_correct_count / len(questions) * 100
        specified_asnt.grade = grade
        specified_asnt.save()
        return specified_asnt
