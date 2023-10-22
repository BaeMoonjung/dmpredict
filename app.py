import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st

dataset = pd.read_csv("healthexamRe.csv")
dataset = dataset.dropna(axis=0)
dataset.insert(2, 'bmi',dataset["WEIGHT"]/((dataset["HEIGHT"]/100)**2))

X = dataset.iloc[:, 2:4].values
y_gluco = dataset.iloc[: , 6].values

X_train, X_test, y_train, y_test = train_test_split(X,y_gluco, test_size=0.2, random_state=0)

reg = LinearRegression()
reg.fit(X_train, y_train)

# height = int(input("키를 입력하세요:"))
# weight = int(input("몸무게를 입력하세요:"))
# waist = int(input("허리둘레를 입력하세요:"))

st.title('키, 몸무게, 허리둘레를 이용한 당뇨 예측 모델')

height = st.number_input('키를 입력하시오.', value=0)
weight = st.number_input('몸무게를 입력하시오.', value=0)
waist = st.number_input('허리둘레를 입력하시오.', value=0)

if height>0:
    bmi = weight/((height/100)**2)

    gluco_predict=reg.predict([[bmi, waist]])

    if st.button("결과 보기"):
        st.write(f'예상 공복혈당:{round(gluco_predict[0])}')
        if gluco_predict > 125:
            st.write("당뇨병 발생 가능성이 높습니다.")
        elif 100 <= gluco_predict <= 125:
            st.write("공복혈당장애가 있을 가능성이 있습니다. 당뇨 발생 가능성이 있으니 식단 조절 및 운동이 필요합니다.")
        else:
            st.write("정상 입니다.")
        
        if st.button("다시하기"): 
            height = 0
            weight = 0
            waist = 0 