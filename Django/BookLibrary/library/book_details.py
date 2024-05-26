from bs4 import BeautifulSoup
import requests
import time

''' This Class will return the Book Details such as 
"Cover Image, Amazon Buy Link, Flipkart Buy Link, Good Reads rating" '''
class BookDetails:
    
    #Initializing the urls for the methods
    def __init__(self, search_query):
        
        self.flipkart = 'https://www.flipkart.com'
        self.flipkart_url = f'{self.flipkart}/search?q={search_query} Book'
        self.amazon = 'https://www.amazon.com'
        self.amazon_url = f'{self.amazon}/s?k={search_query} Book'
        self.good_reads = 'https://www.goodreads.com'
        self.good_reads_url = f'{self.good_reads}/search?q={search_query}'
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"
        }

    #This function returns Cover Image of the Book
    def cover_image(self):     
        try:
            good_reads_response = requests.get(self.good_reads_url, headers=self.headers)
            if not good_reads_response:
                return f"{self.good_reads}/not-found"

            good_reads_response_soup = BeautifulSoup(good_reads_response.content, 'html.parser') 
            book_link = good_reads_response_soup.find('a', class_='bookTitle')
                
            if book_link:
                book_url_in_gr = "https://www.goodreads.com" + book_link['href']
                book_response = requests.get(book_url_in_gr)
                if not book_response:
                    return "https://www.goodreads.com/not-found"

                book_soup = BeautifulSoup(book_response.content, 'html.parser')
                cover_image = book_soup.find('img', class_="ResponsiveImage")
                img_url = cover_image['src']
                return img_url
            else:
                return "The Book is not Found"
        except Exception:
            return f"{self.good_reads}/not-found"

    #This function returns the Flipkart Buy link
    def flipkart_link(self):
        try:
            flipkart_response = requests.get(self.flipkart_url)
            if not flipkart_response:
                return f"{self.flipkart}/not-found"

            flipkart_response_soup = BeautifulSoup(flipkart_response.content, 'html.parser')
            book_in_flipkart = flipkart_response_soup.find('a', class_='VJA3rP')
                
            if book_in_flipkart:
                book_url_in_fk = self.flipkart + book_in_flipkart['href']
                return book_url_in_fk
            else:
                return f"{self.flipkart}/not-found"
        except Exception:
            return f"{self.flipkart}/not-found"

    #This function returns the Amazon Buy link
    def amazon_link(self):
        try:
            amazon_response = requests.get(self.amazon_url, headers=self.headers)
            if not amazon_response:
                return f"{self.amazon}/not-found"

            amazon_response_soup = BeautifulSoup(amazon_response.content, 'html.parser')
            book_in_amazon = amazon_response_soup.find('a', class_='a-link-normal s-no-outline')

            if book_in_amazon:
                book_url_in_ama = self.amazon + book_in_amazon['href']
                return book_url_in_ama
            else:
                return f"{self.amazon}/not-found"
        except Exception:
            return f"{self.amazon}/not-found"

    #This function returns the Good Reads Review
    def good_reads_review(self):
        try:
            good_reads_response = requests.get(self.good_reads_url, headers=self.headers)
            if not good_reads_response:
                return "No Response from GoodReads"

            good_reads_response_soup = BeautifulSoup(good_reads_response.content, 'html.parser') 
            good_reads_response = good_reads_response_soup.find('a', class_ = 'bookTitle')
            
            if good_reads_response:
                book_url_in_gr = self.good_reads + good_reads_response['href']
                good_reads_book = requests.get(book_url_in_gr, headers=self.headers)
                if not good_reads_book:
                    return "The Book is not Available in GoodReads"

                good_reads_soup = BeautifulSoup(good_reads_book.content, 'html.parser')
                stars = good_reads_soup.find('div', class_ = 'RatingStatistics__rating')
                return float(stars.text) if stars else 'Rating not available'
            else:
                return 'The URL of the Book is not found in GoodReads'
        except Exception:
            return "No Response from GoodReads"