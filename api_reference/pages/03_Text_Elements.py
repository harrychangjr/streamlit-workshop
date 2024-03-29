import streamlit as st

st.header("Text elements")

st.sidebar.markdown("Text elements")

st.subheader("st.markdown")

st.write("Display string formatted as Markdown.")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)

st.subheader("st.title")

st.write("""

Display text in title formatting.

Each document should have a single *st.title()*, although this is not enforced.

""")

st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

st.subheader("st.header")

st.write("Display text in header formatting.")

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

st.subheader("st.subheader")

st.write("Display text in subheader formatting.")

st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

st.subheader("st.caption")

st.write("""Display text in small font.

This should be used for captions, asides, footnotes, sidenotes, and other explanatory text.""")

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.subheader("st.code")

st.write("Display a code block with optional syntax highlighting.")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.subheader("st.text")

st.write("Write fixed-width and preformatted text.")

st.text('This is some text.')

st.subheader("st.latex")

st.write("""
Display mathematical expressions formatted as LaTeX.

Supported LaTeX functions are listed at https://katex.org/docs/supported.html.
""")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.subheader("st.divider")

st.write("Display a horizontal rule.")