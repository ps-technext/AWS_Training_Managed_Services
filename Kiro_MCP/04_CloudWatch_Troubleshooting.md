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

# Day 4 — CloudWatch Incident Troubleshooting

## Scenario

> Customer แจ้ง Application ช้าตั้งแต่ 14:00

## Objective

ใช้ Kiro ตรวจ Alarm, Metrics และ Logs แล้วสรุป Evidence

## Task 4.1 — Alarm

```text
Check CloudWatch alarms related to EC2, ALB and RDS.

Find alarms that changed state during the incident period.

Read-only only.
```

## Task 4.2 — Metrics

```text
Investigate EC2, ALB and RDS metrics around the incident time.

Focus on:
- CPU
- Network
- Disk
- TargetResponseTime
- 5XX
- HealthyHostCount
- DBConnections
- Latency

Highlight abnormal values.
```

## Task 4.3 — Logs

```text
Search relevant CloudWatch Logs around the incident time.

Look for:
- ERROR
- Timeout
- Connection refused
- 5xx
- Database errors

Return only relevant findings.
```

## Task 4.4 — Fact vs Hypothesis

```text
Separate the result into:

## Facts
## Evidence
## Hypotheses
## Missing Information
## Next Step
```

## Task 4.5 — Troubleshooting Flow Diagram

```text
Use the draw.io MCP.

Create an incident troubleshooting flow:

Customer Ticket
→ Verify Account
→ CloudWatch Alarm
→ EC2/ALB/RDS Metrics
→ Logs
→ Evidence
→ Root Cause Hypothesis
→ Next Action
```

## Hands-on

- [ ] Alarm
- [ ] Metrics
- [ ] Logs
- [ ] Fact/Hypothesis
- [ ] Troubleshooting Diagram

## Expected Result

Engineer ลดเวลาในการรวบรวม Evidence และมี Incident Flow ที่อธิบายให้ทีมอื่นเข้าใจได้
