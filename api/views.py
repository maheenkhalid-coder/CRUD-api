

# APIView method

# from functools import partial
# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework.views import APIView

# from rest_framework.generics import GenericAPIView

# # Create your views here.

# class StudentAPI(APIView):

#     # serializer_class = StudentSerializer

# # This method for get the info
#     def get(self, request, pk = None, format=None):
#         id=pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     # This method for enter the info
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data entered'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#         # This method for update the info
#     def put(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response ({'msg': 'Success data updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     # This method for partial update the info
#     def patch(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response ({'msg': 'partial data updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     # This method for delete the info
#     def delete(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response ({'msg': 'data deleted'})




# GenericAPIView and Model Mixing

# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# # List and create method PK not required

# class LCStudentList(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# # Retrive Update and destroy PK required

# class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs) 



# generics LcAPIVIEW and RUDApiView

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# POST AND GET pk not needed
class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Update AND Destroy pk needed
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



