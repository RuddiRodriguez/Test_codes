# streamlit stacked bar plot.

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Create a dataframe with fake data.

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c'])

# Create a bar plot of the data.

bar = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    color='c')

# Create a line plot of the data.

line = alt.Chart(df).mark_line(color='red').encode(
    x='a',
    y='c')

# Stack the bar and line plots.

chart = alt.layer(bar, line).properties(
    width=600, height=300)

# Display the chart.

st.altair_chart(chart)

