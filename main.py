from flask import Flask, render_template
from mreadings import get_reading_list

app = Flask(__name__)

@app.route('/')
def base():
    mreadings = get_reading_list().split("\n")
    return render_template("index.html.j2", mreadings=mreadings)

if __name__ == "__main__":
    app.run()
