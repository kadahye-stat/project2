#1 데이터 정합성 확인
-- 전체 행 수 확인
SELECT count(*) FROM Bank_Churn;

-- 상위 5개 샘플 확인
SELECT * FROM Bank_Churn LIMIT 5;

#2 성별에 따른 고객 이탈률 분석
## 남성보다 여성이 더 많이 이탈할까?
SELECT 
    Gender, 
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned_count,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct
FROM Bank_Churn
GROUP BY Gender;

#3 연령대별 고객 이탈률 분석
## 연령대별로 이탈률이 어떻게 달라질까?
SELECT 
    CASE 
        WHEN Age < 30 THEN 'Under 30'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        ELSE '60 and above'
    END AS Age_Group,
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned_count,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct
FROM Bank_Churn
GROUP BY Age_Group
ORDER BY Age_Group; 

#4 보유 상품 수(NumOfProducts)에 따른 고객 이탈률 분석
## 은행 상품을 1개만 쓰는 사람과 3-4개 쓰는 사람 중 누가 더 많이 떠날까?
SELECT 
    NumOfProducts,
    COUNT(*) AS total,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate
FROM Bank_Churn
GROUP BY NumOfProducts
ORDER BY NumOfProducts;

