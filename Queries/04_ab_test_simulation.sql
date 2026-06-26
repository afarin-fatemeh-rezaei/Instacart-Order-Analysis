-- QUERY 4: A/B Test Simulation (Weekend vs Weekday)
-- Compares average basket size and order timing between groups
SELECT 
    CASE 
        WHEN o.order_dow IN (0, 6) THEN 'Weekend (Treatment)' 
        ELSE 'Weekday (Control)' 
    END AS test_group,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(COUNT(op.product_id) * 1.0 / COUNT(DISTINCT o.order_id), 2) AS avg_basket_size,
    ROUND(AVG(o.order_hour_of_day)::numeric, 2) AS avg_order_hour
FROM orders o
JOIN order_products op ON o.order_id = op.order_id
GROUP BY test_group;