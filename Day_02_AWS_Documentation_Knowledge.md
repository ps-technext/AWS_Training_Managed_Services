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

# Day 2 — AWS Documentation + Knowledge Workflow

## Objective

ใช้ Kiro เป็น AWS Knowledge Assistant สำหรับงาน Managed Service

## Task 2.1 — AWS Best Practice

```text
Find the current AWS best practices for Amazon RDS Multi-AZ.

Summarize:
1. How it works
2. Failover behavior
3. What Managed Service should monitor
4. Important limitations

Use AWS documentation as the primary source.
```

## Task 2.2 — Configuration Lookup

```text
Find the AWS documentation for Application Load Balancer idle timeout.

Explain:
- Default value
- How it works
- How to change it
- Operational impact
```

## Task 2.3 — Operations Checklist

เลือก:

```text
EC2 / RDS / ALB / S3 / CloudFront / WAF
```

Prompt:

```text
Create a Managed Service operational checklist for Amazon <SERVICE>.

Separate into:
- Daily
- Weekly
- Monthly
- Security
- Cost
```

## Task 2.4 — Troubleshooting Knowledge

```text
Find AWS documentation for troubleshooting high CPU on EC2.

Convert it into a short troubleshooting runbook for an L1/L2 Managed Service Engineer.
```

## Task 2.5 — Create Knowledge Flow Diagram

ใช้ draw.io MCP:

```text
Use the draw.io MCP.

Create a flowchart:

Customer Issue
→ Search AWS Documentation
→ Check Service Configuration
→ Check Metrics / Logs
→ Form Hypothesis
→ Recommend Next Action
```

## Hands-on

- [ ] หา Best Practice
- [ ] หา Configuration
- [ ] สร้าง Operations Checklist
- [ ] สร้าง Troubleshooting Runbook
- [ ] สร้าง Knowledge Flow ใน draw.io

## Expected Result

Engineer ใช้ Kiro ช่วยหา AWS Knowledge และเปลี่ยนเป็น Runbook/Checklist ได้
