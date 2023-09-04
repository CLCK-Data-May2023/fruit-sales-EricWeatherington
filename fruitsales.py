# add your code here

import pandas

fruit_sales = pandas.DataFrame([[35, 21], [41, 34]], columns = ['Apples', 'Bananas'], index = ['2017', '2018'])

fruit_sales.to_csv('fruit.csv')
