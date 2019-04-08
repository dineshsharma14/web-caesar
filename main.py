from flask import Flask,request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>

    <body>
    <form action="" method="post">
        <label>
        Rotate By:
        <input type="text" name="rot" value="0"/> <!--default value = 0-->
        </label>
        <textarea name="text"></textarea>
        <input type="submit"/>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot_num = int(request.form['rot'])
    text_entered = request.form['text']
    return "<h1>" + rotate_string(text_entered,rot_num) + "</h1>"

app.run()