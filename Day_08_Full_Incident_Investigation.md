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

# Day 8 — Full Managed Service Investigation + Report + Diagram


## Scenario

> Customer แจ้งว่า Application ช้าตั้งแต่ 14:00 และต้องการ Incident Summary

## Objective

รวม MCP หลายตัวใน Workflow เดียว

## Task 8.1 — Verify Environment

```text
Before starting:

Verify:
- AWS Account ID
- Role/Profile
- Region

Read-only only.
```

## Task 8.2 — Investigation

```text
Act as an AWS Managed Service Engineer.

Investigate why the application became slow after 14:00.

Check:
1. Account / Role / Region
2. CloudWatch alarms
3. EC2 metrics
4. ALB metrics
5. RDS metrics
6. CloudWatch logs
7. CloudTrail changes
8. Network configuration

Do not make changes.
```

## Task 8.3 — Evidence Quality

```text
Separate:

## Confirmed Facts
## Evidence
## Hypotheses
## Missing Information
## Recommended Next Step
```

## Task 8.4 — Incident Diagram

```text
Use the draw.io MCP.

Create an incident architecture diagram.

Show:
Client
→ ALB
→ EC2
→ RDS

Add:
- Alarm/metric evidence
- Change event if found
- Suspected failure point

Keep it customer-friendly.
```

## Task 8.5 — Incident Report

```text
Create a Managed Service Incident Report:

## Incident Summary
## Impact
## Timeline
## Evidence
## Findings
## Probable Root Cause
## Recommended Action
## Next Step

Keep it concise.
```

## Task 8.6 — AWS Support Case Preparation

```text
Prepare information for AWS Support:

- Problem summary
- Service
- Region
- Resource IDs
- Start time
- Error
- Evidence
- Troubleshooting performed
- Business impact

Do not create or submit the case.
```

## Task 8.7 — Optional Pricing Impact

ถ้า Recommendation ต้องเพิ่ม Capacity:

```text
Use the AWS Pricing Calculator MCP.

Estimate the cost impact of the recommended capacity change.

Return a shareable calculator URL.
```

## Final Pass Criteria

- [ ] Verify Account/Profile
- [ ] Alarm
- [ ] Metrics
- [ ] Logs
- [ ] CloudTrail
- [ ] Network
- [ ] Fact vs Hypothesis
- [ ] Incident Diagram
- [ ] Customer Report
- [ ] Support Case Information
- [ ] Optional Pricing Estimate
- [ ] No unauthorized write action

## Expected Result

Engineer ใช้ Kiro เป็น AI Operations Assistant ได้ตั้งแต่ Investigation → Diagram → Cost Impact → Report
