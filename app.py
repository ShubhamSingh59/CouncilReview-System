from flask import Flask, render_template, request
import os
import gspread
#from google.auth.credentials import ServiceAccountCredentials
from flask_mysqldb import MySQL
import config

# Create the Flask application instance
app = Flask(__name__)
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_DB'] = config.MYSQL_DB

def set_mysql_credentials(user, password):
    app.config['MYSQL_USER'] = user
    app.config['MYSQL_PASSWORD'] = password


mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('Home.html')

@app.route('/login')
def Login():
    return render_template('Login.html')

@app.route('/signin')
def Signin():
    return render_template('Signin.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/cult')
def cult():
    return render_template('cult.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/welfare')
def welfare():
    return render_template('welfare.html')

@app.route('/acad')
def acad():
    return render_template('acad.html')

@app.route('/pdc')
def pdc():
    return render_template('pdc.html')
@app.route('/irp')
def irp():
    return render_template('irp.html')

@app.route('/pdc_submit', methods=['POST'])
def pdc_submit():
    # Get form data
    secyrating = request.form['secyrating']
    council_rating = request.form['councilRating']
    feedback = request.form['feedback']

    # Store data in MySQL database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO pdc_council (Secretary_rating, Council_rating, Feedback) VALUES (%s, %s, %s)", (secyrating, council_rating, feedback))
    mysql.connection.commit()
    cur.close()

    return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'

@app.route('/tech_submit', methods=['POST'])
def tech_submit():
     if request.method == 'POST':
        # Get form data
        secretary_rating = request.form['technicalSecRating']
        council_rating = request.form['technicalCouncilRating']
        metis_rating = request.form['metisRating']
        mean_mechanics_rating = request.form['meanMechanicsRating']
        digis_rating = request.form['digisRating']
        odyssey_rating = request.form['odysseyRating']
        anveshanam_rating = request.form['AnveshanamRating']
        grasp_rating = request.form['graspRating']
        ml_group_rating = request.form['mlGroupRating']
        feedback = request.form['feedback']

        # Insert into MySQL
        cur = mysql.connection.cursor()
        sql = "INSERT INTO tech_council (Secretary_rating, Council_rating, Metis_rating, Mean_mechanics_rating, Digis_rating, Odyssey_rating, Anveshanam_rating, Grasp_rating, ML_group_rating, Feedback) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (secretary_rating, council_rating, metis_rating, mean_mechanics_rating, digis_rating, odyssey_rating, anveshanam_rating, grasp_rating, ml_group_rating, feedback)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'
     
@app.route('/cult_submit', methods=['POST'])
def cult_submit():
    if request.method == 'POST':
        # Get form data
        cultral_sec_rating = request.form['cultralSecRating']
        cultral_council_rating = request.form['cultralCouncilRating']
        sargam_rating = request.form['sargamRating']
        step_up_rating = request.form['stepUpRating']
        literary_rating = request.form['literaryRating']
        palette_rating = request.form['paletteRating']
        pixels_rating = request.form['pixelsRating']
        abhinaya_rating = request.form['abhinayaRating']
        vinteo_rating = request.form['vinteoRating']
        cinematheque_rating = request.form['cinemathequeRating']
        orenda_rating = request.form['orendaRating']
        quizzing_society_rating = request.form['quizzingSocietyRating']
        awaam_rating = request.form['awaamRating']
        feedback = request.form['feedback']

        # Insert into MySQL
        cur = mysql.connection.cursor()
        sql = "INSERT INTO cult_council (Cultural_Secretary_rating, Cultural_Council_rating, Sargam_rating, Step_up_rating, Literary_Society_rating, Palette_rating, Pixels_rating, Abhinaya_rating, Vinteo_rating, Cinematheque_rating, Orenda_rating, Quizzing_Society_rating, Awaam_rating, Feedback) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (cultral_sec_rating, cultral_council_rating, sargam_rating, step_up_rating, literary_rating, palette_rating, pixels_rating, abhinaya_rating, vinteo_rating, cinematheque_rating, orenda_rating, quizzing_society_rating, awaam_rating, feedback)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'
    
@app.route('/sports_submit', methods=['POST'])
def sports_submit():
    if request.method == 'POST':
        # Get form data
        sports_sec_rating = request.form['sportsSecRating']
        sports_council_rating = request.form['sportsCouncilRating']
        feedback = request.form['feedback']

        # Insert into MySQL
        cur = mysql.connection.cursor()
        sql = "INSERT INTO sports_council(Sports_Secretary_rating, Sports_Council_rating, Feedback) VALUES (%s, %s, %s)"
        val = (sports_sec_rating, sports_council_rating, feedback)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()

        return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'
    
@app.route('/welfare_submit', methods=['POST'])
def welfare_submit():
    if request.method == 'POST':
        # Get form data
        welfare_sec_rating = request.form['welfareSecRating']
        welfare_council_rating = request.form['welfareCouncilRating']
        feedback = request.form['feedback']

        # Insert into MySQL
        cur = mysql.connection.cursor()
        sql = "INSERT INTO welfare_council(Welfare_Secretary_rating, Welfare_Council_rating, Feedback) VALUES (%s, %s, %s)"
        val = (welfare_sec_rating, welfare_council_rating, feedback)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()

        return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'

@app.route('/acad_submit', methods=['POST'])
def acad_submit():
    if request.method == 'POST':
        # Get form data
        acad_sec_rating = request.form['acadSecRating']
        acad_council_rating = request.form['acadCouncilRating']
        feedback = request.form['feedback']

        # Insert into MySQL
        cur = mysql.connection.cursor()
        sql = "INSERT INTO acad_council(Acadmic_Secretary_rating, Acadmic_Council_rating, Feedback) VALUES (%s, %s, %s)"
        val = (acad_sec_rating, acad_council_rating, feedback)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()

        return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'

@app.route('/irp_submit', methods=['POST'])
def irp_submit():
    if request.method == 'POST':
        # Get form data
        irp_sec_rating = request.form['irpSecRating']
        irp_council_rating = request.form['irpCouncilRating']
        feedback = request.form['feedback']

        # Insert into MySQL
        cur = mysql.connection.cursor()
        sql = "INSERT INTO irp_council(IRP_Secretary_rating, IRP_Council_rating, Feedback) VALUES (%s, %s, %s)"
        val = (irp_sec_rating, irp_council_rating, feedback)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()

        return '<script>alert("Data submitted successfully"); window.location.href = "/";</script>'

@app.route('/api/signin', methods=['POST'])
def create_user():
    try:
        app.config['MYSQL_USER'] = config.MYSQL_USER
        app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
        
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("CREATE USER %s@'localhost' IDENTIFIED BY %s", (email, password))
      
        cur.execute("GRANT SELECT ON *.* TO %s@'localhost'",(email,))
        
        mysql.connection.commit()
        cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
       
        mysql.connection.commit() 
        cur.close()
        
        return '<script>alert("Signin successfull"); window.location.href = "/";</script>'
    except Exception as e:
        return '<script>alert("error in sigin process"); window.location.href = "/signin";</script>'

@app.route('/api/login', methods=['POST'])
def newLogin():
    try:
        #set_mysql_credentials('root', 'Stromer/2003')
        email = request.form['email']
        password = request.form['password']
        set_mysql_credentials(email, password)
        cur = mysql.connection.cursor()
        # Check if the user exists in the users table
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        mysql.connection.commit() 
        user_data = cur.fetchone()
        print(user_data)
        if user_data:
            # Set MySQL credential
                cur = mysql.connection.cursor()
            # Execute "SHOW TABLES" query
            # cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'sports_management' AND table_name != 'Users'")
                mysql.connection.commit() 
            # tables = cur.fetchall()
            #print(tables)
                cur.close()
                return '<script>alert("login successfull"); window.location.href = "/";</script>'
        else:
                return '<script>alert("invalid credential"); window.location.href = "/login";</script>'
        
    except Exception as e:
        return '<script>alert("there is some error"); window.location.href = "/login";</script>'

if __name__ == '__main__':
    app.run(debug=True)
