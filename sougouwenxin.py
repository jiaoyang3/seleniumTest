import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from PIL import Image
from io import BytesIO
from urllib import parse


class SouGouWeiXinTestCase(unittest.TestCase):

    # 每次先执行这个方法
    def setUp(self):
        pass

    # 每次最后执行这个方法
    def tearDown(self):
        pass

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Chrome(executable_path="/Users/wcc/Downloads/chromedriver")
        pass

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        pass

    def testAIndex(self):
        url = 'https://weixin.sogou.com/'
        self.browser.get(url)
        time.sleep(5)

        titles = self.browser.find_elements_by_xpath('//*[@id="topwords"]/li')

        # 搜索热词
        # data = {'type':2, 'ie':'utf8', 's_from':'hotnews'}
        # for title in titles:
        #     print(title.text)
        #
        #     hot_url = title.find_element_by_xpath('//a').get_attribute('href')
        #     print(hot_url)
        #
        #     data['query'] = title.text
        #     new_url = url + 'weixin?' + parse.urlencode(data)
        #     print(new_url)

        # 热门
        articles = self.browser.find_elements_by_xpath('//*[@id="pc_0_0"]/li')
        j = 1

        list_url = []
        for article in articles:
            img_url = article.find_element_by_tag_name('img').get_attribute('src')
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            img.save('/Users/jiao/python/webtest/img/' + str(time.time()) + '.jpeg')

            url = article.find_element_by_tag_name('a').get_attribute('href')

            print("第%d篇文章" % j)
            print('图片：' + img_url)
            print('网址：' + url)
            print('标题：' + article.find_element_by_tag_name('h3').text)
            print('概要：' + article.find_element_by_tag_name('p').text)

            j += 1

            obj = {
                'url': url,
                'id': j
            }
            list_url.append(obj)

        print(list_url)

        for url in list_url:
            print(url)
            url = url['url']
            self.browser.get(url)
            title = self.browser.title
            print(title)


if __name__ == '__main__':
    unittest.main(verbosity=2)