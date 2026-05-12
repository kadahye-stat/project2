import pandas as pd
import sqlite3

# 1. 같은 폴더에 있는 CSV 파일을 읽어옵니다.
df = pd.read_csv('Churn_Modelling.csv')

# 2. bank.db라는 이름의 데이터베이스 파일에 연결합니다.
conn = sqlite3.connect('bank.db')

# 3. 'Bank_Churn'이라는 이름의 테이블로 데이터를 저장합니다.
df.to_sql('Bank_Churn', conn, if_exists='replace', index=False)

conn.close()
print("성공! 이제 bank.db 파일이 생성되었습니다.")