#!/usr/bin/env python
# coding: utf-8

# ## COVID VARIANTS EDA ANALYSIS PROJECTS

# In[148]:


#Import Libarary that i want to use in this projects 
# 1} Pandas: Pandas used for data cleaning, data Extraction and data processing 
#2} Numpy: Numpy is used for working in domain of linear algebra
#3} MATLAB & Seaborn: is used for EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np


# In[149]:


# Getting data from folder where i was save the CSV and read that file 
Covid= pd.read_csv("C:/Users/JAYDEEP/Desktop/Power Bi files/covid-variants_EDA.csv")
Covid


# In[5]:


# Getting insight that we have use 
Covid.describe()


# In[7]:


# Checking whole information of data
Covid.info()


# In[11]:


Covid.index


# In[136]:


# Checking which unique location we have
Covid.location.unique()


# In[13]:


# I want to see what types of columns i have
Covid.columns


# In[147]:


# finding and checking for unique value from each column in dataset 

print(f"Countries Unique Number: {Covid.location.nunique()}")
print(f"Date Unique Number: {Covid.date.nunique()}")
print(f"Variants names:\n \n {Covid.variant.unique()}")


# In[15]:


Covid.describe(include='all')


# In[16]:


# Checking Null values in the data
Covid.isnull()


# In[36]:


# Checking date wise mean of number of total sequences
Date_mean=Covid.groupby('date').num_sequences_total.mean()
Date_mean.head(5)


# In[44]:


# Hear i got particular date count that we can explore more 
Location= Covid.groupby('date').date.count()
Location.head(5)


# In[23]:


# As same above i found location count 
Location1=Covid.groupby('location').location.count()
Location1


# In[36]:


Covid.sort_values(by=['location'],ascending=True)


# In[38]:


Covid[Covid.location =='India'].count()


# In[40]:


Location2= Covid.groupby('location').count()
Location2.plot(kind='bar')


# In[95]:


Covid.plot(kind='scatter',x='location',y='variant', color='black')
plt.title('Location wise varient')


# In[127]:


# Checking insights from location India 
India = ['India']
Covid[Covid.location.isin(India)]


# In[ ]:


Covid.groupby('variant').count()


# In[28]:


India= Covid[(Covid.location=='India') & (Covid.variant=='Alpha')]
India.head(10)


# In[4]:


India.sort_values('date').head()


# In[17]:


f,ax = plt.subplots(figsize = (15,30))
sea.barplot(y = Covid.location,x = Covid["num_sequences_total"],palette = "rocket" )
plt.xticks(rotation = 90)
plt.ylabel("Countries")
plt.xlabel("Number of Sequences" )
plt.title("Total Number of Sequences by Countries",color = "black", fontsize = 18)
plt.grid()
plt.show


# In[137]:


# Checking first case where and when and which type of variant is find so per my requirememnt i found that first date and last date 
first_date = pd.to_datetime(Covid['date']).min()
last_date = pd.to_datetime(Covid['date']).max()
print(f"First case seen on{first_date} at {Covid['location'][pd.to_datetime(Covid['date']).idxmin()]} ,Variant : {Covid['variant'][pd.to_datetime(Covid['date']).idxmin()]}")
print(f"Last case seen on {last_date} at {Covid['location'][pd.to_datetime(Covid['date']).idxmax()]},Variant : {Covid['variant'][pd.to_datetime(Covid['date']).idxmax()]}")


# In[138]:


# Hear i want to see on which date first case will be seen at which location and which type of variant is this in India 
Ind = Covid.where(Covid['location']=='India')
Ind.dropna(inplace=True)
Ind.head(5)

first_date = pd.to_datetime(Covid['date']).min()
last_date = pd.to_datetime(Covid['date']).max()
print(f"First case seen on {first_date} at {Ind['location'][pd.to_datetime(Ind['date']).idxmin()]} ,Variant : {Ind['variant'][pd.to_datetime(Ind['date']).idxmin()]}")
print(f"Last case seen on {last_date} at {Ind['location'][pd.to_datetime(Ind['date']).idxmax()]},Variant : {Ind['variant'][pd.to_datetime(Ind['date']).idxmax()]}")


# In[29]:


# Checking Variant wise sequences that find in the whole world 
variants = Covid.variant.unique()
variant_num_seq = []
for i in variants:
    x = Covid[Covid.variant.values==i]
    num_seq = sum(x.num_sequences)
    variant_num_seq.append(num_seq)
    
variant_set = pd.DataFrame({"variant" :variants,"number_of_sequence" : variant_num_seq   })
var_index = variant_set.number_of_sequence.sort_values(ascending=False).index.values
variant_set = variant_set.reindex(var_index)
variant_set


# In[47]:


plt.subplots(figsize=(10,10))
sea.barplot(y=variant_set.variant,x=variant_set.number_of_sequence)
plt.ylabel("Variant")
plt.xlabel("Number_Sequence")
plt.title("Number of Sequence by Variant")


# In[52]:


# As i meanstioned above that hear i found that the location wise varient sum 
num_seq = pd.pivot_table(Covid,'num_sequences', index = ['location'], columns = ['variant'], 
                          aggfunc={'num_sequences': np.sum})
num_seq


# In[58]:


Date_var= pd.pivot_table(Covid,'num_sequences',index= ['date'], columns= ['variant'],
                         aggfunc = {'num_sequences':np.sum})

Date_var


# In[60]:


Covid.plot(color="lightgrey" )


# In[67]:


# Top 10 countres with most spread on different variants of covid-19
for_map = df_num_seq.iloc[0:10]
for_map


f,ax = plt.subplots(figsize = (30,15))
sea.lineplot(x='location',y='Alpha',data=for_map)
sea.lineplot(x='location',y='Beta',data=for_map)
sea.lineplot(x='location',y='Delta',data=for_map)
sea.lineplot(x='location',y='Gamma',data=for_map)
sea.lineplot(x='location',y='Omicron',data=for_map)
plt.xlabel("Countries", fontsize=25)
plt.ylabel("Sample of variant", fontsize=20)
plt.title("Top 10 countries with most Spread of different variants of Covid-19", fontsize = 25)
plt.xticks(rotation=45, fontsize=18)
plt.yticks(fontsize=18)
plt.legend(labels=["Alpha","Beta","Delta","Gamma","Omicron"], title = "Variant", 
           fontsize = '20', title_fontsize = "20")
plt.grid()
plt.show


# ## Covid-19 Spread in India

# In[71]:


Omicron = Covid[Covid['variant'] == 'Omicron']
Delta = Covid[Covid['variant'] == 'Delta']
Beta = Covid[Covid['variant'] == 'Beta']
Alpha= Covid[Covid['variant'] == 'Alpha']
Gamma= Covid[Covid['variant'] == 'Gamma']
others = Covid[(Covid['variant'] != 'Beta') & (Covid['variant'] != 'Delta') & (Covid['variant'] != 'Omicron') & (Covid['variant'] != 'Alpha') & (Covid['variant'] != 'Gamma')]


# In[75]:


omicron_data = Omicron.groupby("date").sum()
omicron_data["date"] = omicron_data.index
delta_data = Delta.groupby("date").sum()
delta_data["date"] = delta_data.index
beta_data = Beta.groupby("date").sum()
beta_data["date"] = beta_data.index
alpha_data = Alpha.groupby("date").sum()
alpha_data["date"] = alpha_data.index
gamma_data = Gamma.groupby("date").sum()
gamma_data["date"] = gamma_data.index
others_data = others.groupby("date").sum()
others_data["date"] = others_data.index

Omicron_ind = Omicron[Omicron['location'] == 'India']
Delta_ind = Delta[Delta['location'] == 'India']
Beta_ind = Beta[Beta['location'] == 'India']
Alpha_ind = Alpha[Alpha['location'] == 'India']
Gamma_ind= Gamma[Gamma['location'] == 'India']
others_ind = others[others['location'] == 'India']
#since others contain different type of variants which may be recorded on same date
others_ind_data = others_ind.groupby("date").sum()


# In[76]:


plt.figure(figsize = (15,8))
sea.lineplot(x=Omicron_ind["date"],y=Omicron_ind["num_sequences"],label="Omicron",linestyle="--")
sea.lineplot(x=Delta_ind['date'],y=Delta_ind['num_sequences'],label='Delta',linestyle="--")
sea.lineplot(x=Beta_ind["date"],y=Beta_ind['num_sequences'],label='Beta',linestyle="--")
sea.lineplot(x=Alpha_ind['date'],y=Alpha_ind['num_sequences'],label='Alpha',linestyle="--")
sea.lineplot(x=Gamma_ind["date"],y=Gamma_ind['num_sequences'],label='Gamma',linestyle="--")
sea.lineplot(x=others_ind['date'],y=others_ind['num_sequences'],label='others',linestyle="--")
plt.xticks(rotation=90)
plt.xlabel("Date", fontsize=16)
plt.ylabel("num_sequences", fontsize=16)
plt.title('Covid-19 Spread in India',fontsize=16)
plt.show()


# In[150]:


plt.figure(figsize = (15,8))
sea.lineplot(x=omicron_data["date"],y=omicron_data["num_sequences"],label="Omicron",linestyle="--")
sea.lineplot(x=delta_data['date'],y=delta_data['num_sequences'],label='Delta',linestyle="--")
sea.lineplot(x=beta_data["date"],y=beta_data['num_sequences'],label='Beta',linestyle="--")
sea.lineplot(x=alpha_data['date'],y=alpha_data['num_sequences'],label='Alpha',linestyle="--")
sea.lineplot(x=gamma_data["date"],y=gamma_data['num_sequences'],label='Gamma',linestyle="--")
sea.lineplot(x=others_data['date'],y=others_data['num_sequences'],label='others',linestyle="--")
plt.xticks(rotation=90)
plt.xlabel("Date", fontsize=16)
plt.ylabel("num_sequences", fontsize=16)
plt.title('Covid-19 cases per day through out the world',fontsize=16)
plt.show()


# In[154]:


plt.figure(figsize=(25,10))

plt.subplot(1,2,1).set_title("Spread of Omicron variant India v/s World", fontdict= { 'fontsize': 18, 'fontweight':'bold'})
sea.lineplot(x=Omicron_ind['date'],y=Omicron_ind["num_sequences"],label="India",)
sea.lineplot(x=omicron_data["date"],y=omicron_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)

plt.subplot(1,2,2).set_title("Spread of Alpha variant India v/s World", fontdict= { 'fontsize': 18, 'fontweight':'bold'})
sea.lineplot(x=Alpha_ind['date'],y=Alpha_ind["num_sequences"],label="India")
sea.lineplot(x=alpha_data["date"],y=alpha_data["num_sequences"],label="World")

plt.xticks(rotation=90)
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)
plt.grid()
plt.show()


# In[ ]:





# In[86]:


plt.figure(figsize=(20,15))
plt.subplot(1,2,2).set_title("Spread of Delta variant India v/s World using log scale plot", fontdict= { 'fontsize': 16, 'fontweight':'bold'})
gx=sea.lineplot(x=Delta_ind['date'],y=Delta_ind["num_sequences"],label="India")
hx=sea.lineplot(x=delta_data["date"],y=delta_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
gx.set(yscale='log')
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)
plt.show()


# In[152]:


# lets now comparing each varient spread India Vs World

plt.figure(figsize=(20,15))

plt.subplot(1,2,1).set_title("Spread of Beta variant India v/s World", fontdict= { 'fontsize': 18, 'fontweight':'bold'})
sea.lineplot(x=Beta_ind['date'],y=Beta_ind["num_sequences"],label="India",)
sea.lineplot(x=beta_data["date"],y=beta_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)

plt.subplot(1,2,2).set_title("Spread of Delta variant India v/s World", fontdict= { 'fontsize': 18, 'fontweight':'bold'})
sea.lineplot(x=Delta_ind['date'],y=Delta_ind["num_sequences"],label="India")
sea.lineplot(x=delta_data["date"],y=delta_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)
plt.show()


# In[89]:


# lets now comparing each varient spread India Vs World

plt.figure(figsize=(25,10))

plt.subplot(1,2,1).set_title("Spread of Gamma variant India v/s World using log scale plot", fontdict= { 'fontsize': 16, 'fontweight':'bold'})
ix = sea.lineplot(x=Gamma_ind['date'],y=Gamma_ind["num_sequences"],label="India",)
jx = sea.lineplot(x=others_data["date"],y=others_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
ix.set(yscale='log')
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)

plt.subplot(1,2,2).set_title("Spread of Others variant India v/s World using log scale plot", fontdict= { 'fontsize': 16, 'fontweight':'bold'})
kx = sea.lineplot(x=others_ind['date'],y=others_ind["num_sequences"],label="India")
lx = sea.lineplot(x=others_data["date"],y=others_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
kx.set(yscale='log')
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)
plt.show()


# In[153]:


# lets now comparing each varient spread India Vs World

plt.figure(figsize=(20,15))

plt.subplot(1,2,1).set_title("Spread of Omricron variant India v/s World using log scale plot", fontdict= { 'fontsize': 16, 'fontweight':'bold'})
ax = sea.lineplot(x=Omicron_ind['date'],y=Omicron_ind["num_sequences"],label="India",)
bx = sea.lineplot(x=omicron_data["date"],y=omicron_data["num_sequences"],label="World")
plt.xticks(rotation=90)
plt.grid()
ax.set(yscale='log')
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)

plt.subplot(1,2,2).set_title("Spread of Alpha variant India v/s World using log scale plot", fontdict= { 'fontsize': 16, 'fontweight':'bold'})
cx =sea.lineplot(x=Alpha_ind['date'],y=Alpha_ind["num_sequences"],label="India")
dx = sea.lineplot(x=alpha_data["date"],y=alpha_data["num_sequences"],label="World")

plt.xticks(rotation=90)
cx.set(yscale='log')
plt.xlabel("Date", fontsize=14)
plt.ylabel("num_sequences", fontsize=14)
plt.grid()
plt.show()


# In[101]:


Covid.corr
f,ax = plt.subplots(figsize=(5, 5))
sea.heatmap(Covid.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax) #remove annot=True, and cee the difference
plt.show()


# In[107]:


#checking num of sequences vs total sequences using Scatter plot 
Covid.plot(kind='scatter', x='num_sequences', y='num_sequences_total',alpha = 0.5,color = 'red')
plt.xlabel('num_sequences')              # label = name of label
plt.ylabel('num_sequences_total')
plt.title('Num of Sequences vs Total Sequences Scatter Plot')   


# In[110]:


data1 = Covid.loc[:,['num_sequences','perc_sequences','num_sequences_total']]
data1.plot()

data1.plot(subplots = True)
plt.show()


# In[122]:


data1 = Covid.set_index(["variant","date"]) 
data1.head(100).sort_values(by='date')


# ## Conclusion

# In[ ]:


From above all the data reading and ploting the data with respected to corresponding sequences here we can conclude following thing:-

The Data set is for 121 country and in overall world there are 24 types of variant found which cause/
responsible for the Covid-19 Infection.
Alpha, Beta, Gamma, Delta and Omicron only these type of variants are labeled by "WHO".
First case registered in world as per Data set on 2020-05-11 at Argentina ,Variant : Alpha &
Last case registered in wolrd as per Data set on 2022-01-05 at Bangladesh,Variant : Alpha
--First case registered in India on 2020-05-11, Variant: Alpha
--Last case registered in India on 2021-12-27, Variant: Alpha
Across the whole world Delta variant cases seen most like :3834100
Max. Aplha variant spread found in United Kingdom = 2,62,781 Nos.
Max. Beta variant spread found in South Africa = 7,489 Nos.
Max. Delta variant spread found in United States = 13,27,443 Nos
Max. Gamma variant spread found in Brazil = 47,252 Nos.
Max. Omicron variant spread found in United Kingdom = 65,137 Nos.

