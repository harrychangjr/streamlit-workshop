import streamlit as st
import pandas as pd
import numpy as np
import random

st.header("Data elements")

st.sidebar.markdown("Data elements")

st.subheader("st.dataframe")

st.write("""

Display a dataframe as an interactive table.

This command works with dataframes from Pandas, PyArrow, Snowpark, and PySpark. 
It can also display several other types that can be converted to dataframes, e.g. numpy arrays, lists, sets and dictionaries.

""")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.write("You can also pass a Pandas Styler object to change the style of the rendered DataFrame:")

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

st.write("Or you can customize the dataframe via `column_config`, `hide_index`, or `column_order`:")

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.write("`st.dataframe` supports the `use_container_width` parameter to stretch across the full container width:")

# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)

st.subheader("st.data_editor")

st.write("""

Display a data editor widget.

The data editor widget allows you to edit dataframes and many other data structures in a table-like UI.

""")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.write("You can also allow the user to add and delete rows by setting `num_rows` to ""dynamic"":")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.write("Or you can customize the data editor via `column_config`, `hide_index`, `column_order`, or `disabled`:")

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.subheader("st.column_config")

st.write("""

When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in st.dataframe and st.data_editor, it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

""")

st.code("""

Column("Streamlit Widgets", 
        help="Streamlit **widget** commands 🎈")
        
TextColumn("Widgets",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$")

NumberColumn("Price (in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d")

CheckboxColumn("Your favorite?",
            help="Select your **favorite** widgets",
            default=False)
        
SelectboxColumn("App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM"],
            required=True)
        
DatetimeColumn("Appointment",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60)

DateColumn("Birthday",
            min_value=date(1900, 1, 1),
            max_value=date(2005, 1, 1),
            format="DD.MM.YYYY",
            step=1)
        
TimeColumn("Appointment",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60)
        
ListColumn("Sales (last 6 months)",
            help="The sales volume in the last 6 months",
            width="medium")
        
LinkColumn("Trending apps",
            help="The top trending Streamlit apps",
            validate="^https://[a-z]+\.streamlit\.app$",
            max_chars=100,
            display_text="https://(.*?)\.streamlit\.app")
        
ImageColumn("Preview Image", help="Streamlit app preview screenshots")
        
LineChartColumn("Sales (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100)
        
BarChartColumn("Sales (last 6 months)",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100)
        
ProgressColumn("Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000)



""", language='python')

st.subheader("st.table")

st.write("""Display a static table.

This differs from `st.dataframe` in that the table in this case is static: its entire contents are laid out directly on the page.""")

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)

st.subheader("st.metric")

st.write("""Display a metric in big bold font, with an optional indicator of how the metric changed.

Tip: If you want to display a large number, it may be a good idea to shorten it using packages like millify or numerize. E.g. `1234` can be displayed as `1.2k` using `st.metric("Short number", millify(1234))`.""")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")

st.subheader("st.json")

st.write("Display object or string as a pretty-printed JSON string.")

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})