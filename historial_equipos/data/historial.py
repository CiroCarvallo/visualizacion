#scrapping historial de equipos argentinos
import urllib.request
from bs4 import BeautifulSoup
import csv

raiz_url="http://www.promiedos.com.ar/historialpartidos.php?equipo="
equipos=["Aldosivi","All%20Boys","Argentinos","Arsenal",'Atlanta','Atl%20Rafaela','Atl%20Tucuman','Banfield','Belgrano',
'Boca%20Juniors','Chacarita','Colon','Crucero%20(M)','Def%20y%20Justicia','Estudiantes20%(LP)','Ferro','Gimnasia%20(LP)','Gimnasia%20(J)',
'Godoy%20Cruz','Huracan','Independiente','Instituto','Lanus','Newells','Nueva%20Chicago','Olimpo','Platense','Quilmes',
'Racing%20Club','River%20Plate','Rosario%20Central','San%20Lorenzo','San%20Martin%20(Sj)','San%20Martin%20(T)','Sarmiento%20(J)','Temperley',
'Talleres%20(C)','Tigre','Union','Velez']

# devuelve la pagina como un html
def get_hist_equipo(equipo):
	#page=urllib.request.urlopen(raiz_url+equipos[num_equipo])
	page=urllib.request.urlopen("http://www.promiedos.com.ar/historialpartidos.php?equipo="+equipo)
	return page

# parsear el html
def parse_html(page):
	soup=BeautifulSoup(page,'html.parser')
	return soup

def crear_csv_historial(equipo):
	#crea csv con historial para n-esimo equipo de equipos
	page=get_hist_equipo(equipo)
	page_soup=parse_html(page)
	tabla=page_soup.table.find_all('tr')
	header=['equipo','jugados','ganados','perdidos','empatados','diferencia','gf','gc']
	with open('historial_'+equipo,'w',newline='') as f:
		writer=csv.writer(f)
		writer.writerow(header)
		for row in tabla:
			columnas=row.find_all('td')
			if(len(columnas)>0):
				valores=[columnas[0].get_text()[4:]]
				for columna in columnas[1:-1]: # el ultimo es ' '
					valores.append(columna.get_text())
				print(valores)
				writer.writerow(valores)

#for equipo in equipos:
#	crear_csv_historial(equipo)
crear_csv_historial('Sarmiento%20(J)')

