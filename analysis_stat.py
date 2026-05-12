import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. 데이터 로드
df = pd.read_csv('Churn_Modelling.csv')

# 2. 로그 변환 (Log Transformation)
# Balance와 EstimatedSalary가 0인 경우를 대비해 +1을 해줍니다 (log1p)
df['Log_Balance'] = np.log1p(df['Balance'])
df['Log_Salary'] = np.log1p(df['EstimatedSalary'])

# 3. 범주형 변수 처리 (Gender: Female=1, Male=0)
df['IsFemale'] = df['Gender'].map({'Female': 1, 'Male': 0})

# 4. 분석에 사용할 독립변수(X)와 종속변수(y) 설정
features = ['CreditScore', 'Age', 'Tenure', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'Log_Balance', 'Log_Salary', 'IsFemale']
X = df[features]
X = sm.add_constant(X) # 상수항 추가
y = df['Exited']

# 5. 로지스틱 회귀 분석 (Logistic Regression)
model = sm.Logit(y, X).fit()

# 6. 결과 출력 (P-value 및 오즈비 확인)
print("--- 로지스틱 회귀 결과 요약 ---")
print(model.summary())

# 오즈비(Odds Ratio) 계산: 계수에 지수를 취함
odds_ratios = np.exp(model.params)
print("\n--- 오즈비 (Odds Ratio) ---")
print(odds_ratios)

# 7. 다중공선성(VIF) 체크
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print("\n--- VIF 결과 (다중공선성) ---")
print(vif_data)