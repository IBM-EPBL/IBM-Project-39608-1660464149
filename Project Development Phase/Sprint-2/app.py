from flask import Flask,render_template,request
import pickle 
from sklearn.preprocessing import StandardScaler
sd = StandardScaler()

dbfile = open('regression.pkl','rb')
model = pickle.load(dbfile)

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/login', methods = ['POST' , 'GET'])
def login():
   #mpg = request.form['mpg']
   cys = float(request.form["noc"])
   dis=float(request.form["dpm"])
   hp=float(request.form["hp"])
   w=float(request.form["w"])
   a=float(request.form["a"])
   my=float(request.form["my"])
   ori=float(request.form["o"])
   print(int(cys),int(dis),int(hp),int(w),int(a),int(my),int(ori))
   total=[[int(cys),int(dis),int(hp),int(w),int(a),int(my),int(ori)]]
   p=model.predict(total)
   p=p[0]
   print(p)
   
   
   return render_template('index.html',label="The performance of the car is "+str(p))




if __name__ == '__main__':
   app.run(debug=True)