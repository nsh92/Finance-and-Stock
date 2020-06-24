from flask import Flask, render_template, request
import webbrowser
from urllib import parse

app = Flask(__name__)

url = "http://dart.fss.or.kr/dsab002/search.ax?"
#webbrowser.open(url)

@app.route('/')
def index():
    return render_template("/app/search.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        report = request.form['report']
        kan = request.form['kan']
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        stock = request.form['stock']
        goto = url + "reportName=" + parse.quote(report) + "&&maxResults=" + kan + "&&startDate=" + startdate + "&&endDate=" + enddate + "&textCrpNm=" + parse.quote(stock)
        print(report)
        print(kan)
        print(startdate)
        print(enddate)
        print(stock)
        print(goto)

        return webbrowser.open(goto) and render_template("/app/search.html")

if __name__ == "__main__":
    app.run()




