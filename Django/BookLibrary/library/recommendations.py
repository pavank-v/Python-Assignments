import requests

'''This class returns the Top 10 Books using Google API'''
class Recommendations:
    
    #This function returns the top 10 fiction books
    def fiction():
        url = "https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=relevance&maxResults=10"
        response = requests.get(url)
        if response.status_code == 200:
            books_data = response.json()
            books = books_data.get("items", [])
            top_books = []
            for book in books:
                book_info = {
                    'title': book['volumeInfo'].get('title'),
                    'authors': book['volumeInfo'].get('authors', []),
                    'publishedDate': book['volumeInfo'].get('publishedDate'),
                    'thumbnail': book['volumeInfo'].get('imageLinks', {}).get('thumbnail'),
                    'description':book['volumeInfo'].get('description'),
                }
                top_books.append(book_info)
            return top_books
        else:
            return []
    
    #This function returns the top 10 non-fiction books  
    def non_fiction():
        url = "https://www.googleapis.com/books/v1/volumes?q=subject:nonfiction&orderBy=relevance&maxResults=10"
        response = requests.get(url)
        if response.status_code == 200:
            books_data = response.json()
            books = books_data.get("items", [])
            top_books = []
            for book in books:
                book_info = {
                    'title': book['volumeInfo'].get('title'),
                    'authors': book['volumeInfo'].get('authors', []),
                    'publishedDate': book['volumeInfo'].get('publishedDate'),
                    'thumbnail': book['volumeInfo'].get('imageLinks', {}).get('thumbnail'),
                    'description':book['volumeInfo'].get('description'),
                }
                top_books.append(book_info)
            return top_books
        else:
            return []