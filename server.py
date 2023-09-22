from flask import Flask , render_template , send_from_directory
import os 
app = Flask(__name__) 

@app.route("/") 
def hello_world():
    return(render_template("./index.html")) 

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name) 

@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'icon.ico')
