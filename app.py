from flask import *
import mysql.connector

app = Flask(__name__)


db_config={
    "host":"localhost",
    "user":"root",
    "password":"5028",
    "database":"scraped_data"
}

@app.route("/")
def home():
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM countries;")
            show = cursor.fetchall()
        except mysql.connector.Error as err:
            flash(f"Database Error: {err}", "danger")
            show = []
        finally:
            cursor.close()
            connection.close()
        return render_template('countries.html',val=show)


if __name__ == '__main__':
    app.run(debug=True)
