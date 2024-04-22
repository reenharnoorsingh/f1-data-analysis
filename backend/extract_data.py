import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

source = urllib.request.urlopen('https://www.formula1.com/en/results.html/1990/drivers.html').read()
soup = BeautifulSoup(source, 'html.parser')  # Use 'html.parser' as the parser
table = soup.find_all('table')[0]
df = pd.read_html(str(table), flavor='bs4', header=[0])[0]
df.drop(["Unnamed: 0", "Unnamed: 6"], axis=1, inplace=True)
df.head()
df.plot.bar(x="Driver", y="PTS");
