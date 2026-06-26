# Business Memo: Instacart Order Analysis – Product Growth Opportunities

**To:** Product Leadership Team  
**From:** Afarin Fatemeh Rezaei
**Date:** June 2026  
**Subject:** Data-Driven Recommendations to Drive Revenue & Retention

---

## Executive Summary

This analysis was conducted on 3.4 million grocery orders to identify growth levers for the product. The key findings reveal that weekend shoppers generate significantly higher order values, staple products drive customer loyalty, and a meaningful segment of users is at risk of churning. Immediate action on these three fronts can drive measurable revenue growth.

---

## Key Insights & Recommendations

### 1. Weekend Conversion Lift (A/B Test Simulation)
**Finding:** Weekend shoppers have an average basket size of **11.46 items**, compared to **10.06** on weekdays. This is a **14% increase**.

**Statistical Validation:** An independent T-test yielded a P-value of **0.0000000000**, confirming this difference is statistically significant and not due to random chance.

**Recommendation:** Invest in weekend-specific marketing campaigns, push notifications, and UI features (e.g., "Weekend Family Bundles") to capitalize on this behavior. The 14% lift translates to significant incremental revenue.

---

### 2. Retention Drivers (Best Sellers)
**Finding:** Staple grocery items command the highest reorder rates.
- **Bananas:** 18,726 purchases, 88.4% reorder rate
- **Organic Low Fat Milk:** 91.3% reorder rate

**Recommendation:** Guarantee 100% stock availability for these staples. Out-of-stock events on these items directly threaten customer loyalty. These products should be prioritized in warehouse restocking schedules.

---

### 3. Customer Health (RFM Segmentation)
**Finding:** Currently:
- **53,622 Champions** (high-value, recent buyers)
- **19,950 At-Risk** users (low engagement, likely to churn)

**Recommendation:** Launch a targeted "Win-Back" campaign specifically for the At-Risk segment. Offering a 10% discount voucher or free delivery could reactivate these users, increasing overall revenue without the cost of acquiring new customers.

---

### 4. Overall KPIs
| Metric | Value |
| :--- | :--- |
| Total Orders | 131,209 |
| Unique Customers | 131,209 |
| Avg Basket Size | 10.55 items |
| Avg Days Between Orders | 17.07 days |

---

## Next Steps

1. **Feature Development:** Run a live randomized A/B test for the proposed "Weekend Bundle" feature to confirm causality.
2. **Marketing:** Deploy the win-back campaign within the next 14 days to reduce churn.
3. **Dashboard:** A live dashboard tracking these KPIs is available [HERE](https://datastudio.google.com/reporting/8fac75f1-af58-4064-a7d0-dd44ffdac431).

---

## Appendix

- **Tools Used:** PostgreSQL, Python (Pandas, Scipy, Matplotlib), Data Studio.
- **Data Sample:** Instacart Market Basket Dataset (3.4M orders, 130k users).
