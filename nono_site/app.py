from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static/site.css')


# Define a route to render the first HTML page
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Define a route to render the second HTML page
@app.route('/1')
def page2():
    return render_template('pets.html')

# Define a route to render the third HTML page
@app.route('/2')
def page3():
    return render_template('pic_try.html')

if __name__ == '__main__':
    app.run(debug=True)
