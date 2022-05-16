import pandas as pd 
import json

f = open('markup_data.json')
markup_data = json.load(f)

# import most recent csv data from GCP bucket

df = pd.read_csv('test_productData_2.csv')
df["IS_ADJUSTED"] = False

for adjustment in markup_data:
    for index, row in df.iterrows():
        price = df.at[index, 'PRICE']
        isChanged = df.at[index, 'IS_ADJUSTED']
        if ((adjustment['lower_bound'] < price < adjustment['higher_bound']) and (isChanged == False)):
            df.at[index, 'PRICE'] = price + round(price * adjustment['markup_percent'])
            df.at[index, 'IS_ADJUSTED'] = True
    percentage = "{:.0%}".format(adjustment['markup_percent'])
    print(f"{percentage} markup products completed!")

print("Finished. Now writing as CSV!")
df.drop(columns='IS_ADJUSTED')
df.to_csv('price_adjusted_products.csv', index=False)
print("Process is now completed!")