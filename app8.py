# 파일을 분리해서 개발하는 방법

# 파일을 분리해서 개발할 때 장점.
# 1. 협업이 가능하다.
# 2. 디버깅을 쉽게 할수 있다.

import streamlit as st

# 다른 파일을 가져와서 사용하기 위해서 사용
from app8_home import run_home
from app8_eda import run_eda
from app8_ml import run_ml
from app8_about import run_about

def main() : 
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()

    elif choice == menu[1]:
        run_eda()
    
    elif choice == menu[2]:
        run_ml()

    elif choice == menu[3]:
        run_about()

if __name__ == '__main__' :
    main()