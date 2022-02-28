import streamlit as st
import sympy as sp

header= st.container()
data=st.container()

with header:
    st.title('刘教授小课堂')

with data:
    st.subheader('输入数据')
    x=st.selectbox('未知数:',options=['x'])
    input_fun=st.text_input('方程:','2*x^3+2*x^2+x-5/10')

    ## calculate
    x = sp.Symbol(x,real=True)
    f = input_fun
    result = sp.solveset(f,domain=sp.S.Reals)

    st.subtitle('x的结果:')

    if len(result)==0:
        st.text("无实数解")
    else:
        for i in result:
            st.markdown("* "+str(i.evalf()))

