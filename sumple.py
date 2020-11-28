import streamlit as st
import pandas as pd
import numpy as np


st.title("tokuno My first APP")

st.write("データフレーム")
st.write(pd.DataFrame({
"1st colum" : [1,2,3,4],
 "2nd colum" : [10,20,30,40]
}))

"""
# My 1st APP
## マジックコマンド
こんな感じでマジックコマンドを利用できる。MarkDown対応。

"""
if st.checkbox("Show DataFrame"):
    chart_df = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
    )

    st.line_chart(chart_df)
