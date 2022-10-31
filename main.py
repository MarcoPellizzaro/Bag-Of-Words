#Marco Vinícius Costódio Pellizzaro

'''
Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e 
imprimir esta matriz na tela. Para tanto: 
a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, 
onde cada item será uma das palavras da sentença. 
b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores, 
onde cada item será um lexema.  
c) Este único corpus será usado para gerar o vocabulário. 
d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da 
técnica bag of Words em todo o corpus.  
'''

from bs4 import BeautifulSoup
import requests
import re

url = 'https://en.wikipedia.org/wiki/Parsing'
res1 = requests.get(url)
url = 'https://academic.oup.com/jamia/article/18/5/544/829676?login=false'
res2 = requests.get(url)
url = 'https://en.wikipedia.org/wiki/Natural_language_processing'
res3 = requests.get(url)
url = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
res4 = requests.get(url)
url = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'
res5 = requests.get(url)
html_pages = {res1.text, res2.text, res3.text, res4.text, res5.text}

corpus = []
vocabulario1 = []

for html_page in html_pages:
  soup = BeautifulSoup(html_page, 'html.parser')
  linhas = re.split('[;.!?\n\t]',soup.get_text())
  corpus.append(linhas)

for lista in corpus:
  for sentenca in lista:
    list = sentenca.split(' ')
    for j in list:
      j = re.split('[,()]',j)
      for i in j:
        no = True
        for x in vocabulario1:
          if i.lower() == x[0]:
            x[1] += 1
            no = False
            break
        if no and i != '':
          vocabulario1.append([i.lower(), 1])

print(vocabulario1)
