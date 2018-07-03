# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
#import pickle
import pandas as pd



app=Flask(__name__)



@app.route('/login')
def details():
    return render_template("input.html")

@app.route('/output',methods=['POST'])
def prediction():
    if request.method=='POST':
        input_data1=int(request.form.get('input'))
        input_data2=int(request.form.get('input1'))
        #input_data3=request.form.get('input3')
        
        #model11=pickle.load(open("C:\\Users\\sabhiniveeshu.kumar\\DataScience\\Python\\Hackathon\\ApplicationForecaster-DataSet\\hack.sav","rb"))
        #prediction=model11(input_data1,input_data2)
        
        data=pd.read_csv("we.csv")
    
    #result=pd.DataFrame([]) 
    #result_mon=pd.DataFrame([])
        #input_daat=input_data1.astype(int)
        a=data.loc[data['Zip']==input_data1]
    
        aa=data.loc[(data['Month']==input_data2) & (data['Zip']==input_data1)]
    
        a['Count']=a.groupby('Product')['Product'].transform('count')
    
        aa['Count_m']=aa.groupby('Product')['Product'].transform('count')
        a['Prob']=a['Count'].map(lambda x : x/sum(a['Count']))
    
        aa['Prob_month']=aa['Count_m'].map(lambda x : x/sum(aa['Count_m']))
    #b=a.sort_values('Prob',ascending=False)
    
    #bb=aa.sort_values('Prob_month',ascending=False)
    #e=b['Prob'].unique()
    #ee=bb['Prob_month'].unique()
    
    #size=len(e)
    #g=[]
    #l=[]
    #count=0
    #for i in e:
        #f=a.loc[(a['Prob']==i) & (a['Zip']==zip)]
        #h=f['Product'].unique()
        #k=f['Prob'].unique()
        
            
            
        
        #k=k*100
        #l.append(k)
       # g.append(h)
        
        #count=count+1
        #if count==5:
            #break
    #result['Product']=g
    #result['Probability']=l
    
        zip=a[['Product','Prob']]
    
        month=aa[['Product','Prob_month']]
    
        total_file=zip.merge(month,on=['Product'])
    
        total_file['Total_Prob']=total_file['Prob'] * total_file['Prob_month'] *1000
    
        Total_f_rd=total_file.drop_duplicates(['Product','Total_Prob'])
    
        total_sort=Total_f_rd.sort_values(['Total_Prob'],ascending=False)
    
        to_pro_larg=total_sort.nlargest(1,'Total_Prob')

            
      
    #gg=[]
    #ll=[]
    #for j in ee:
        #ff=aa.loc[(aa['Prob_month']==j) & (aa['Zip']==zip)]
        #hh=ff['Product'].unique()
        #kk=ff['Prob_month'].unique()
        #gg.append(hh)
        #ll.append(kk)
    
    #result_mon['Product']=gg
    #result_mon['Probabil_month']=ll
    
    #result['Product']=result['Product'].astype(str).str.strip('[]')
    #result['Probability']=result['Probability'].astype(str).str.strip('[]').astype(float)
    
    #result_mon['Product']=result_mon['Product'].astype(str).str.strip('[]')
    #result_mon['Probabil_month']=result_mon['Probabil_month'].astype(str).str.strip('[]').astype(float)
    
    #final=result.merge(result_mon,on=['Product']) 
    #final['Total_Proba']=final['Probability']*final['Probabil_month']*1000
    
    #final_p=final.sort_values('Total_Proba',ascending=False)
    
        #return to_pro_larg['Product']
        
        
        
        
        
        
        
        
        
        return render_template("output.html",output=to_pro_larg)
        #y=to_pro_larg
        #if y:
            #return render_template("output.html",output=to_pro_larg)
        #else:
            #return "PLease"



if __name__== "__main__":
    app.debug=True
    app.run(port=5000)

