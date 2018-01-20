url = 'https://dinbendon.net/do/idine?shop=209534'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
print(soup)