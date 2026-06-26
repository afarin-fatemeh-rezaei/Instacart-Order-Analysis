-- QUERY 1: Product Health KPIs
-- Measures overall business performance
SELECT 
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.user_id) AS unique_customers,
    ROUND(COUNT(op.product_id) * 1.0 / COUNT(DISTINCT o.order_id), 2) AS avg_items_per_basket,
    ROUND(AVG(o.days_since_prior_order)::numeric, 2) AS avg_days_between_purchases
FROM orders o
JOIN order_products op ON o.order_id = op.order_id;