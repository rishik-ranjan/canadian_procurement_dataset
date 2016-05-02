from flask import Flask,render_template,request,redirect
app = Flask(__name__)

app.vars = {}

app.plotnumber=7
app.divs = {'p2': u'\n<div class="plotdiv" id="18c305a4-c7e9-4ac8-adbc-7c69376a62b6"></div>', 'p3': u'\n<div class="plotdiv" id="14f28914-331b-446a-9ec0-3e406047bca2"></div>', 'p1': u'\n<div class="plotdiv" id="6b451d31-f87b-4832-8467-1df71cf34e0e"></div>', 'p6': u'\n<div class="plotdiv" id="f6f62132-1c06-41ea-812e-734fc925c002"></div>', 'p7': u'\n<div class="plotdiv" id="6ca05731-5239-4dd0-99c1-e3b4b3270ef6"></div>', 'p4': u'\n<div class="plotdiv" id="f5bd0113-83b3-4dcf-ae2a-cabfe70f40ad"></div>', 'p5': u'\n<div class="plotdiv" id="6b358f06-33bc-484f-8c84-b1d07d0ac143"></div>'}

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

