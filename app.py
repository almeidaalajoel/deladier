from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/california')
def california():
    return render_template('california.html')
    
@app.route('/southwest')
def southwest():
    return render_template('southwest.html')

@app.route('/tuscany')
def tuscany():
    return render_template('tuscany.html')

@app.route('/tour')
def tour():
    return render_template('tour.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/flight')
def flight():
    return render_template('flight.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/galleries')
def galleries():
    return render_template('galleries.html')

if __name__ == '__main__':
    app.run(debug=True)
