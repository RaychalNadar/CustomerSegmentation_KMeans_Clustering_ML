#Importing Libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
from sklearn.cluster import KMeans
from flask import *

#Loading Dataset
df=pd.read_excel(r'C:\Users\prema\Desktop\ecom_customer_data.xlsx')

#Handling Null vlaues
df.Gender=df.Gender.fillna(df.Gender.mode()[0])

#Data Normalization
features=df.iloc[:,2:].values
scaler=MinMaxScaler()
scaled_features=scaler.fit_transform(features)

#Training KMeans Model
KMeansModel=KMeans(n_clusters=3)
KMeansModel=KMeansModel.fit(scaled_features)

#Predicting Cluster Labels
cluster_labels=KMeansModel.predict(scaled_features)
df['Cluster_Labels']=pd.DataFrame(cluster_labels)

#Creating a Flask object
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():

    data=None
    scaled_data=None
    cluster_label_of_data=None

    #Extracting form data
    data = [
            request.form['Orders'],
            request.form['Jordan'],
            request.form['Gatorade'],
            request.form['Samsung'],
            request.form['Asus'],
            request.form['Udis'],
            request.form['Mondelez_International'],
            request.form['Wrangler'],
            request.form['Vans'],
            request.form['Fila'],
            request.form['Brooks'],
            request.form['HandM'],
            request.form['Diary_Queen'],
            request.form['Fendi'],
            request.form['Hewlett_Packard'],
            request.form['Pladis'],
            request.form['Asics'],
            request.form['Siemens'],
            request.form['JMSmucker'],
            request.form['Pop_Chips'],
            request.form['Juniper'],
            request.form['Huawei'],
            request.form['Compaq'],
            request.form['IBM'],
            request.form['Burberry'],
            request.form['Mi'],
            request.form['LG'],
            request.form['Dior'],
            request.form['Scabal'],
            request.form['Tommy_Hilfiger'],
            request.form['Hollister'],
            request.form['Forever21'],
            request.form['Colavita'],
            request.form['Microsoft'],
            request.form['Jiffy_mix'],
            request.form['Kraft']
        ]
    
    #Converting to numeric type
    data = [int(d) for d in data]

    print(data)

    #Scaling and reshaping data point
    scaled_data = scaler.transform([data])

    print(scaled_data)

    #Predicting Cluster Labels for a new scaled data point
    cluster_label_of_data = KMeansModel.predict(scaled_data)

    print(cluster_label_of_data)

    #Rendering Template
    return render_template('result.html',result=cluster_label_of_data[0])

#Running the app
if __name__=='__main__':
    app.run(debug=True)