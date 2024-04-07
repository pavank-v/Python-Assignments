'''Importing the necessary Packages'''
from bs4 import BeautifulSoup
import requests

'''
In this class based on the user Book input, it will return the Price and URL of the book
from E-Commerce websites like Amazon and FlipKart, it will also return the reviews from GoodReads
'''
class BookLibrary:
    
    '''initializing the search query of the book'''
    def __init__(self,search_query):
        self.flipkart_url = f'https://www.flipkart.com/search?q={search_query}'
        self.amazon_url = f'https://www.amazon.com/s?k={search_query}'
        self.good_reads_url = f'https://www.goodreads.com/search?q={search_query}'
        
        '''User Agent to Avoid the Site from Blocking "COPIED FROM DIGITAL OCEAN" '''
        self.headers = {'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'}
        
    '''This function will return the Price of the Book in Flipkart and URL to buy the Book'''
    def flipkart_price_and_link(self):
        
        try:
            flipkart_response = requests.get(self.flipkart_url)
            flipkart_response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException('Error occurred during request:', e)
        
        if flipkart_response.status_code == 200:
            flipkart_response_soup = BeautifulSoup(flipkart_response.content,'html.parser')
            book_in_flipkart = flipkart_response_soup.find('a', class_ = 's1Q9rs')
                
            if book_in_flipkart:
                book_url_in_fk = f'https://www.flipkart.com' + book_in_flipkart['href']
                
                try:
                    flipkart_book_response = requests.get(book_url_in_fk)
                    flipkart_book_response.raise_for_status()
                    
                except requests.exceptions.RequestException as e:
                    raise requests.exceptions.RequestException('Error occurred during request:', e)
                    
                if flipkart_book_response.status_code == 200:
                    flipkart_book_response = BeautifulSoup(flipkart_book_response.content,'html.parser')
                    flipkart_book_price = flipkart_book_response.find('div',class_ = '_30jeq3 _16Jk6d')
                    return \
                        f'The URL of the Book in FlipKart is: \n{book_url_in_fk} \n' \
                        f'The Price of the Book in FlipKart is: \n{flipkart_book_price.text}'
                            
                else:
                    return 'The Book is not Available in FlipKart'
                    
            else:
                return 'The URL of the Book is not found in FlipKart'
            
        else:
            return 'No Response from FlipKart'
            
    '''This function will return the Price of the Book in Amazon and URL to buy the Book'''
    def amazon_price_and_link(self):
        
        try:
            amazon_response = requests.get(self.amazon_url, headers=self.headers)
            amazon_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException('Error occurred during request:', e)
            
        if amazon_response.status_code == 200:
            amazon_response_soup = BeautifulSoup(amazon_response.content, 'html.parser')
            book_in_amazon = amazon_response_soup.find('a', class_ = 'a-link-normal s-no-outline')
            
            if book_in_amazon:
                book_url_in_ama = 'https://www.amazon.com' + book_in_amazon['href']
                
                try:
                    amazon_book_response = requests.get(book_url_in_ama, headers=self.headers)
                    amazon_book_response.raise_for_status()
                    
                except requests.exceptions.RequestException as e:
                    raise requests.exceptions.RequestException('Error occurred during request:', e)
                    
                if amazon_book_response.status_code == 200:
                    amazon_book_soup = BeautifulSoup(amazon_book_response.content, 'html.parser')
                    price_of_book_ama = amazon_book_soup.find('span', class_ = 'a-size-base a-color-secondary')
                    return \
                        f'The URL of the Book in Amazon is: \n{book_url_in_ama}\n'\
                        f'the Price of the Book in Amazon is: \n{price_of_book_ama.text}\n'
                    
                else:
                    return 'The Book is not Available in Amazon'
            else:
                return 'The URL of the Book is not found in Amazon'
        else:
            return 'No Response from Amazon'
        
    '''This function will return the Reviews of the Book from GoodReads'''
    def reviews_from_goodreads(self):
        review_list =[]
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
                    reviewer_name = good_reads_soup.findAll('div', class_ = "ReviewerProfile__name")
                    review_content = good_reads_soup.findAll('section', class_ = 'ReviewText')
                    
                    for i in range(len(reviewer_name)):
                        name =reviewer_name[i].text
                        review = review_content[i].text
                        review_list.append((name,review))
                    return \
                        f'The Rating for the Book is{stars.text}\n'\
                        f'the Reviews are {review_list}'
                        
                else:
                    return 'The Book is not Available in GoodReads'
            else:
                return 'The URL of the Book is not found in GoodReads'
        else:
            return 'No Response from GoodReads'
                
'''Dictionary which contains all the Books information'''
def initialize_library():
    
    book_list = {'book_1' : {'author_name' : 'Joseph Murphy', 'book_name' : 'The Power of Your Subconcious Mind'},
                'book_2' : {'author_name' : 'Alex Hormozi, Alexander Hormozi, et al', 'book_name' : '100M Offers'},
                'book_3' : {'author_name' : 'Alex Harmozi', 'book_name' : '100M Leads'},
                'book_4' : {'author_name' : 'Robert T. Kiyosaki', 'book_name' : 'Rich Dad, Poor Dad'},
                'book_5' : {'author_name' : 'Paulo Coelho', 'book_name' : 'The Alchemist'},
                'book_6' : {'author_name' : 'Mark Manson', 'book_name' : 'The Subtle Art of Not Giving a F*ck'},
                'book_7' : {'author_name' : 'George S. Clason', 'book_name' : 'The Richest Man in Babylon'},
                'book_8' : {'author_name' : 'James Clear', 'book_name' : 'Atomic Habits'},
                'book_9' : {'author_name' : 'Dan Sullivan', 'book_name' : 'Who Not How'},
                'book_10' : {'author_name' : 'Jeff Bezos', 'book_name' : 'Invent and Wander'},
                }


    return book_list

'''Printing the Dictionary as list so that it will be Easy for User to Read'''
def main():
    book_list = initialize_library()
    print("The list of books in the Library are:")
    for index, books in enumerate(book_list):
        print(index+1, list(book_list[books].values()))

    '''Getting the Book's input from User'''
    book_input = int(input("Enter the Book's Number:"))
    number_of_the_book = 'book_'+str(book_input)

    if book_input <= 10 and book_input >= 1:
        '''
        immplemented a list for each book.
        It contains Book Name and Author Name
        '''
        li=list(book_list[number_of_the_book].values())
        print(f'''Book's Name:"{li[1]}" Author's Name:"{li[0]}"''')
        search_query = li[1] 
        
        '''Object Creation'''
        booklib = BookLibrary(search_query) 
        
        '''Calling the functions'''
        try:
            print(booklib.flipkart_price_and_link())
        except requests.exceptions.RequestException as e:
            print('Error Occured due to', e)
        try:
            print(booklib.amazon_price_and_link())
        except requests.exceptions.RequestException as e:
            print('Error Occured due to', e)
        try:
            print(booklib.reviews_from_goodreads())
        except requests.exceptions.RequestException as e:
            print('Error Occured due to', e)
            
    else:
        print('Please Enter a valid index')
'''Calling main'''       
if __name__ == "__main__":
    main()