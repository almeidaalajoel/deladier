from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_view_counter import ViewCounter

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    page = Page.query.filter_by(title="/").first()
    if not page:
        page = Page(title = "/", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('index.html', count= page.count)

@app.route('/california')
def california():
    page = Page.query.filter_by(title="/california").first()
    if not page:
        page = Page(title = "/california", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('california.html', count= page.count)
    
@app.route('/southwest')
def southwest():
    page = Page.query.filter_by(title="/southwest").first()
    if not page:
        page = Page(title = "/southwest", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('southwest.html', count= page.count)

@app.route('/tuscany')
def tuscany():
    page = Page.query.filter_by(title="/tuscany").first()
    if not page:
        page = Page(title = "/tuscany", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('tuscany.html', count= page.count)

@app.route('/tour')
def tour():
    page = Page.query.filter_by(title="/tour").first()
    if not page:
        page = Page(title = "/tour", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('tour.html', count= page.count)

@app.route('/events')
def events():
    page = Page.query.filter_by(title="/events").first()
    if not page:
        page = Page(title = "/events", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('events.html', count= page.count)

@app.route('/flight')
def flight():
    page = Page.query.filter_by(title="/flight").first()
    if not page:
        page = Page(title = "/flight", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('flight.html', count= page.count)

@app.route('/contact')
def contact():
    page = Page.query.filter_by(title="/contact").first()
    if not page:
        page = Page(title = "/contact", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('contact.html', count= page.count)

@app.route('/galleries')
def galleries():
    page = Page.query.filter_by(title="/galleries").first()
    if not page:
        page = Page(title = "/galleries", count=0)
        db.session.add(page)
    page.count+=1
    db.session.commit()
    return render_template('galleries.html', count= page.count)

if __name__ == '__main__':
    app.run(debug=True)
