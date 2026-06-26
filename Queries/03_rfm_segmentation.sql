-- QUERY 3: RFM Customer Segmentation
-- Uses NTILE to score customers by frequency and recency
WITH customer_metrics AS (
    SELECT 
        o.user_id,
        COUNT(DISTINCT o.order_id) AS order_frequency,
        MAX(o.days_since_prior_order) AS recency  -- Lower recency = more recent
    FROM orders o
    GROUP BY o.user_id
),
scored_customers AS (
    SELECT 
        user_id,
        NTILE(4) OVER (ORDER BY order_frequency DESC) AS frequency_score,
        NTILE(4) OVER (ORDER BY recency ASC) AS recency_score
    FROM customer_metrics
)
SELECT 
    'Champions (High Freq, Recent)' AS segment,
    COUNT(*) AS user_count
FROM scored_customers
WHERE frequency_score >= 3 AND recency_score >= 3
UNION ALL
SELECT 
    'At-Risk (Low Freq, Old)',
    COUNT(*)
FROM scored_customers
WHERE frequency_score = 1 AND recency_score = 1;