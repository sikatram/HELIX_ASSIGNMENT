from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Question
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import logging

logger = logging.getLogger('django')

def add_question(request):
    logger.info("Received request to add_question")
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))
        title = ''
        question = ''
        if 'title' in request_data:
            title = request_data['title']
        if 'question' in request_data:
            question = request_data['question']
        if title and question:
            Question.objects.create(title=title, question=question)
            logger.info("SUCCESS: add_question: creating new entry with valid title and question")
            return JsonResponse({'status': 'success'})
        else:
            logger.info("ERROR: add_question: invalid title or question")
    
    logger.info("ERROR: add_question: request can not be processed")
    return JsonResponse({'status': 'error'})


def get_questions(request):
    logger.info("Received request to get_question")
    if request.method == 'GET':
        questions = []
        for question in Question.objects.all():
            questions.append({
                'id': question.id,
                'title': question.title,
                'question': question.question
            })

        logger.info("SUCCESS: get_question: rendering questions")
        return JsonResponse({"questions": questions})


def health(request):
    logger.info("Received request to health")
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)

def empty(request):
    logger.info("Received request to empty")
    return HttpResponse(status=200)
