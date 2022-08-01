import pandas as pd

# load data
# accessed from https://www.kaggle.com/datasets/knightbearr/sales-product-data

jan = pd.read_csv('Sales_January_2019.csv')
feb = pd.read_csv('Sales_February_2019.csv')
mar = pd.read_csv('Sales_March_2019.csv')
apr = pd.read_csv('Sales_April_2019.csv')
may = pd.read_csv('Sales_May_2019.csv')
jun = pd.read_csv('Sales_June_2019.csv')
jul = pd.read_csv('Sales_July_2019.csv')
aug = pd.read_csv('Sales_August_2019.csv')
sep = pd.read_csv('Sales_September_2019.csv')
oct = pd.read_csv('Sales_October_2019.csv')
nov = pd.read_csv('Sales_November_2019.csv')
dec = pd.read_csv('Sales_December_2019.csv')

# combine into single data frame

data = pd.concat([jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec])

# reset the index to make possible coding more smooth

data.reset_index(inplace = True)

# convert columns to proper types
# "Quantity Ordered" to numeric
# "Price Each" to float
# "Order Date" to datetime

data['Quantity Ordered'] = pd.to_numeric(data['Quantity Ordered'], errors = 'coerce')
data['Price Each'] = pd.to_numeric(data['Price Each'], errors = 'coerce')
data['Order Date'] = pd.to_datetime(data['Order Date'], errors = 'coerce')

# create a total price column

data['total price'] = data['Quantity Ordered'] * data['Price Each']

# extract hour, month, day, and dayofweek from "Order Date"

data['hour'] = data['Order Date'].dt.hour
data['month'] = data['Order Date'].dt.month
data['day'] = data['Order Date'].dt.day
data['dayofweek'] = data['Order Date'].dt.dayofweek

# extract zip code from the address
# this should be more than sufficient to make judgments based on location

data['zip'] = data['Purchase Address'].str.extract(r'(\d{5}\-?\d{0,4})')

# the data has a number of rows that have null values, they seem to be blank across all metrics
# just to double check, a quick skim over the data frame will be done

'''print(data.info())

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(data[data['Order ID'].isna()])'''

# since it seems like the null rows are all blank, they can be dropped

data = data.dropna()

# export to a new csv

data.to_csv("sales_data_2019.csv", index=False)