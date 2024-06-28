import connexion
from flask import redirect

app = connexion.FlaskApp(__name__, specification_dir='.')
app.add_api('meteoapi.yaml', arguments={'title': 'MeteoAPI'})

@app.route('/')  
def home():  
    return redirect('/ui')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

