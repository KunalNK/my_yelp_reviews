import requests
from bs4 import BeautifulSoup
import csv

pages=[0,20,40,60,80,100]

# Open writer with name
file_name = "yelp_reviews_new.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

 # write a new row as a header
f.writerow(['Name', 'Location', 'Reviews'])

for page in pages:
    source= requests.get('https://www.yelp.com/biz/bar-karaoke-lounge-toronto?start={}'.format(page))


    print(page)
    soup = BeautifulSoup(source.text, 'html.parser')
    #print(soup)
    reviews=soup.find(class_="lemon--div__373c0__1mboc spinner-container__373c0__N6Hff border-color--default__373c0__3-ifU")

    my_review=reviews.find_all(class_="lemon--li__373c0__1r9wz margin-b3__373c0__q1DuY padding-b3__373c0__342DA border--bottom__373c0__3qNtD border-color--default__373c0__3-ifU")
    print(len(my_review))

    

    for reviews in my_review:

        name=reviews.find(class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE").get_text()
        print(name)
        location=reviews.find(class_="lemon--div__373c0__1mboc responsive-hidden-small__373c0__2vDff border-color--default__373c0__3-ifU").get_text()
        print(location)
        people_reviews=reviews.find(class_="lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-").get_text()
        print(people_reviews)

        print('name', name)
        print('location', location)
        print('people_reviews', people_reviews)

        print('Writing rows')
        # add the information as a row into the csv table
        f.writerow([name, location, people_reviews])