import requests
from lxml import etree

url = "https://browser.geekbench.com/v5/compute/search?utf8=✓&q=AMD+Radeon+Pro+5300M+"
ua_headers = {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
html_codes = requests.get(url=url, headers=ua_headers).text
tree = etree.HTML(html_codes)
for x in range(1,26):
    contents = tree.xpath('//*[@id="wrap"]/div/div/div/div[2]/div[%s]/div/div/div[5]/span[2]' % str(x))
    print(contents)
