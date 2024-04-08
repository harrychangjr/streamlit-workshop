
import sys
import NumPy as np    
import pandas as pd               
import plotly.figure_factory as ff 
 
# setting path
sys.path.append('../multipage_demo')
from multipage_demo.main_page import *

st.set_page_config(          
    page_title = "Real-Time Data Dashboard",             
    page_icon = "Active",          
    layout = "wide",       
)

with st.sidebar:
    st.title('Page 2 ❄️')
    st.caption("Page 2 ❄️")
    
x_filter = st.selectbox ("Select X value", pd.unique(file.columns))
y_filter = st.selectbox ("Select Y value", pd.unique(file.columns))
group_filter = st.selectbox ("Select Group value", pd.unique(file.columns))

chart_visual = st.sidebar.selectbox("Selecting Visual Charts", ("Line Chart", "Bar Chart"))

fig.add_trace(go.scatter (x = data.country, y = data.formerly_drank, mode = ‘Bar Chart’, name = ‘Formerly_Drank’))
