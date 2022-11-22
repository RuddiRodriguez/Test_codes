from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from  PIL import Image
import io 


st.set_page_config(layout='wide') #Choose wide mode as the default setting

#Add a logo (optional) in the sidebar

#Add the expander to provide some information about the app
with st.sidebar.expander("About the App"):
     st.write("""
        Interactive project management App )
     """)
    #  



st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Times'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Upload your project plan file and generate Gantt chart instantly</p>', unsafe_allow_html=True)

st.subheader('Step 2: Upload your project plan file')
uploaded_file = st.file_uploader("Fill out the project plan template and upload your file here. After you upload the file, you can edit your project plan within the app.", type=['csv'])
if uploaded_file is not None:
    Tasks=pd.read_csv(uploaded_file)
    
    Tasks['Data_to_AA'] = Tasks['Data_to_AA'].astype('datetime64')
    Tasks['Due_Date'] = Tasks['Due_Date'].astype('datetime64')
    
    grid_response = AgGrid(
        Tasks,
        editable=True, 
        height=300, 
        width='100%',
        )

    updated = grid_response['data']
    df = pd.DataFrame(updated) 
    df.to_csv(r'C:\Users\ruddi.garcia\Projects\ExcelPlanning\Data_Report\backup.csv', index=False)
    
    #Main interface - section 3
    st.subheader('Step 3: Generate the Gantt chart')
    
    Options = st.selectbox("View Gantt Chart by:", ['AA_Contact'],index=0)
    #if st.button('Generate Gantt Chart'): 
    fig = px.timeline(
                    df, 
                    x_start="Data_to_AA", 
                    x_end="Due_Date", 
                    y="AA_Contact",
                    color=Options,
                    hover_name="Project_Name"
                    )

    fig.update_yaxes(autorange="reversed")          #if not specified as 'reversed', the tasks will be listed from bottom up       
    
    fig.update_layout(
                    title='Project Plan Gantt Chart',
                    hoverlabel_bgcolor='#DAEEED',   #Change the hover tooltip background color to a universal light blue color. If not specified, the background color will vary by team or completion pct, depending on what view the user chooses
                    bargap=0.2,
                    height=600,              
                    xaxis_title="", 
                    yaxis_title="",                   
                    title_x=0.5,                    #Make title centered                     
                    xaxis=dict(
                            tickfont_size=15,
                            tickangle = 270,
                            rangeslider_visible=True,
                            side ="top",            #Place the tick labels on the top of the chart
                            showgrid = True,
                            zeroline = True,
                            showline = True,
                            showticklabels = True,
                            tickformat="%x\n",      #Display the tick labels in certain format. To learn more about different formats, visit: https://github.com/d3/d3-format/blob/main/README.md#locale_format
                            )
                )
    
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='blue', size=15))

    st.plotly_chart(fig, use_container_width=True)  #Display the plotly chart in Streamlit

    st.subheader('Bonus: Export the interactive Gantt chart to HTML and share with others!') #Allow users to export the Plotly chart to HTML
    buffer = io.StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    html_bytes = buffer.getvalue().encode()
    st.download_button(
        label='Export to HTML',
        data=html_bytes,
        file_name='Gantt.html',
        mime='text/html'
    ) 
#else:
    st.write('---') 

else:
    st.warning('You need to upload a csv file.')