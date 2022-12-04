# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# print(df.isnull().sum()/len(df))

# f3 컬럼 삭제
df = df.drop('f3', axis = 1)

# f1의 결측치는 city별 중앙값으로 대체
# print(df.groupby('city')['f1'].median())

k = 58.0
d = 75.0
b = 62.0
s = 68.0

# f1 결측치 city별 중앙값으로 대체
df['f1'] = df['f1'].fillna(
    df['city'].map({'서울':s, '경기':k, '부산':b, '대구':d}))

print(df)

