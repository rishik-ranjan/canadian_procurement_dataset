#import os
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

app.vars = {}

app.currentplot=0

@app.route('/index',methods=['GET','POST'])
def index():
	if request.method == 'GET' and app.currentplot<6:
		if app.currentplot==0:
			return render_template('p1.html')
		if app.currentplot==1:
			return render_template('p2.html')
		if app.currentplot==2:
			return render_template('p3.html')
		if app.currentplot==3:
			return render_template('p4.html')
		if app.currentplot==4:
			return render_template('p5.html')
		if app.currentplot==5:
			return render_template('p6.html')
	else:
		print app.currentplot
		return redirect('/main')

@app.route('/main')
def main():
    if app.currentplot==6: 
		app.currentpot = 0
		return render_template('end.html')
    return redirect('/next')
	
@app.route('/next',methods=['POST'])
def next():  
    app.currentplot += 1
    return redirect('/index')
	
if __name__ == "__main__":
    app.run(debug=True)    

