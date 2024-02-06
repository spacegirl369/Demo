import streamlit as st
import pandas as pd
dict={
    'volume' :[3.5, 7,8,6.9,6],
    'mass' :[10,30,50,64,45],
    'velocity' :[0.05,0.09,0.04,1,0.03],
    'state' :['solid','liquid','solid','solid','liquid']
}
df=pd.DataFrame(dict)
st.title('volume,mass,velocity and state table')
st.table(df)

