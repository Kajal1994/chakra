from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calibrate')
def calibrate():
    intention = request.args.get('intention', '')
    mood = request.args.get('mood', '')
    return render_template('calibrate.html', intention=intention, mood=mood)

if __name__ == '__main__':
    app.run(debug=True) 