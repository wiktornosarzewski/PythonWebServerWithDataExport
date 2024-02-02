from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        result = request.form.to_dict()
        with open('result.txt', 'w') as f:
            f.write(str(result))
        return 'Formularz wysłany! Wprowadzone dane to: {}. <br><br><form method="get" action="/"><input type="submit" value="Wypełnij kolejną"></form>'.format(result)
    return '''
        <form method="post">
            <label>Imię:</label>
            <input type="text" name="first_name"><br>
            <label>Nazwisko:</label>
            <input type="text" name="last_name"><br>
            <label>Email:</label>
            <input type="email" name="email"><br>
            <input type="submit" value="Wyślij">
        </form>
    '''

if __name__ == '__main__':
    app.run()
