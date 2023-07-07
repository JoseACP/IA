from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_data():
    # Realiza una solicitud HTTP a la página web de origen
    response = requests.get('https://colab.research.google.com/drive/1OMVWX57KJR7wuENpBs0rVhCVoZ8sCL-s#scrollTo=UKPpO4siDWGi')
    
    # Extrae los datos utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Aquí puedes usar las funciones de BeautifulSoup para extraer los datos específicos que deseas
    
    # Por ejemplo, supongamos que quieres extraer el título de la página
    title = soup.title.string
    
    # Renderiza la plantilla HTML y pasa los datos extraídos
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run()
