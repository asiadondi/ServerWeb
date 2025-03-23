from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 4 endpoint: '/','/form','/urlpar/<par>','/reqpar' in cui viene fatta una richiesta HTTP
@app.route('/',methods=['GET']) # la funzione che c'è dopo è associata all'url allora quello che si deve fare è che se lo stiamo
# chiedendo in modalità GET allora si esegue la funzione main, altrimenti quando arriva al server
# una richiesta all'url esegui la funzione form e così via
def main():
    #return 'ciao marco'
    user = {'username': 'Marco'}
    list = [1,2,3,4,5]
    return render_template('index.html', title='Home', user=user, list=list)

# http form
@app.route('/form')
def root():
    return redirect(url_for('static', filename='login.html')) # dice al browser di prendere il file nella cartella static, 
    # ci si ridireziona al file login.html che visualizza una semplice form html


# parameters in the url
@app.route('/urlpar/<par>',methods=['GET'])
def urlpar(par):
    user = {'username': par}
    list = [1, 2, 3, 4, 5]
    return render_template('index.html', title='Home', user=user, list=list)

# http get parameters
@app.route('/reqpar',methods=['GET','POST'])
def getpar():
    print(request.values)
    user = {'username': request.values['name']}
    return render_template('index.html', title='Home', user=user, list=[])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # Flask sta eseguendo local host e rende l'applicazione 
    # accessibile dall'ip pubblico
    # 155.185 sono gli indirizzi UNIMORE


