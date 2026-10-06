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

# Day 5 — CloudTrail + IAM + Change Investigation

## Objective

ตอบให้ได้:

```text
ใครทำ?
ทำอะไร?
ทำเมื่อไหร่?
มาจากไหน?
กระทบอะไร?
```

## Task 5.1 — Infrastructure Changes

```text
Check CloudTrail for important infrastructure changes during the last 24 hours.

Focus on:
- EC2
- Security Groups
- Load Balancers
- RDS
- IAM

Read-only only.
```

## Task 5.2 — Security Group Change

```text
Find who modified Security Groups in the last 24 hours.

Show:
- Time
- User/Role
- Event
- Resource
- Source IP
```

## Task 5.3 — EC2 Administrative Change

```text
Find:
- StartInstances
- StopInstances
- RebootInstances
- ModifyInstanceAttribute
- RunInstances
- TerminateInstances

during the last 24 hours.

Do not make changes.
```

## Task 5.4 — IAM Review

```text
Identify IAM roles or policies that appear broad.

Separate:
- Confirmed permissions
- Potential risk
- What should be reviewed manually

Do not modify IAM.
```

## Task 5.5 — Change Timeline

```text
Create an incident change timeline:

Time
User/Role
Action
Resource
Possible Impact
```

## Task 5.6 — Draw Change Flow

```text
Use the draw.io MCP.

Create a sequence diagram showing:

Engineer/User
→ AWS API
→ CloudTrail Event
→ Changed Resource
→ Application Impact
→ Managed Service Investigation
```

## Hands-on

- [ ] หา Change
- [ ] หา User/Role
- [ ] หา Source IP
- [ ] สร้าง Timeline
- [ ] วาด Change Flow

## Expected Result

Engineer สามารถเชื่อม Infrastructure Change กับ Incident ได้เร็วขึ้น
