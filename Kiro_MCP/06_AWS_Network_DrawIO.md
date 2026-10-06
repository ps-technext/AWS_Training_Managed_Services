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

# Day 6 — AWS Network Troubleshooting + Architecture Diagram


## Objective

ใช้ AWS Network MCP + draw.io MCP วิเคราะห์ Connectivity

## Task 6.1 — Network Overview

```text
Create a network overview for this AWS account.

Show:
- VPC
- Subnets
- Route Tables
- Internet Gateways
- NAT Gateways
- Transit Gateway if available
- Load Balancers

Read-only only.
```

## Task 6.2 — EC2 to RDS

Scenario:

```text
EC2 cannot connect to RDS.
```

Prompt:

```text
Investigate the network path between EC2 and RDS.

Check:
- VPC
- Subnet
- Route Table
- Security Groups
- Network ACL
- DNS
- RDS endpoint/port

Rank the possible causes.

Do not change configuration.
```

## Task 6.3 — Private Subnet Internet

```text
Check whether this private subnet has a valid Internet egress path.

Check:
- Route Table
- NAT Gateway
- Internet Gateway
- Security Groups
- NACL
```

## Task 6.4 — ALB Target Unhealthy

```text
Investigate why ALB targets are unhealthy.

Check:
- Listener
- Target Group
- Health Check
- Security Groups
- Application Port
- Routing
```

## Task 6.5 — Draw Current Network

```text
Use the draw.io MCP.

Create an editable AWS network diagram from the discovered configuration.

Show:
- VPC
- Availability Zones
- Public/Private Subnets
- ALB
- EC2
- RDS
- NAT Gateway
- Internet Gateway
- Transit Gateway if present

Do not invent missing components.
```

## Task 6.6 — Draw Problem Path

```text
Highlight the traffic path:

Client
→ ALB
→ EC2
→ RDS

Mark the suspected failure point.
```

## Hands-on

เลือกหนึ่ง Scenario:

- [ ] EC2 → RDS ไม่ได้
- [ ] Private Subnet ออก Internet ไม่ได้
- [ ] ALB Target Unhealthy

ต้องส่ง:

- [ ] Finding
- [ ] Probable Root Cause
- [ ] Recommended Action
- [ ] draw.io Diagram

## Expected Result

Engineer สามารถอธิบาย Network Issue ด้วยทั้ง Evidence และ Diagram
