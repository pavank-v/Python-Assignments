from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .forms import SearchBook
from .models import Book, SearchHistory
from .book_details import BookDetails
from .serializers import BookSerializer
from .recommendations import Recommendations

'''Home Page View'''
class Home(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def home(request):
        if request.user.is_authenticated:
            return render(request, 'library/home.html')
        else:
            return render(request, 'authentication/signin.html')
        
'''This class returns the Search result of the Book'''
class SearchBooks(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get(self, request, format=None):
        input_serializer = BookSerializer()
        return render(request, 'library/base.html', {'form':input_serializer})

    def post(self, request, format=None):
        input_serializer = BookSerializer(data=request.data)
        if input_serializer.is_valid():
            title = input_serializer.validated_data['title'].title()
            details = BookDetails(title)
            amazon_url = details.amazon_link
            flipkart_url = details.flipkart_link
            good_reads_review = details.good_reads_review
            cover_image = details.cover_image
            # Record search history
            if not SearchHistory.objects.filter(title=title, user=request.user).exists():
                search = SearchHistory.objects.get_or_create(
                    user = request.user,
                    title=title,
                    defaults={
                        'cover_image': cover_image,
                        'amazon_url': amazon_url,
                        'flipkart_url': flipkart_url,
                        'good_reads_review': good_reads_review
                    }
                )
                if isinstance(search, tuple):
                    search = search[0]
            else:
                search = SearchHistory.objects.get(title=title, user=request.user)
            
            
            output_serializer = BookSerializer(search)
            context = {
                'book_data':output_serializer.data
            }
            return render(request, 'library/search_result.html', context)
        
'''This class adds the book to favorite page'''       
class AddToFavorite(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def post(self, request, format=None):

        if not Book.objects.filter(title=request.POST.get('title')).exists():
            Book.objects.get_or_create(
                    title=request.POST.get('title'),
                    user=request.user,
                    defaults={
                        'cover_image': request.POST.get('cover_image'),
                        'amazon_url': request.POST.get('amazon_url'),
                        'flipkart_url': request.POST.get('flipkart_url'),
                        'good_reads_review': request.POST.get('good_reads_review')
                    }
                )
        return redirect('favorites') 
    
    def get(self, request, format=None):
        return redirect('home')

'''This class returns the list of favorite books'''
class Favorites(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get(self, request, format=None):
        books = Book.objects.filter(user=request.user).order_by('-id')
        return render(request, "library/favorites.html",{'books':books})

'''This is the Home page Base view'''
class Base(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get(self, request, format=None):
        if request.user.is_authenticated:
            form = SearchBook()
            fiction = Recommendations.fiction()
            non_fiction = Recommendations.non_fiction()
            context = {
                'form':form,
                'fiction':fiction,
                'non_fiction':non_fiction,
            }
            return render(request, 'library/base.html', context)
        else:
            return render(request, 'authentication/signin.html')
        
'''This Class returns the Search history'''   
class History(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def get(self, request, format=None):
        search_history = SearchHistory.objects.filter(user=request.user).order_by('-id')
        return render(request, 'library/search_history.html', {'search_history': search_history})
