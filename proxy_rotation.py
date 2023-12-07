import requests

with open("valid_proxies.txt","r") as f: #takes input from the valid proxies file
        proxies = f.read().split("\n")  #stores the conten from the file into list called proxies 

sites_to_check = ["http://books.toscrape.com/index.html",
                  "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
                  "http://books.toscrape.com/catalogue/category/books/thriller_37/index>"]
#contains the url of the websites to be checked

counter = 0 #to keep track of list of proxies

for site in sites_to_check:
        try:
                print(f"Using the Proxy: {proxies[counter]}")
                res = requests.get(site, proxies = {"http": proxies[counter], "https": proxies[counter]})

                print(res.status_code)
                print(res.text) #prints the html code

        except:
                print("Failed")
        finally:
                counter = counter+1