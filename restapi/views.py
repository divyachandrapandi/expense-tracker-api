# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from django.forms.models import model_to_dict
from restapi import models, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.


class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ["category", "merchant"]
    permission_classes = [HasAPIKey]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    permission_classes = [HasAPIKey]


# class ExpenseListCreate(APIView):
#     def get(self, request):
#         expenses = models.Expense.objects.all()
#         serializer = serializers.Expense(expenses, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = serializers.Expense(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)


# class ExpenseListCreate(APIView):
#     def get(self, request):
#         expenses = models.Expense.objects.all()
#         all_expenses = [model_to_dict(expense) for expense in expenses]
#         return Response(all_expenses, status=200)
#
#     def post(self, request):
#         amount = request.data["amount"]
#         merchant = request.data["merchant"]
#         description = request.data["description"]
#         category = request.data["category"]
#
#         expense = models.Expense.objects.create(
#             amount=amount, merchant=merchant, description=description, category=category
#         )
#         return Response(model_to_dict(expense), status=201)
