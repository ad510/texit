from flask import Flask
from tex import renderTex;
from graph import renderGraph;
app = Flask(__name__)

@app.route('/tex/<query>')
def tex(query):
	return renderTex(query)

@app.route('/graph/<query>')
def graph(query):
	return renderGraph(query);

#Pointless comment

if __name__=="__main__":
	app.run();