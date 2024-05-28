'''
Necessary Packages
'''
from bs4 import BeautifulSoup
import requests

'''global variable for product '''
product_soup = None

'''
In this class a customer can search for a mobile or any product
it will give the basic details like Price, Specifications and customer reviews
so that it will be easier for the customers to make a purchase
'''
class FlipkartResult:
    '''
    Initializing the search query of the product
    '''
    def __init__(self,search_query):
        self.search_query = search_query
        
    def flipkart(self):
        '''
        This function will search the product in flipkart website and identify the URL
        then return the product name
        '''
        global product_soup
        
        base_url = f'https://www.flipkart.com/search?q={self.search_query}'

        try:
            response = requests.get(base_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return 'Error',e

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            product_url = soup.find('a', class_ = 'VJA3rP')
            if product_url:
                exact_url = 'https://www.flipkart.com' + product_url['href']
                
                try:
                    product_response = requests.get(exact_url)
                    product_response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    return 'Error',e
                
                if product_response.status_code == 200:
                    product_soup = BeautifulSoup(product_response.content,'html.parser')
                    name = product_soup.find('span', class_ = 'B_NuCI')
                    return name.text
                else:
                   return 'Unable to fetch the product'
            else:
                return 'Unable to find the product URL'
        else:
            return 'Unable to Process the request'
            
    def price_of_the_product(self):
        '''
        This function will return the Price of the product
        '''
        price_element = product_soup.find('div', class_ = '_30jeq3 _16Jk6d')
        if price_element:
            return f"The Price of the Product is {price_element.text}"
        else:
            return "Not able to find the price of the Product"
            
    def specifications(self):
        '''
        This function will return the specifications of the product
        Generally the specifications will be categorized into many attributes 
        in this function it will return all the listed specifications of the product
        '''
        general_div = product_soup.find('div', class_ ='flxcaE', string = 'General' )
        if general_div:
            general_table = general_div.find_next('table', class_ = '_14cfVK')

            for row1 in general_table.find_all('tr', class_ = '_1s_Smc row'):
                datas1 = row1.find_all('td')
                for data1 in datas1:
                    print(data1.text.strip())
                
        display_features_div = product_soup.find('div', class_ = 'flxcaE', string = 'Display Features')
        if display_features_div:
            display_features_table = display_features_div.find_next('table', class_ = '_14cfVK')

            for row2 in display_features_table.find_all('tr', class_ = '_1s_Smc row'):
                datas2 = row2.find_all('td')
                for data2 in datas2:
                    print(data2.text.strip())
                    
                    
        os_performance_div = product_soup.find('div', class_ = 'flxcaE', string = 'Os & Processor Features')
        if os_performance_div:
            os_performance_table = os_performance_div.find_next('table', class_ = '_14cfVK')

            for row3 in os_performance_table.find_all('tr', class_ = '_1s_Smc row'):
                datas3 = row3.find_all('td')
                for data3 in datas3:
                    print(data3.text.strip()) 
                    
                    
        memory_div = product_soup.find('div', class_ = 'flxcaE', string = 'Memory & Storage Features')
        if memory_div:
            memory_table = memory_div.find_next('table', class_ = '_14cfVK')

            for row4 in memory_table.find_all('tr', class_ = '_1s_Smc row'):
                datas4 = row4.find_all('td')
                for data4 in datas4:
                    print(data4.text.strip()) 
                    
        camera_div = product_soup.find('div', class_ = 'flxcaE', string = 'Camera Features')
        if camera_div:
            camera_table = camera_div.find_next('table', class_ = '_14cfVK')

            for row5 in camera_table.find_all('tr', class_ = '_1s_Smc row'):
                datas5 = row5.find_all('td')
                for data5 in datas5:
                    print(data5.text.strip())
                
    def ratings(self):
        '''
        This function will return the Ratings given by the customers
        '''
        ratings_div = product_soup.find('div',class_ = 'gUuXy- _16VRIQ')
        ratings = ratings_div.find('div', class_ = '_3LWZlK')
        reviewers = ratings_div.find('span', class_ = '_2_R_DZ')
        return f'The product rating is:{ratings.text} which is from {reviewers.text}'

'''
Getting information about the products
'''
product_1 = FlipkartResult('Samsung S24 ultra')
product_2 = FlipkartResult('Iphone 15 pro max')
product_3 = FlipkartResult('oneplus 12')
print(product_1.flipkart())
print()
print(product_1.price_of_the_product())
print()
print(product_1.specifications())
print()
print(product_1.ratings())
print()
print()
print(product_2.flipkart())
print()
print(product_2.price_of_the_product())
print()
print(product_2.specifications())
print()
print(product_2.ratings())
print()
print()
print(product_3.flipkart())
print()
print(product_3.price_of_the_product())
print()
print(product_3.specifications())
print()
print(product_3.ratings())