from flask import Flask, render_template,url_for, jsonify, request
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'lcbiusr'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bIUsR#231'
app.config['MYSQL_DATABASE_DB'] = 'newdatasets'
app.config['MYSQL_DATABASE_HOST'] = '192.168.1.208'
mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def siteConfig():
    sql = "SELECT * FROM newdatasets.country "
    cursor.execute(sql)
    results = cursor.fetchall()
    sql1 = "SELECT * FROM newdatasets.state "
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    return render_template('siteConfig.html',results=results,results1=results1)


@app.route('/processfiles')
def processfiles():
    return render_template('ProcessFiles.html')


if __name__ == '__main__':
    app.run(debug=True)
