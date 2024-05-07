'''Importing the necessary Packages'''
from bs4 import BeautifulSoup
import requests
# import matplotlib.pyplot as plt
# from PIL import Image
# from io import BytesIO

class BookDetails:
    
    '''initializing the search query of the book'''
    def __init__(self,search_query):
        
        self.flipkart_url = f'https://www.flipkart.com/search?q={search_query}'
        self.amazon_url = f'https://www.amazon.in/s?k={search_query}'
        self.good_reads_url = f'https://www.goodreads.com/search?q={search_query}'
        self.cover_picture = f'https://www.goodreads.com/search?q={search_query}'
        
        '''User Agent to Avoid the Site from Blocking "COPIED FROM DIGITAL OCEAN" '''
        self.headers = {'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'}
        
    '''This function will return the cover picture of the book'''
    def cover_image(self):
        
        try:
            good_reads_response = requests.get(self.good_reads_url, headers=self.headers)
            good_reads_response.raise_for_status()
            
            if good_reads_response.status_code == 200:
                good_reads_response_soup = BeautifulSoup(good_reads_response.content, 'html.parser') 
                book_link = good_reads_response_soup.find('a', class_='bookTitle')
                
                if book_link:
                    book_url_in_gr = "https://www.goodreads.com" + book_link['href']
                    book_response = requests.get(book_url_in_gr)
                    book_response.raise_for_status()
                    
                    if book_response.status_code == 200:
                        book_soup = BeautifulSoup(book_response.content, 'html.parser')
                        cover_image = book_soup.find('img', class_="ResponsiveImage")
                        img_url = cover_image['src']
                        return img_url
                        # if img_url:
                        #     img_response = requests.get(img_url)
                        #     img_response.raise_for_status()
                        #     #Open the image using PIL
                        #     img = Image.open(BytesIO(img_response.content))
                        #     #Plot the image
                        #     imgplot = plt.imshow(img)
                        #     plt.axis('off')
                        #     plt.show()
                        # else:
                        #     print("Cover image not found.")
                    else:
                        print("Failed to retrieve book page from Goodreads.")
                else:
                    print("Book link not found on Goodreads page.")
            else:
                print("Failed to retrieve data from Goodreads.")
        
        except requests.exceptions.RequestException as e:
            print("Error occurred during request:", e)
            
    '''This function will return the Flipkart URL to buy the Book'''    
    def flipkart_link(self):
        
        try:
            flipkart_response = requests.get(self.flipkart_url)
            flipkart_response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException('Error occurred during request:', e)
        
        if flipkart_response.status_code == 200:
            flipkart_response_soup = BeautifulSoup(flipkart_response.content,'html.parser')
            book_in_flipkart = flipkart_response_soup.find('a', class_ = 'VJA3rP')
                
            if book_in_flipkart:
                book_url_in_fk = f'https://www.flipkart.com' + book_in_flipkart['href']
                return book_url_in_fk
                    
            else:
                return 'The URL of the Book is not found in FlipKart'
            
        else:
            return 'No Response from FlipKart'
            
    '''This function will return the Amazon URL to buy the Book'''
    def amazon_link(self):
        
        try:
            amazon_response = requests.get(self.amazon_url, headers=self.headers)
            amazon_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException('Error occurred during request:', e)
            
        if amazon_response.status_code == 200:
            amazon_response_soup = BeautifulSoup(amazon_response.content, 'html.parser')
            book_in_amazon = amazon_response_soup.find('a', class_ = 'a-link-normal s-no-outline')
            
            if book_in_amazon:
                book_url_in_ama = 'https://www.amazon.in' + book_in_amazon['href']
                return book_url_in_ama

            else:
                return 'The URL of the Book is not found in Amazon'
        else:
            return 'No Response from Amazon'
        
    '''This function will return the Rating of the Book from GoodReads'''
    def good_reads_review(self):
        try:
            good_reads_response = requests.get(self.good_reads_url, headers=self.headers)
            good_reads_response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException('Error occurred during request:', e)
        
        if good_reads_response.status_code == 200:
            good_reads_response_soup = BeautifulSoup(good_reads_response.content, 'html.parser') 
            good_reads_response = good_reads_response_soup.find('a', class_ = 'bookTitle')
            
            if good_reads_response:
                book_url_in_gr = "https://www.goodreads.com" + good_reads_response['href']
                
                try:
                    good_reads_book = requests.get(book_url_in_gr, headers=self.headers)
                    good_reads_book.raise_for_status()
                    
                except requests.exceptions.RequestException as e:
                    raise requests.exceptions.RequestException('Error occurred during request:', e)
                
                if good_reads_book.status_code == 200:
                    good_reads_soup = BeautifulSoup(good_reads_book.content, 'html.parser')
                
                    stars = good_reads_soup.find('div', class_ = 'RatingStatistics__rating')
                    
                    return float(stars.text)
                        
                else:
                    return 'The Book is not Available in GoodReads'
            else:
                return 'The URL of the Book is not found in GoodReads'
        else:
            return 'No Response from GoodReads'
