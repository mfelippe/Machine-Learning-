from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input("Digite a pesquisa:")

driver = webdriver.Chrome()
driver.get("https:www.google.com")

#pesquisa de informação
campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

#mostrando a quantidade de resultados encontrados
resultados = driver.find_element_by_xpath("//div[@id='result-stats']")
print(resultados.text)

#pegando a quantidade de resultados
numero_resultados = float(resultados.text.split('Aproximadamente ')[1].split(' resultados')[0].replace(".",""))
maximo_paginas = numero_resultados/10
pagina_limite = int(input ("%s páginas encontradas, até que páina desejar buscar ?"% (maximo_paginas)))

#proxima pagina
url_pagina=driver.find_element_by_xpath("//a[@aria-label='Page 2']").get_attribute("href")

pagina_atual = 0
start = 10
lista_resultados =[]

while pagina_atual <= pagina_limite :

	if pagina_atual > 0:
		url_pagina = url_pagina.replace("start=%s" % start,"start=%s" % (start+10))
		start += 10
		driver.get(url_pagina)
	elif pagina_atual ==1:
		driver.get(url_pagina)
	pagina_atual+= 1
		

	#pegando os dados pesquisados

	divs = driver.find_elements_by_xpath("//div[@class='g']")

	#para cada resultado encontrado pega os titulos e os links
	for div in divs:
		 nome = div.find_element_by_tag_name("span").text
		 link = div.find_element_by_tag_name("a").get_attribute("href")

		 resultado_pesquisa = "%s,%s" %(nome, link)
		 print(resultado_pesquisa)

		 lista_resultados.append(resultado_pesquisa)

#salvando os resultados em um arquivo
with open("resultados.txt", "w") as arquivo:
	for resul in lista_resultados:
		arquivo.write("%s\n" % resul)
	arquivo.close()

print("%s resultados encontrados e salvos" % len(lista_resultados))


