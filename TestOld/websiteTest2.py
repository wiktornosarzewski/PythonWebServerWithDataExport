from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        return render_template_string('''
            <html>
                <head>
                    <title>Przykładowy formularz</title>
                </head>
                <body>
                    <form action="/" method="post">
                        <label for="text">Wpisz tekst:</label><br>
                        <input type="text" id="text" name="text"><br>
                        <label for="button">Przycisk:</label><br>
                        <button type="submit" id="button" name="button">Wyślij</button>
                    </form>
                    <p>Wpisany tekst: {{ text }}</p>
                </body>
            </html>
        ''', text=text)
    else:
        return render_template_string('''
            <html>
                <head>
                    <title>Przykładowy formularz</title>
                </head>
                <body>
                    <form action="/" method="post">
                        <label for="text">Wpisz tekst:</label><br>
                        <input type="text" id="text" name="text"><br>
                        <label for="button">Przycisk:</label><br>
                        <button type="submit" id="button" name="button">Wyślij</button>
                    </form>
                </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)
