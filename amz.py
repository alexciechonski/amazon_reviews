from requests_html import HTMLSession
import json
import os

class Reviews:
    def __init__(self, asin) -> None:
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        self.url = f'https://www.amazon.com/Luminara-Realistic-Artificial-Classic-Pillar/product-reviews/B097T7XM7H/ref=cm_cr_othr_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')

    def parse(self,reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]',first=True).text
            rating = review.find('i[data-hook=review-star-rating] span',first=True).text
            body = review.find('span[data-hook=review-body] span',first=True).text.replace('\n','').strip()

            data ={
                'title':title,
                'rating':rating,
                'body':body[:100]
            }

            total.append(data)
        return total

    def save(self,results):
        with open(self.asin + 'reviews.json','w') as f:
            json.dump(results, f)
            print(os.path.abspath(self.asin + 'reviews.json'))



if __name__=='__main__':
    amz = Reviews('B097T7XM7H')  #asin
    results = []
    for x in range(1,5):
        reviews = amz.pagination(x)
        if reviews is not False:
            results.append(amz.parse(reviews))
        else:
            print('No more pages')
            break
print(results)
amz.save(results)









