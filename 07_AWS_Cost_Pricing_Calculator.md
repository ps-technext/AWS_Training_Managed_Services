# Kiro + AWS MCP for Managed Service Team

> **Platform:** Windows 10/11  
> **Duration:** 1 Hour / Day  
> **Tools:** Kiro IDE, AWS CLI v2, uv/uvx, Node.js, npm/npx, AWS IAM Identity Center  
> **Operating Mode:** Read-Only First

## Safety Rules

- ตรวจ `AWS Account ID / Role / Profile / Region` ก่อนทุกครั้ง
- Training ใช้ Read-Only เป็นหลัก
- `autoApprove` ให้เป็น `[]`
- ไม่ให้ AI ทำ Delete / Stop / Restart / Reboot / Terminate / Modify Production อัตโนมัติ
- หากต้องแก้ไข Production ให้ AI แนะนำขั้นตอน แล้ว Engineer Review และ Execute เอง

---

# Day 7 — AWS Cost + Pricing + Pricing Calculator MCP

## Objective

แยกให้ได้ว่าเครื่องมือไหนใช้ทำอะไร:

```text
Billing & Cost MCP
→ ดูค่าใช้จ่ายจริง / historical spend

AWS Pricing MCP
→ ดู unit price / service pricing

AWS Pricing Calculator MCP
→ สร้าง estimate ใหม่ + shareable calculator URL
```

## Task 7.1 — Current Cost Driver

```text
Analyze AWS cost for the current month.

Show:
- Top services
- Cost trend
- Unusual increases
- Items requiring investigation
```

## Task 7.2 — Cost by Account / Service

```text
Group AWS cost by:

1. Linked Account
2. Service

Highlight major cost drivers.
```

## Task 7.3 — Unit Pricing

```text
Find current AWS pricing for:

- EC2 m7i.large
- EC2 m7i.xlarge
- Linux
- On-Demand
- Singapore

Explain the difference.
```

## Task 7.4 — Build Pricing Calculator Estimate

ใช้ `sample-aws-pricing-calculator-mcp@latest`

```text
Use the AWS Pricing Calculator MCP.

Build an estimate for:

Region: Singapore

Application Load Balancer
2 x EC2 m7i.large Linux On-Demand
100 GB gp3 per EC2
1 x RDS MySQL db.r7g.large Multi-AZ

Return:
- Monthly estimate
- Service breakdown
- Shareable AWS Pricing Calculator URL
```

## Task 7.5 — Validate Estimate

```text
Validate the estimate before saving.

If required configuration is missing, tell me exactly which field is missing.
Do not guess.
```

## Task 7.6 — Cost Architecture Diagram

```text
Use the draw.io MCP.

Create an architecture diagram for the same estimate:

Internet
→ ALB
→ 2 x EC2
→ RDS Multi-AZ

Add a note that pricing is based on the AWS Pricing Calculator estimate.
```

## Task 7.7 — Customer Cost Summary

```text
Create a concise customer-facing pricing summary:

- Architecture
- Main assumptions
- Estimated monthly cost
- Main cost drivers
- Items that require validation
- Pricing Calculator URL
```

## Hands-on

- [ ] Actual Cost
- [ ] Unit Pricing
- [ ] Pricing Calculator Estimate
- [ ] Shareable URL
- [ ] Architecture Diagram
- [ ] Customer Summary

## Expected Result

Engineer เข้าใจความต่างระหว่าง Cost Analysis, Pricing Lookup และ Forward-looking Estimate
