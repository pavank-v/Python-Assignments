from bs4 import BeautifulSoup
import requests

book_list = {'book_1' : {'author_name' : 'Joseph Murphy', 'book_name' : 'The Power of Your Subconcious Mind'},
             'book_2' : {'author_name' : 'Napoleon Hill', 'book_name' : 'Think and Grow Rich'},
             'book_3' : {'author_name' : 'Rhonda Byrne', 'book_name' : 'The Secret'},
             'book_4' : {'author_name' : 'Robert T. Kiyosaki', 'book_name' : 'Rich Dad, Poor Dad'},
             'book_5' : {'author_name' : 'Paulo Coelho', 'book_name' : 'The Alchemist'},
             'book_6' : {'author_name' : 'Mark Manson', 'book_name' : 'The Subtle Art of Not Giving a F*ck'},
             'book_7' : {'author_name' : 'George S. Clason', 'book_name' : 'The Richest Man in Babylon'},
             'book_8' : {'author_name' : 'James Clear', 'book_name' : 'Atomic Habits'},
             'book_9' : {'author_name' : 'Dan Sullivan', 'book_name' : 'Who Not How'},
             'book_10' : {'author_name' : 'Jeff Bezos', 'book_name' : 'Invent and Wander'},
             }

for i in book_list:
    li=list(book_list[i].values())
    print(f'''Book:"{li[1]}" Author:"{li[0]}"''')
    
    search_query = li[1]
    flipkart_url = f'https://www.flipkart.com/search?q={search_query}'
    amazon_url = f'https://www.amazon.in/s?k={search_query}'
    good_reads_url = f'https://www.goodreads.com/search?q={search_query}'
    
    '''flipkart'''
    print(flipkart_url)
    try:
        flipkart_response = requests.get(flipkart_url)
        flipkart_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('error',e)
    
    if flipkart_response.status_code == 200:
        flipkart_response_soup = BeautifulSoup(flipkart_response.content,'html.parser')
        book_in_flipkart = flipkart_response_soup.find('a', class_ = '_2rpwqI')
             
        if book_in_flipkart:
            book_url_in_fk = f'https://www.flipkart.com' + book_in_flipkart['href']
            print(book_url_in_fk)
             
            try:
                flipkart_book_response = requests.get(book_url_in_fk)
                flipkart_book_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print('error',e)
                
            if flipkart_book_response.status_code == 200:
                flipkart_book_soup = BeautifulSoup(flipkart_book_response.content,'html.parser')
            else:
                print('not valid')
                
        else:
            print('not found')
        
    else:
        print('not found')
        
    price_of_book_fk = flipkart_book_soup.find('div',class_ = '_30jeq3 _16Jk6d')
    print(price_of_book_fk.text)
    '''end of flipkart'''
    
    '''amazon'''
    print(amazon_url)
    try:
        amazon_response = requests.get(amazon_url)
        amazon_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    else:
        if amazon_response.status_code == 200:
            amazon_response_soup = BeautifulSoup(amazon_response.content, 'html.parser')
            book_in_amazon = amazon_response_soup.find('a', class_='a-link-normal s-no-outline')
            
            if book_in_amazon:
                book_url_in_ama = 'https://www.amazon.in' + book_in_amazon['href']
                print('The URL is:', book_url_in_ama)
            else:
                print('Book not found on Amazon.')
        else:
            print('Failed to retrieve data from Amazon.')
        
    good_reads_response = requests.get(good_reads_url)
    break
    
    
    
    


    