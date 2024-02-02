from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        result = request.form
        return str(result)
    return '''
        <form method="post">
            <label>Imię:</label>
            <input type="text" name="first_name"><br>
            <label>Nazwisko:</label>
            <input type="text" name="last_name"><br>
            <label>Email:</label>
            <input type="text" name="email"><br>
            <input type="submit" value="Wyślij">
        </form>
    '''

if __name__ == '__main__':
    app.run()
