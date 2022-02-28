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

def get_result(a1,a2,b1,b2,n):
    x = sp.Symbol('x', real=True)
    f = "x*(" + str(a2) + "-x)*((" + str(b2) + "-" + str(n) + "*x))**" + str(n) + "-x*(" + str(a1) + "-x)*((" + str(
        b1) + "-" + str(n) + "*x))**" + str(n) + ""
    result = sp.solveset(f, domain=sp.S.Reals)
    return result

header= st.container()
data=st.container()

with header:
    st.title('刘教授小课堂')

with data:
    st.subheader('输入数据')
    #x=st.selectbox('未知数:',options=['x'])
    lef,rig=st.columns(2)
    a1=lef.text_input('a1:',0.5)
    b1 = rig.text_input('b1:',0.3)
    a2= lef.text_input('a2:',0.6)
    b2 = rig.text_input('b2:',0.4)
    n=st.text_input('n:',2)


    ## calculate
    #x = sp.Symbol('x',real=True)
    #f = r"x*("+str(a2)+"-x)*(("+str(b2)+"-"+str(n)+"*x))**"+str(n)+"-x*("+str(a1)+"-x)*(("+str(b1)+"-"+str(n)+"*x))**"+str(n)+""
    #result= sp.solveset(f,domain=sp.S.Reals)


    try:
        st.subheader('x的结果:')
        result=get_result(a1,a2,b1,b2,n)

        if len(result)==0:
            st.text("无实数解")
        else:
            for i in result:
                st.markdown("* "+str(i.evalf()))

            input_fun = "x*(" + str(a2) + "-x)*((" + str(b2) + "-" + str(n) + "*x))**" + str(n) + "-x*(" + str(a1) + "-x)*((" + str(
                b1) + "-" + str(n) + "*x))**" + str(n) + ""


            #st.text("图像")
            #x = np.linspace(-1, 1, 30)
            #input_fun=input_fun.replace("^","**")
            #y = eval(input_fun)
            #x = np.linspace(-1, 1, 30)
            #draw_plot(x,y)
    except BaseException:
        st.error("请重新输入")