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

# Day 3 — AWS Inventory + Account Overview

## Objective

ใช้ Kiro สำรวจ AWS Resource และทำ Account Overview

## Task 3.1 — Account Inventory

```text
Create an AWS inventory for this account.

Include:
- EC2
- RDS
- Load Balancers
- Auto Scaling Groups
- S3
- VPC
- NAT Gateway

Group by Region.

Read-only only.
```

## Task 3.2 — EC2 Inventory

```text
List all EC2 instances.

Show:
- Name
- Instance ID
- Instance Type
- State
- Private IP
- Public IP
- VPC
- Availability Zone
```

## Task 3.3 — Find Tag Gaps

```text
Find EC2 resources missing:

- Name
- Environment
- Owner

Do not modify tags.
```

## Task 3.4 — Public Exposure Review

```text
Identify resources that may be publicly accessible.

Check:
- EC2 Public IP
- Internet-facing Load Balancers
- Public RDS
- S3 public access configuration

Read-only only.
```

## Task 3.5 — Create Architecture Overview with draw.io

```text
Use the available AWS inventory.

Then use the draw.io MCP to create a high-level architecture diagram showing:

- VPC
- Public/Private Subnets
- ALB
- EC2
- RDS
- NAT Gateway

Do not invent resources that are not found.
```

## Task 3.6 — Account Summary

```text
Create a Managed Service account summary:

- Resource count
- Production resources
- Public-facing resources
- Tag gaps
- Potential risks
- Items requiring investigation
```

## Hands-on

- [ ] Inventory
- [ ] Tag Gap
- [ ] Public Exposure
- [ ] Architecture Diagram
- [ ] Account Summary

## Expected Result

Engineer สามารถสร้าง Inventory + Architecture Overview ได้จาก Workflow เดียว
