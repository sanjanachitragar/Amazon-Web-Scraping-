import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Entry, StringVar

def fetch_product_name():
    url = url_entry.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find(id="productTitle")

            if title_tag:
                product_name.set(title_tag.get_text(strip=True))
            else:
                product_name.set('Product name not found')
    except Exception as e:
        product_name.set("An error occured")

#create a window
root = Tk()
root.title("Amazon Product Name Fetcher")

product_name = StringVar()
product_name.set("Enter URL and click Fetch")

Label(root, text="Enter Amazon Product URL: ").pack()
url_entry = Entry(root, width=60)
url_entry.pack()

fetch_button = Button(root, text="Fetch", command=fetch_product_name)
fetch_button.pack()

Label(root, textvariable=product_name).pack()

root.mainloop()