import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data
import plotly.figure_factory as ff
import plotly.express as px
from bokeh.plotting import figure
import pydeck as pdk
import graphviz

st.header("Chart elements")

st.sidebar.markdown("Chart elements")

st.subheader("st.area_chart")

st.write(
"""
Display an area chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If `st.area_chart` does not guess the data specification correctly, try specifying your desired chart using `st.altair_chart`.

"""
)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

st.area_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)

st.subheader("st.bar_chart")

st.write(
"""
Display a bar chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If `st.bar_chart` does not guess the data specification correctly, try specifying your desired chart using `st.altair_chart`.

"""
)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

chart_data = pd.DataFrame(
   {
       "col1": list(range(20)) * 3,
       "col2": np.random.randn(60),
       "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
   }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")

chart_data = pd.DataFrame(
   {"col1": list(range(20)), "col2": np.random.randn(20), "col3": np.random.randn(20)}
)

st.bar_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)

st.subheader("st.line_chart")

st.write(
"""
Display a line chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If `st.line_chart` does not guess the data specification correctly, try specifying your desired chart using `st.altair_chart`.

"""
)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

st.line_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)

st.subheader("st.scatter_chart")

st.write(
"""
Display a scatterplot chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If `st.scatter_chart` does not guess the data specification correctly, try specifying your desired chart using `st.altair_chart`.

"""
)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
chart_data['col4'] = np.random.choice(['A','B','C'], 20)

st.scatter_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col4',
    size='col3',
)

chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"])

st.scatter_chart(
    chart_data,
    x='col1',
    y=['col2', 'col3'],
    size='col4',
    color=['#FF0000', '#0000FF'],  # Optional
)

st.subheader("st.pyplot")

st.write(
"""
Display a matplotlib.pyplot figure.

"""
)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.subheader("st.altair_chart")

st.write(
"""
Display a chart using the Altair library.

"""
)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)

st.subheader("st.vega_lite_chart")

st.write(
"""
Display a chart using the Vega-Lite library.

"""
)

chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

st.vega_lite_chart(
   chart_data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "a", "type": "quantitative"},
           "y": {"field": "b", "type": "quantitative"},
           "size": {"field": "c", "type": "quantitative"},
           "color": {"field": "c", "type": "quantitative"},
       },
   },
)

source = data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )

st.subheader("st.plotly_chart")

st.write(
"""
Display an interactive Plotly chart.

Plotly is a charting library for Python. The arguments to this function closely follow the ones for Plotly's plot() function. You can find more about Plotly at https://plot.ly/python.

To show Plotly charts in Streamlit, call *st.plotly_chart* wherever you would call Plotly's *py.plot* or *py.iplot*.

"""
)

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)


st.subheader("st.pydeck_chart")

st.write(
"""
Draw a chart using the PyDeck library.

This supports 3D maps, point clouds, and more! More info about PyDeck at https://deckgl.readthedocs.io/en/latest/.

These docs are also quite useful:

DeckGL docs: https://github.com/uber/deck.gl/tree/master/docs

DeckGL JSON docs: https://github.com/uber/deck.gl/tree/master/modules/json

When using this command, Mapbox provides the map tiles to render map content. Note that Mapbox is a third-party product and Streamlit accepts no responsibility or liability of any kind for Mapbox or for any content or information made available by Mapbox.

Mapbox requires users to register and provide a token before users can request map tiles. Currently, Streamlit provides this token for you, but this could change at any time. We strongly recommend all users create and use their own personal Mapbox token to avoid any disruptions to their experience. You can do this with the `mapbox.token` config option. The use of Mapbox is governed by Mapbox's Terms of Use.

To get a token for yourself, create an account at https://mapbox.com. For more info on how to set config options, see https://docs.streamlit.io/library/advanced-features/configuration

"""
)

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

st.subheader("st.graphviz_chart")

st.write(
"""
Display a graph using the dagre-d3 library.

"""
)

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

st.subheader("st.map")

st.write(
"""
Display a map with a scatterplot overlaid onto it.

This is a wrapper around `st.pydeck_chart` to quickly create scatterplot charts on top of a map, with auto-centering and auto-zoom.

When using this command, Mapbox provides the map tiles to render map content. Note that Mapbox is a third-party product and Streamlit accepts no responsibility or liability of any kind for Mapbox or for any content or information made available by Mapbox.

Mapbox requires users to register and provide a token before users can request map tiles. Currently, Streamlit provides this token for you, but this could change at any time. We strongly recommend all users create and use their own personal Mapbox token to avoid any disruptions to their experience. You can do this with the `mapbox.token` config option. The use of Mapbox is governed by Mapbox's Terms of Use.

To get a token for yourself, create an account at https://mapbox.com. For more info on how to set config options, see https://docs.streamlit.io/library/advanced-features/configuration

"""
)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
