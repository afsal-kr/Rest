from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import recipe,review
from .serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


# class RecipeList(generics.ListCreateAPIView):
#       queryset = recipe.objects.all()
#       serializer_class = RecipeSerializer
#
# class ReviewList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = review.objects.all()
#     serializer_class = ReviewSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = recipe.objects.all()
    serializer_class = RecipeSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = review.objects.all()
    serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_logout(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, request):
        self.request.user.auth_token.delete()
        return Response({'msg': 'Logout Successfully'}, status=status.HTTP_200_OK)

class createvev(APIView):
  #permission_classes=[IsAuthenticated,]
  def post(request):
    r=ReviewSerializer(data=request.data)
    if(r.is_valid):
       r.save()
       return Response(r.data,status=status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)

class detailrev(APIView):
  #permission_classes=[IsAuthenticated,]
  def get_object(request,pk):
     try:
       return recipe.objects.get(pk=pk)
     except:
       raise Http404
     def get(self,request,pk):
       r=self.get_object(pk)
       rev=review.objects.filter(recipe_name=r)
       revdet=ReviewSerializer(rev,many=True)
       return Response(revdet.data)

class Cuisinesearch(APIView):
    def get(self,request):
        query= self.request.query_params.get('cuisine')
        if (query):
            name=recipe.objects.filter(cuisine=query)
            n=RecipeSerializer(name,many=True)
            return Response(n.data)
        return Response('no content',status=status.HTTP_204_NO_CONTENT)

