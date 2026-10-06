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

# Day 1 — Windows Setup + Kiro + uv + npx + Workspace MCP


AWS MCP ช่วยให้ Kiro / AI Assistant เข้าถึงข้อมูลและเครื่องมือ AWS ผ่านช่องทางที่เป็นระบบ แทนการให้ Engineer copy command หรือเปิดหลาย Console เอง

ประเด็นหลักที่ใช้ในหลักสูตรนี้:

- แยก Customer ด้วย Workspace + AWS Profile
- ทำ Inventory ได้เร็วขึ้น
- ช่วย Troubleshoot จาก Alarm / Metrics / Logs
- ตรวจ Change ผ่าน CloudTrail
- วิเคราะห์ Network
- ดู Cost / Pricing
- สร้าง Pricing Estimate
- สร้าง Architecture Diagram
- สรุป Incident และ Support Case

---

## Objective

หลังจบวันนี้ Engineer ต้องสามารถ:

- ติดตั้ง Kiro
- ใช้ AWS CLI + IAM Identity Center
- เข้าใจ `uv / uvx`
- เข้าใจ `npm / npx`
- สร้าง Kiro Workspace
- โหลด `mcp.json`
- ทดสอบ AWS MCP, Pricing Calculator MCP และ draw.io MCP

## 1. Install Kiro

ดาวน์โหลด Kiro สำหรับ Windows:

```text
https://kiro.dev/downloads/
```

## 2. Install AWS CLI v2

แนะนำติดตั้งจาก AWS CLI v2 installer หรือใช้วิธีมาตรฐานขององค์กร

ตรวจสอบ:

```powershell
aws --version
```

## 3. Install uv

เปิด PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

ปิดและเปิด PowerShell ใหม่:

```powershell
uv --version
uvx --version
```

### uv / uvx คืออะไร

```text
uv   = จัดการ Python / package / environment
uvx  = รัน Python package/tool โดยไม่ต้องติดตั้ง global
```

ตัวอย่าง:

```powershell
uvx awslabs.aws-network-mcp-server@latest
```

## 4. Install Node.js + npm + npx

แนะนำใช้ Node.js LTS:

```powershell
winget install OpenJS.NodeJS.LTS
```

ปิดและเปิด PowerShell ใหม่ แล้วตรวจสอบ:

```powershell
node --version
npm --version
npx --version
```

### npm / npx คืออะไร

```text
npm = ติดตั้งและจัดการ Node.js package
npx = รัน Node.js package โดยไม่ต้องติดตั้ง global
```

ตัวอย่าง:

```powershell
npx -y sample-aws-pricing-calculator-mcp@latest
```

```powershell
npx -y @drawio/mcp
```

## 5. Configure AWS IAM Identity Center

สร้าง Profile:

```powershell
aws configure sso --profile customer-a-readonly
```

Login:

```powershell
aws sso login --profile customer-a-readonly
```

ตรวจสอบ:

```powershell
aws sts get-caller-identity --profile customer-a-readonly
```

## 6. Create Customer Workspace

แนะนำ:

```text
C:\Managed-Service\Customer-A\
└── .kiro\
    └── settings\
        └── mcp.json
```

เปิด Kiro:

```text
File → Open Folder
C:\Managed-Service\Customer-A
```

หรือกด:

```text
Ctrl + Shift + P
```

ค้นหา:

```text
Kiro: Open workspace MCP config (JSON)
```

นำไฟล์ `mcp.json` ของ Training Package ไปใช้

## 7. Change Customer Profile

ใน `mcp.json` เปลี่ยน:

```text
customer-a-readonly
```

เป็น Profile จริง เช่น:

```text
betagro-prod-readonly
```

และตรวจ Region:

```text
ap-southeast-1
```

## 8. Verify MCP

Save `mcp.json` แล้วเปิด MCP panel ใน Kiro

ควรเห็นอย่างน้อย:

```text
aws-mcp
cloudwatch
cloudtrail
aws-network
billing-cost-management
aws-pricing
aws-pricing-calculator
drawio
```

## 9. First Test

Prompt:

```text
Before doing anything, verify my AWS Account ID, Role/Profile and Region.

This is a read-only investigation.
Do not make any changes.
```

## 10. Test Pricing Calculator MCP

Prompt:

```text
Use the AWS Pricing Calculator MCP.

Create a simple estimate for:
- 1 x EC2 Linux instance
- m7i.large
- Singapore
- On-Demand
- 730 hours/month

Return a shareable AWS Pricing Calculator URL.
```

## 11. Test draw.io MCP

Prompt:

```text
Use the draw.io MCP.

Create a simple AWS architecture diagram:

Internet
  ↓
Application Load Balancer
  ↓
2 x EC2
  ↓
Amazon RDS

Open the diagram in draw.io.
```

## Hands-on

- [ ] Kiro Installed
- [ ] AWS CLI Installed
- [ ] uv / uvx Installed
- [ ] Node.js Installed
- [ ] npm / npx Installed
- [ ] AWS SSO Login สำเร็จ
- [ ] `sts get-caller-identity` ถูก Account
- [ ] Workspace MCP Loaded
- [ ] Pricing Calculator MCP ทำงาน
- [ ] draw.io MCP ทำงาน

## Expected Result

Engineer พร้อมใช้ Kiro + AWS MCP ทั้งฝั่ง Python (`uvx`) และ Node.js (`npx`)
