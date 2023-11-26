#!/usr/bin/env python
# coding: utf-8

# In[1]:


tesla = yf.Ticker("TSLA")


# In[2]:


get_ipython().system('pip install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip install bs4')
#!pip install plotly

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Define Graphing Function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[3]:


#1
tesla = yf.Ticker("TSLA")

#2
tesla_data = tesla.history(period="max")

#3
tesla_data.reset_index(inplace=True)
tesla_data.head()


# In[4]:


#1
tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_html_data = requests.get(tesla_url).text

#2
tesla_soup = BeautifulSoup(tesla_html_data, "html5lib")

#3
tesla_tables = tesla_soup.find_all('table')

for index,table in enumerate(tesla_tables):
    if ("Tesla Quarterly Revenue" in str(table)):
        tesla_table_index = index

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        tesla_revenue = tesla_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)

#4
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue

#5
tesla_revenue.tail()


# In[7]:


#1
tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_html_data = requests.get(tesla_url).text

#2
tesla_soup = BeautifulSoup(tesla_html_data, "html5lib")

#3
tesla_tables = tesla_soup.find_all('table')

for index,table in enumerate(tesla_tables):
    if ("Tesla Quarterly Revenue" in str(table)):
        tesla_table_index = index

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        tesla_revenue = tesla_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)

#4
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue

#5
tesla_revenue.tail()


# In[8]:


url= "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data=requests.get(url).text


# In[9]:


soup = BeautifulSoup(html_data,"html5lib")


# In[10]:


tesla_revenue= pd.read_html(url, match="Tesla Quarterly Revenue", flavor='bs4')[0]
tesla_revenue=tesla_revenue.rename(columns = {'Tesla Quarterly Revenue(Millions of US $)': 'Date', 'Tesla Quarterly Revenue(Millions of US $).1': 'Revenue'}, inplace = False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",","").str.replace("$","")
tesla_revenue.head()


# In[11]:


import requests

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_data = response.text
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


# In[12]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_data, 'html.parser')


# In[13]:


import pandas as pd

# Find the table with Tesla Quarterly Revenue
table = soup.find('table', {'class': 'historical_data_table'})

# Extract data and create DataFrame
tesla_revenue = pd.read_html(str(table))[0]

# Rename columns
tesla_revenue.columns = ["Date", "Revenue"]

# Remove commas and dollar signs from the Revenue column
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '').str.replace('$', '')

# Remove rows with empty strings or NaN in the Revenue column
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'].notna() & (tesla_revenue['Revenue'] != '')]

# Display the entire DataFrame
print("Entire DataFrame:")
print(tesla_revenue)


# In[14]:


# Display the last 5 rows of the DataFrame
print("\nLast 5 Rows:")
print(tesla_revenue.tail())


# In[15]:


tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_html_data = requests.get(tesla_url).text


# In[16]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_data, 'html.parser')


# In[30]:


tesla_soup = BeautifulSoup(tesla_html_data, "html5lib")
tesla_tables = tesla_soup.find_all('table')
tesla_table_index = index


# In[29]:


for index,table in enumerate(tesla_tables):
    if ("Tesla Quarterly Revenue" in str(table)):
        tesla_table_index = index


# In[25]:


tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])


# In[27]:


for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        tesla_revenue = tesla_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)


# In[31]:


url= "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data=requests.get(url).text


# In[32]:


soup = BeautifulSoup(html_data,"html5lib")


# In[33]:


tesla_revenue= pd.read_html(url, match="Tesla Quarterly Revenue", flavor='bs4')[0]
tesla_revenue=tesla_revenue.rename(columns = {'Tesla Quarterly Revenue(Millions of US $)': 'Date', 'Tesla Quarterly Revenue(Millions of US $).1': 'Revenue'}, inplace = False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",","").str.replace("$","")
tesla_revenue.head()


# In[34]:


import pandas as pd
from bs4 import BeautifulSoup
import requests

# Step 1: Download the webpage
tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_html_data = requests.get(tesla_url).text

# Step 2: Parse HTML with BeautifulSoup
tesla_soup = BeautifulSoup(tesla_html_data, "html5lib")

# Step 3: Find the table with Tesla Quarterly Revenue
tesla_tables = tesla_soup.find_all('table')
tesla_table_index = None

for index, table in enumerate(tesla_tables):
    if "Tesla Quarterly Revenue" in str(table):
        tesla_table_index = index
        break

# Check if the table is found
if tesla_table_index is not None:
    # Step 4: Extract data from the table and create DataFrame
    tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

    for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
        col = row.find_all("td")
        if col:
            date = col[0].text
            revenue = col[1].text.replace("$", "").replace(",", "")
            tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

    # Step 5: Clean the DataFrame and display the last 5 rows
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    print("Tesla Revenue DataFrame:")
    print(tesla_revenue.tail())
else:
    print("Table 'Tesla Quarterly Revenue' not found on the webpage.")


# In[35]:


#1
gamestop = yf.Ticker("GME")

#2
gme_data = gamestop.history(period="max")

#3
gme_data.reset_index(inplace=True)
gme_data.head()


# In[36]:


#1
gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_html_data = requests.get(gme_url).text

#2
gme_soup = BeautifulSoup(gme_html_data, "html5lib")

#3
gme_tables = gme_soup.find_all('table')

for index,table in enumerate(gme_tables):
    if ("GameStop Quarterly Revenue" in str(table)):
        gme_table_index = index

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in gme_tables[gme_table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col !=[]):
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")
        gme_revenue = gme_revenue.append({"Date" : date, "Revenue" : revenue}, ignore_index=True)

#4
gme_revenue.tail()


# In[38]:


# Find the table with Tesla Quarterly Revenue
tesla_tables = tesla_soup.find_all('table')
tesla_table_index = None

for index, table in enumerate(tesla_tables):
    if "Tesla Quarterly Revenue" in str(table) or "Revenue" in str(table):
        tesla_table_index = index
        break
        # Check if the table is found
if tesla_table_index is not None:
    # Step 4: Extract data from the table and create DataFrame
    tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

    for row in tesla_tables[tesla_table_index].tbody.find_all("tr"):
        col = row.find_all("td")
        if col:
            date = col[0].text
            revenue = col[1].text.replace("$", "").replace(",", "")
            tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

    # Step 5: Clean the DataFrame and display the last 5 rows
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    print("Tesla Revenue DataFrame:")
    print(tesla_revenue.tail())
else:
    print("Table 'Tesla Quarterly Revenue' not found on the webpage.")


# In[39]:


import pandas as pd
from bs4 import BeautifulSoup
import requests

# Step 1: Download the webpage
gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_html_data = requests.get(gme_url).text

# Step 2: Parse HTML with BeautifulSoup
gme_soup = BeautifulSoup(gme_html_data, "html5lib")

# Step 3: Find the table with GameStop Quarterly Revenue
gme_tables = gme_soup.find_all('table')
gme_table_index = None

for index, table in enumerate(gme_tables):
    if "GameStop Quarterly Revenue" in str(table):
        gme_table_index = index
        break

# Check if the table is found
if gme_table_index is not None:
    # Step 4: Extract data from the table and create DataFrame
    gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

    for row in gme_tables[gme_table_index].tbody.find_all("tr"):
        col = row.find_all("td")
        if col:
            date = col[0].text
            revenue = col[1].text.replace("$", "").replace(",", "")
            gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

    # Display the last 5 rows of the DataFrame
    print("GameStop Revenue DataFrame:")
    print(gme_revenue.tail())
else:
    print("Table 'GameStop Quarterly Revenue' not found on the webpage.")


# In[41]:


import requests



# Use requests to download the webpage
response = requests.get(gme_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the HTML content as a variable named html_data
    html_data = response.text
    print("Webpage downloaded successfully.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


# In[42]:


# URL of the webpageheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(gme_url, headers=headers)
gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"


# In[43]:


import time

# Add a delay of 1 second between requests
time.sleep(1)


# In[44]:


import pandas as pd
from bs4 import BeautifulSoup
import requests

# Step 1: Download the webpage
gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_html_data = requests.get(gme_url).text

# Step 2: Parse HTML with BeautifulSoup
gme_soup = BeautifulSoup(gme_html_data, "html5lib")

# Step 3: Find the table with GameStop Quarterly Revenue
gme_tables = gme_soup.find_all('table')
gme_table_index = None

for index, table in enumerate(gme_tables):
    if "GameStop Quarterly Revenue" in str(table):
        gme_table_index = index
        break

# Check if the table is found
if gme_table_index is not None:
    # Step 4: Extract data from the table and create DataFrame
    gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

    for row in gme_tables[gme_table_index].tbody.find_all("tr"):
        col = row.find_all("td")
        if col:
            date = col[0].text
            revenue = col[1].text.replace("$", "").replace(",", "")
            gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

    # Display the last 5 rows of the DataFrame
    print("GameStop Revenue DataFrame:")
    print(gme_revenue.tail())
else:
    print("Table 'GameStop Quarterly Revenue' not found on the webpage.")


# In[46]:


#1
make_graph(tesla_data, tesla_revenue, 'Tesla')

#2
make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




