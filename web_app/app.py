from flask import Flask, request, render_template
from telcom import telecom_fnc
selected_student=[20,10,40,60,70]
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
 
         return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def multiply():
    #if request.method == 'POST':
        int_features3 = [int(x) for x in request.form.values()]
        print (int_features3)
        result=telecom_fnc(int_features3)
        print (result)
        return render_template('result.html', result=result)
  #  return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)