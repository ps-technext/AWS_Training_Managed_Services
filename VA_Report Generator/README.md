# วิธีใช้ VA Report Generator แบบง่าย

ใช้ไฟล์ `generate_report.py` เพื่ออ่านไฟล์ VA Scan CSV แล้วสร้างรายงานออกมาเป็น:

- `VA_Scan_Report.md`
- `VA_Scan_Report.docx`

---

## 1. ติดตั้ง Python

ดาวน์โหลด Python จาก:

```text
https://www.python.org/downloads/
```

ตอนติดตั้งให้เลือก:

```text
Add Python to PATH
```

ตรวจสอบว่าใช้งานได้:

```powershell
python --version
```

ตัวอย่าง:

```text
Python 3.12.7
```

---

## 2. สร้าง Folder

ตัวอย่าง:

```powershell
mkdir C:\VA-Report
cd C:\VA-Report
```

นำไฟล์ 2 ไฟล์นี้มาไว้ใน Folder เดียวกัน:

```text
C:\VA-Report
│
├── generate_report.py
└── vascanreport.csv
```

> ชื่อ CSV ต้องเป็น `vascanreport.csv`

---

## 3. ติดตั้ง Package

เปิด PowerShell ใน Folder แล้วรัน:

```powershell
pip install pandas matplotlib python-docx
```

รอจนติดตั้งเสร็จ

---

## 4. รัน Report

ใช้คำสั่ง:

```powershell
python generate_report.py
```

ถ้าสำเร็จจะเห็นประมาณนี้:

```text
กำลังอ่านไฟล์ vascanreport.csv...
กำลังสร้างรายงาน VA_Scan_Report.docx...
กำลังสร้างรายงาน VA_Scan_Report.md...
เสร็จสิ้น!
```

---

## 5. ดูไฟล์ที่ได้

หลังรันเสร็จ Folder จะเป็น:

```text
C:\VA-Report
│
├── generate_report.py
├── vascanreport.csv
├── VA_Scan_Report.md
└── VA_Scan_Report.docx
```

เปิดไฟล์:

```text
VA_Scan_Report.docx
```

ด้วย Microsoft Word ได้เลย

---

# วิธีใช้งานครั้งต่อไป

เอาไฟล์ VA Scan CSV ใหม่มาแทนไฟล์เดิม:

```text
vascanreport.csv
```

จากนั้นรัน:

```powershell
python generate_report.py
```

เท่านี้ก็จะสร้าง Report ใหม่
