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

import requests
from bs4 import BeautifulSoup, Comment
import spacy

nlp = spacy.load("en_core_web_sm") 

url1 = 'https://en.wikipedia.org/wiki/Natural_language_processing'
url2 = 'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html'
url3 = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
url4 = 'https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1'
url5 = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'

sites = [url1, url2, url3, url4, url5]

textos = []

i = 0
while i < 5:
  texto = []
  textos.append(texto)
  i += 1

i = 0;
while i < 5:                     
  html = requests.get(sites[i]).text                     
  soup = BeautifulSoup(html, 'html.parser')     
  for j in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
    j.decompose()
    texts = ' '.join(soup.stripped_strings)                      
  page = nlp(texts)

  for x in page.sents:
      textos[i].append(x.text)

  i += 1;

vocabulario = []

for lista in textos:
  for sentenca in lista:
    list = sentenca.split(' ')
    for j in list:
      j = re.split('[,()]',j)
      for i in j:
        no = True
        for x in vocabulario:
          if i.lower() == x:
            no = False
            break
        if no and i != '':
          vocabulario.append(i.lower())

print(vocabulario)

bagOfWords = []

for sentencas in corpus:
    for sentenca in sentencas:
      vetor = [0] * len(vocabulario)
      for palavra in sentenca.split(' '):
          if palavra in vocabulario:
            vetor[vocabulario.index(palavra)] += 1
      bagOfWords.append(vetor)

for x in bagOfWords:
  print(x)
