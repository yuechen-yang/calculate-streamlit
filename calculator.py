import streamlit as st
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt



# Plot the function
def draw_plot(x,y):
  fig = plt.figure()
  plt.plot(x, y, color='skyblue')
  plt.xlabel('x', fontweight='bold')
  plt.ylabel('y', fontweight='bold')
  plt.grid(linestyle = '--')
  return st.pyplot(fig)

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

    st.subheader('x的结果:')

    if len(result)==0:
        st.text("无实数解")
    else:
        for i in result:
            st.markdown("* "+str(i.evalf()))


        st.text("图像")
        #min=st.slider("最小值:",min_value=-20,max_value=20,value=-5)
        #max = st.slider("最大值:", min_value=min, max_value=50, value=5)
        x = np.linspace(-3, 3, 50)
        input_fun=input_fun.replace("^","**")
        y = eval(input_fun)
        #x = np.linspace(-3, 3, 50)
        draw_plot(x,y)