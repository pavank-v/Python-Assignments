'''Importing the Necessary Packages'''
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import seaborn as sns
import matplotlib.pyplot as plt

''' Class creation for Sales'''
class SalesScript:
    
    '''Initializing the sales_df for further process'''
    def __init__(self,sales_df):
        self.sales_df = sales_df
        self.bikes_df = self.sales_df[self.sales_df['PRODUCTLINE'] == 'Motorcycles']
        self.cars_df = self.sales_df[self.sales_df['PRODUCTLINE'] == 'Classic Cars']
        self.truck_bus_df = self.sales_df[self.sales_df['PRODUCTLINE'] == 'Trucks and Buses']
        self.v_cars_df = self.sales_df[self.sales_df['PRODUCTLINE'] == 'Vintage Cars']
        self.planes_df = self.sales_df[self.sales_df['PRODUCTLINE'] == 'Planes']
        self.ships_df = self.sales_df[self.sales_df['PRODUCTLINE'] == 'Ships']
    
    '''This function will return the Product Line'''   
    def list_of_products(self):
        products = self.sales_df['PRODUCTLINE'].unique()
        return f'The Products are:{products}'
    
    '''This Function returns the Products which Sold the most'''   
    def top_sales(self):
        
        self.max_sales_bike = self.bikes_df.loc[self.bikes_df['SALES'].idxmax()]
        desired_col_bike = self.max_sales_bike[['ORDERNUMBER', 'PRODUCTLINE']]
        self.max_sales_cars = self.cars_df.loc[self.cars_df['SALES'].idxmax()]
        desired_col_cars = self.max_sales_cars[['ORDERNUMBER', 'PRODUCTLINE']]
        self.max_sales_truck_bus = self.truck_bus_df.loc[self.truck_bus_df['SALES'].idxmax()]
        desired_col_truck_bus = self.max_sales_truck_bus[['ORDERNUMBER', 'PRODUCTLINE']]
        self.max_sales_vcars = self.v_cars_df.loc[self.v_cars_df['SALES'].idxmax()]
        desired_col_vcars = self.max_sales_vcars[['ORDERNUMBER', 'PRODUCTLINE']]
        self.max_sales_planes = self.planes_df.loc[self.planes_df['SALES'].idxmax()]
        desired_col_planes = self.max_sales_planes[['ORDERNUMBER', 'PRODUCTLINE']]
        self.max_sales_ships = self.ships_df.loc[self.ships_df['SALES'].idxmax()]
        desired_col_ships = self.max_sales_ships[['ORDERNUMBER', 'PRODUCTLINE']]
        
        return f'\
        The Top Performer in sales for MotorCycles is:\n{desired_col_bike}\n\
        The Top Performer in sales for Classic Cars is:\n{desired_col_cars}\n\
        The Top Performer in sales for Trucks and Buses is:\n{desired_col_truck_bus}\n\
        The Top Performer in sales for Vintage Cars is:\n{desired_col_vcars}\n\
        The Top Performer in sales for Planes is:\n{desired_col_planes}\n\
        The Top Performer in sales for Ships is:\n{desired_col_ships}\n'
                
    '''This function will return the Products which most Quantities sold'''           
    def most_quantities_ordered(self):
        
        max_quantities_ordered_bike = self.bikes_df.loc[self.bikes_df['QUANTITYORDERED'].idxmax()]
        desired_col_bike = max_quantities_ordered_bike[['ORDERNUMBER', 'PRODUCTLINE']]
        max_quantities_ordered_cars = self.cars_df.loc[self.cars_df['QUANTITYORDERED'].idxmax()]
        desired_col_cars = max_quantities_ordered_cars[['ORDERNUMBER', 'PRODUCTLINE']]
        max_quantities_ordered_truck_bus = self.truck_bus_df.loc[self.truck_bus_df['QUANTITYORDERED'].idxmax()]
        desired_col_truck_bus = max_quantities_ordered_truck_bus[['ORDERNUMBER', 'PRODUCTLINE']]
        max_quantities_ordered_vcars = self.v_cars_df.loc[self.v_cars_df['QUANTITYORDERED'].idxmax()]
        desired_col_vcars = max_quantities_ordered_vcars[['ORDERNUMBER', 'PRODUCTLINE']]
        max_quantities_ordered_planes = self.planes_df.loc[self.planes_df['QUANTITYORDERED'].idxmax()]
        desired_col_planes = max_quantities_ordered_planes[['ORDERNUMBER', 'PRODUCTLINE']]
        max_quantities_ordered_ships = self.ships_df.loc[self.ships_df['QUANTITYORDERED'].idxmax()]
        desired_col_ships = max_quantities_ordered_ships[['ORDERNUMBER', 'PRODUCTLINE']]
        
        return f'\
        The Top Performer in Quantities Ordered for MotorBikes is:\n{desired_col_bike}\n\
        The Top Performer in Quantities Ordered for Classic Cars is:\n{desired_col_cars}\n\
        The Top Performer in Quantities Ordered for Trucks and Buses is:\n{desired_col_truck_bus}\n\
        The Top Performer in Quantities Ordered for Vintage Cars is:\n{desired_col_vcars}\n\
        The Top Performer in Quantities Ordered for Planes is:\n{desired_col_planes}\n \
        The Top Performer in Quantities Ordered for Ships is:\n{desired_col_ships}'
                
    '''This function will return the Profit of Single unit of Top Products'''           
    def profit_for_top_products(self):
        
        self.profit_for_single_bike = self.max_sales_bike['PRICE'] - self.max_sales_bike['MSRP']
        self.profit_for_single_car = self.max_sales_cars['PRICE'] - self.max_sales_cars['MSRP']
        self.profit_for_single_truck_bus = self.max_sales_truck_bus['PRICE'] - self.max_sales_truck_bus['MSRP']
        self.profit_for_single_vcar = self.max_sales_vcars['PRICE'] - self.max_sales_vcars['MSRP']
        self.profit_for_single_plane = self.max_sales_planes['PRICE'] - self.max_sales_planes['MSRP']
        self.profit_for_single_ship = self.max_sales_ships['PRICE'] - self.max_sales_ships['MSRP']
        
        return f'\
        Profit for Single Unit of MotorCycle is:{self.usd_to_inr(self.profit_for_single_bike):.2f}\n\
        Profit for Single Unit of Classic Cars is:{self.usd_to_inr(self.profit_for_single_car):.2f}\n\
        Profit for Single Unit of Trucks and Buses is:{self.usd_to_inr(self.profit_for_single_truck_bus):.2f}\n\
        Profit for Single Unit of Vintage Cars is:{self.usd_to_inr(self.profit_for_single_vcar):.2f}\n\
        Profit for Single Unit of Planes is:{self.usd_to_inr(self.profit_for_single_plane):.2f}\n\
        Profit for Single Unit of Ships is:{self.usd_to_inr(self.profit_for_single_ship):.2f}\n'
    
    '''This Function will return the Total Profit gained by the Top Products'''
    def total_profit(self):
        
        profit_for_bikes = self.profit_for_single_bike * self.max_sales_bike['QUANTITYORDERED']
        profit_for_cars = self.profit_for_single_car * self.max_sales_cars['QUANTITYORDERED']
        profit_for_truck_bus = self.profit_for_single_truck_bus * self.max_sales_truck_bus['QUANTITYORDERED']
        profit_for_vcars = self.profit_for_single_vcar * self.max_sales_vcars['QUANTITYORDERED']
        profit_for_planes = self.profit_for_single_plane * self.max_sales_planes['QUANTITYORDERED']
        profit_for_ships = self.profit_for_single_ship * self.max_sales_ships['QUANTITYORDERED']
        
        return f'\
        The Total Profit for MotorCycles is:{self.usd_to_inr(profit_for_bikes):.2f}\n\
        The Total Profit for Cars is :{self.usd_to_inr(profit_for_cars):.2f}\n\
        The Total Profit for Trucks and Buses is:{self.usd_to_inr(profit_for_truck_bus):.2f}\n\
        The Total Profit for Vintage Cars is:{self.usd_to_inr(profit_for_vcars):.2f}\n\
        The Total Profit for Planes is:{self.usd_to_inr(profit_for_planes):.2f}\n\
        The Total Profit for Ships is:{self.usd_to_inr(profit_for_ships):.2f}\n'
                
    '''In this function it will calculate the profit of each and every product and will create a new column called 'PROFIT'.
        The Output will be stored in the given file location'''        
    def profit_for_all_products(self):
        
        all_profit = self.sales_df
        all_profit['PROFIT'] = (all_profit['SALES'] - all_profit['MSRP']) * all_profit['QUANTITYORDERED']
        all_profit.drop(['ORDERDATE', 'STATUS', 'YEAR', 'CUSTOMERNAME', 'CITY', 'STATE', 'POSTALCODE', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME'], axis = 1, inplace=True)
        data = all_profit.to_csv()
        
        csv_output_file = 'assignment_6_pavan\output.csv'
        with open(csv_output_file,'w',newline='') as file:
            file.write(data)
        
        return f'All the Unnecessary Columns are removed and the Output of is saved in {csv_output_file}'
        
    '''In the Dataset the currency is USD so in order to convert it to INR, multiplying the USD with current Exchange Rates of INR,
        which is webscrapped from the website called 'xe.com' ''' 
        
    def usd_to_inr(self,usd:float):
        
        search_query = 'Amount=1&From=USD&To=INR'
        url_for_conversion = f'https://www.xe.com/currencyconverter/convert/?{search_query}'
        
        try:
            xe_request = requests.get(url_for_conversion)
            xe_request.raise_for_status()
            time.sleep(3)
        except requests.exceptions.RequestException as e:
            return f'Error Occured due to {e}'
        
        if xe_request.status_code == 200:
            
            google_response = BeautifulSoup(xe_request.content, 'html.parser')
            exchange_rate = google_response.find('p',class_='sc-1c293993-1 fxoXHw')
            current_exchange_rate = exchange_rate.contents[0]
            current_exchange_rate = float(current_exchange_rate)
            return float(current_exchange_rate)*usd
        
        else:
            return 'There is a Problem Fetching in Currency Rates'
    
    '''In this function we represent the Top Products interms of Sales by graphic visualization'''           
    def visualization_of_top_performers(self):
        
        sales_sorted = self.sales_df.sort_values(by='SALES', ascending=False)
        top_products = sales_sorted['PRODUCTCODE'].head(20)
        top_sales = sales_sorted['SALES'].head(20)
        '''using the barplot'''
        sns.barplot(x = top_products,y = top_sales,data = sales_sorted.head(20) ,palette='inferno')
        '''setting labels for both axes'''
        plt.xlabel('Product ID')
        plt.ylabel('Sales')
        '''label rotation'''
        plt.xticks(rotation=90)
        '''Title'''
        plt.title('Top Products by Sales')
        time.sleep(2) #Visualiztion Delay
        plt.show()
        
'''All the instances and function calls are in this function'''    
    
def main():
    
    '''Reading the file using open'''
    time.sleep(1)
    csvfile = open(r'assignment_6_pavan\sales_data.csv',newline='')
    x = csv.DictReader(csvfile, delimiter=',')
    '''Creating a DataFrame'''
    sales_df = pd.DataFrame(x)
    
    ''' Converting the columns datatype for calculations'''
    sales_df[['SALES', 'PRICE', 'MSRP', 'QUANTITYORDERED']] = \
        sales_df[['SALES', 'PRICE', 'MSRP', 'QUANTITYORDERED']].astype(float)

    #Object Creation
    sales_record = SalesScript(sales_df)
    
    #Calling the functions
    print(sales_record.list_of_products())
    print(sales_record.top_sales())
    print(sales_record.most_quantities_ordered())
    print(sales_record.profit_for_top_products())
    print(sales_record.total_profit())
    print(sales_record.profit_for_all_products())
    print(sales_record.visualization_of_top_performers())
    
'''Calling the main()'''
if __name__ == "__main__":
    main()