import psycopg2
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

# CONNECT TO DATABASE
conn = psycopg2.connect(
    host="localhost",
    database="instacart_analysis",
    user="postgres",
    password="0024049379"  
)

print("✅ Connected to PostgreSQL successfully!")

# PULL THE RAW DATA FOR A/B TEST 
query = """
    SELECT 
        o.order_id,
        CASE WHEN o.order_dow IN (0, 6) THEN 'Weekend' ELSE 'Weekday' END as day_type,
        COUNT(op.product_id) as basket_size
    FROM orders o
    JOIN order_products op ON o.order_id = op.order_id
    GROUP BY o.order_id, day_type
"""

df = pd.read_sql(query, conn)
print(f"✅ Pulled {len(df)} orders from the database.")

# RUN THE STATISTICAL T-TEST
weekend = df[df['day_type'] == 'Weekend']['basket_size']
weekday = df[df['day_type'] == 'Weekday']['basket_size']

t_stat, p_value = stats.ttest_ind(weekend, weekday)

print("\n" + "="*50)
print("📊 A/B TEST STATISTICAL RESULTS")
print("="*50)
print(f"Weekend Average Basket: {weekend.mean():.2f} items")
print(f"Weekday Average Basket: {weekday.mean():.2f} items")
print(f"Difference: {weekend.mean() - weekday.mean():.2f} items")
print(f"P-Value: {p_value:.10f}")

if p_value < 0.05:
    print("✅ RESULT: STATISTICALLY SIGNIFICANT! The weekend increase is real.")
else:
    print("❌ RESULT: NOT STATISTICALLY SIGNIFICANT. The difference could be random.")
print("="*50)

# CREATE A BOXPLOT CHART
plt.figure(figsize=(10, 6))
sns.boxplot(x='day_type', y='basket_size', data=df, palette=['#FF6B6B', '#4ECDC4'])
plt.title('Weekend vs Weekday Basket Size Comparison', fontsize=16)
plt.ylabel('Number of Items in Basket')
plt.xlabel('Day Type')
plt.grid(axis='y', alpha=0.3)

# Save the chart to Desktop
chart_path = os.path.expanduser("~/Desktop/weekend_weekday_chart.png")
plt.savefig(chart_path, dpi=300, bbox_inches='tight')
print(f"✅ Chart saved to your Desktop: {chart_path}")

# SAVE THE FULL DATAFRAME AS CSV 
csv_path = os.path.expanduser("~/Desktop/ab_test_raw_data.csv")
df.to_csv(csv_path, index=False)
print(f"✅ Raw data saved to: {csv_path}")

# Pull the Top 10 Products 
top_products_query = """
    SELECT 
        p.product_name,
        COUNT(*) AS times_purchased,
        ROUND(SUM(op.reordered) * 100.0 / COUNT(*), 2) AS reorder_rate
    FROM order_products op
    JOIN products p ON op.product_id = p.product_id
    GROUP BY p.product_name
    HAVING COUNT(*) > 100
    ORDER BY reorder_rate DESC
    LIMIT 10
"""
df_top = pd.read_sql(top_products_query, conn)
top_csv_path = os.path.expanduser("~/Desktop/top_10_products.csv")
df_top.to_csv(top_csv_path, index=False)
print(f"✅ Top 10 products saved to: {top_csv_path}")

# Close the connection
conn.close()
print("\n🎉 Python analysis complete!")