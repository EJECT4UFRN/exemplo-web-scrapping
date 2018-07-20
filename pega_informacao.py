# Eae programadores Ejectinianos, como estão?
# Hoje, decidi comentar sobre um assunto muito irado sobre programação, o famigerado 'web scraping'
# Esse site fala direitinho o que é: https://blogbrasil.westcon.com/o-que-e-web-scraping
# Sério, leiam antes de se aventurar nesse código. É importante
# Decidi criar esse exemplo para mostrar mais uma técnica de programação que as vezes
# Algum cliente quer implementar (É mais díficil mas pode acontecer, vai que)
# Já realizamos projetos precisando disso (Famigerado FBC)
# Nesse exemplo, eu varro o blog da EJECT e capturo as informações sobre suas postagens
# Recomendo ver outros dois links para as coisas fazerem sentido:
# Biblioteca Python BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Biblioteca Python urllib: https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# Sem mais delongas, vamos analisar o código
# (Último aviso, prometo. Rodem esse código para ver a mágica acontecendo)



from bs4 import BeautifulSoup # Biblioteca feita pela comunidade Python para análise de HTML
from urllib.request import urlopen # Biblioteca do próprio Python para fazer requisições de páginas web

html = urlopen('http://ejectufrn.com.br/blog/') # Realiza a requisição da página da EJECT
bsObj = BeautifulSoup(html.read(), 'html.parser') # Coloca tudo o que veio do servidor para um objeto que seja fácil de trabalhar
postagens_links = bsObj.find('ul', {'id': 'postagens'}).findAll('a') # Pega todos os links das postagens da página

for i in postagens_links: # Estou percorrendo os links
	link_da_postagem = i['href'] # Peguei o link

	print('Fazendo requisição da página: http://ejectufrn.com.br' + link_da_postagem)

	html_da_postagem = urlopen('http://ejectufrn.com.br' + link_da_postagem) # Vou até a página da postagem
	pagina_da_postagem = BeautifulSoup(html_da_postagem.read(), 'html.parser') # Coloco o que veio do servidor da página da postagem num lugar que seja fácil de trabalhar

	titulo = pagina_da_postagem.find('header', {'animated fadeIn'}).find('h1') # Pego o título da página
	texto = pagina_da_postagem.find('footer', {'class': 'textopostagem'}) # Pego o texto da postagem

	# Escrevo isso dentro de um arquivo
	with open(titulo.get_text() + '.html', 'w') as f:
		f.write(str(pagina_da_postagem.html))