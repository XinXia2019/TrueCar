import requests
import json
import csv
import time as time
from bs4 import BeautifulSoup

def flatten_dict(dd, separator ='_', prefix =''): 
    return { prefix + separator + k if prefix else k : v 
             for kk, vv in dd.items() 
             for k, v in flatten_dict(vv, separator, kk).items() 
             } if isinstance(dd, dict) else { prefix : dd } 


data_year = list(range(1997,2021,1)[::-1])

data_page = []
print("Get page numbers..")
for year in data_year:
    url = f'https://www.truecar.com/used-cars-for-sale/listings/year-{year}/'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    page = soup.find_all(class_ = "page-link")[-3].get_text()
    data_page.append(page)

print("Start scraping..")

data_all =[]
for idx in range(len(data_year)):
    year = data_year[idx]
    total_page = int(data_page[idx])
    
    print("-" * 100)
    print(f"Year {year}")
    time_start = time.time()
    

    for page in range(1,total_page+1,1):
        try:
            url = f"https://www.truecar.com/abp/api/vehicles/used/listings?new_or_used=u&per_page=30&postal_code=&year_high={year}&year_low={year}&page={page}"
            res = requests.get(url)
            json_file = json.loads(res.content)['listings']
            
            for file in json_file:
                data_all.append(flatten_dict(file))
                
        except Exception as e:
            print("!"*100)
            print(e)
            print("!"*100)

    print(f"Finished in {time.time() - time_start : .2f} seconds")
    
print("Saving to csv file...")
df = pd.DataFrame(data_all)
df.to_csv("true_car_9720.csv",index = False)
print("Done")