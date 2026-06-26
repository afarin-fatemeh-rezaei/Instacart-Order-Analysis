-- QUERY 2: Top 10 Products by Reorder Rate
-- Identifies products with the highest customer retention
SELECT 
    p.product_name,
    COUNT(*) AS times_purchased,
    ROUND(SUM(op.reordered) * 100.0 / COUNT(*), 2) AS reorder_rate_percent
FROM order_products op
JOIN products p ON op.product_id = p.product_id
GROUP BY p.product_name
HAVING COUNT(*) > 100  -- Filters out low-volume products to avoid statistical noise
ORDER BY reorder_rate_percent DESC
LIMIT 10;