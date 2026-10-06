import pandas as pd
import matplotlib.pyplot as plt
import datetime
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.shared import RGBColor
from docx.oxml.shared import OxmlElement, qn
from docx.enum.table import WD_TABLE_ALIGNMENT

# กำหนดชื่อไฟล์ CSV ที่ต้องการอ่าน (เปลี่ยนตามชื่อไฟล์จริงของคุณ)
INPUT_FILE = 'vascanreport.csv'
OUTPUT_FILE_MD = 'VA_Scan_Report.md'
OUTPUT_FILE_DOCX = 'VA_Scan_Report.docx'

def set_thai_font(paragraph, font_name='TH SarabunPSK', font_size=14):
    """ตั้งค่าฟอนต์ภาษาไทยสำหรับ paragraph"""
    for run in paragraph.runs:
        run.font.name = font_name
        run.font.size = Pt(font_size)

def add_table_style(table, header_color=RGBColor(41, 128, 185), alt_row_color=RGBColor(245, 245, 245)):
    """เพิ่ม modern styling ให้กับตาราง"""
    # Style header row
    for cell in table.rows[0].cells:
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), f'{header_color:06x}' if isinstance(header_color, int) else '2980B9')
        cell._tc.get_or_add_tcPr().append(shading_elm)
        
        # Set header text color to white
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.bold = True
    
    # Alternate row colors
    for i, row in enumerate(table.rows[1:], 1):
        if i % 2 == 0:
            for cell in row.cells:
                shading_elm = OxmlElement('w:shd')
                shading_elm.set(qn('w:fill'), f'{alt_row_color:06x}' if isinstance(alt_row_color, int) else 'F5F5F5')
                cell._tc.get_or_add_tcPr().append(shading_elm)
    
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

def create_executive_summary_box(doc, content):
    """สร้าง summary box สำหรับผู้บริหาร"""
    summary_table = doc.add_table(rows=1, cols=1)
    summary_table.style = 'Table Grid'
    cell = summary_table.cell(0, 0)
    
    # Add blue background
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), 'E8F4FD')
    cell._tc.get_or_add_tcPr().append(shading_elm)
    
    # Add content
    p = cell.paragraphs[0]
    p.text = content
    set_thai_font(p, 'TH SarabunPSK', 14)
    
    return summary_table

def set_table_thai_font(table, font_name='TH SarabunPSK', font_size=12):
    """ตั้งค่าฟอนต์ภาษาไทยสำหรับตาราง"""
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                # ตั้งค่าฟอนต์สำหรับ run ที่มีอยู่
                for run in paragraph.runs:
                    run.font.name = font_name
                    run.font.size = Pt(font_size)
                # หากไม่มี run ให้สร้างใหม่
                if not paragraph.runs and paragraph.text:
                    run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
                    run.font.name = font_name
                    run.font.size = Pt(font_size)

def update_table_content_font(table, font_name='TH SarabunPSK', font_size=12):
    """อัปเดตฟอนต์สำหรับตารางที่มีเนื้อหาแล้ว"""
    for row in table.rows:
        for cell in row.cells:
            # เก็บข้อความเดิม
            original_text = cell.text
            # ล้างเนื้อหาเดิม
            cell.text = ''
            # เพิ่มข้อความใหม่ด้วยฟอนต์ที่ถูกต้อง
            if original_text:
                run = cell.paragraphs[0].add_run(original_text)
                run.font.name = font_name
                run.font.size = Pt(font_size)

def generate_docx_report(total_findings, severity_counts, fix_available_counts, top_resources, top_cves, urgent_fixes, df):
    """สร้างรายงานในรูปแบบ Word Document"""
    print(f"กำลังสร้างรายงาน {OUTPUT_FILE_DOCX}...")
    
    # สร้าง Document ใหม่
    doc = Document()
    
    # ตั้งค่าหน้ากระดาษ A4 และ margins
    section = doc.sections[0]
    section.page_height = Inches(11.7)  # A4 height
    section.page_width = Inches(8.3)    # A4 width
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    
    # Modern Header with company branding area
    # Title with modern styling
    title = doc.add_heading('CYBERSECURITY ASSESSMENT REPORT', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_thai_font(title, 'TH SarabunPSK', 24)
    for run in title.runs:
        run.font.color.rgb = RGBColor(41, 128, 185)  # Professional blue
        run.bold = True
    
    # Subtitle
    subtitle = doc.add_heading('Vulnerability Analysis & Risk Assessment', level=2)
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_thai_font(subtitle, 'TH SarabunPSK', 16)
    for run in subtitle.runs:
        run.font.color.rgb = RGBColor(127, 140, 141)  # Gray
    
    # Report metadata in a styled box
    metadata_table = doc.add_table(rows=3, cols=2)
    metadata_table.style = 'Table Grid'
    
    # Report Date
    metadata_table.cell(0, 0).text = 'Report Date:'
    metadata_table.cell(0, 1).text = datetime.datetime.now().strftime('%B %d, %Y at %H:%M')
    
    # Source
    metadata_table.cell(1, 0).text = 'Data Source:'
    metadata_table.cell(1, 1).text = INPUT_FILE
    
    # Status
    metadata_table.cell(2, 0).text = 'Report Status:'
    metadata_table.cell(2, 1).text = 'CONFIDENTIAL - Executive Summary'
    
    # Style metadata table
    for row in metadata_table.rows:
        for i, cell in enumerate(row.cells):
            if i == 0:  # Labels column
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True
                        run.font.color.rgb = RGBColor(52, 73, 94)
    
    update_table_content_font(metadata_table, 'TH SarabunPSK', 12)
    metadata_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Add spacing
    doc.add_paragraph()
    
    # 1. Executive Summary Dashboard
    exec_heading = doc.add_heading('EXECUTIVE DASHBOARD', level=1)
    set_thai_font(exec_heading, 'TH SarabunPSK', 18)
    for run in exec_heading.runs:
        run.font.color.rgb = RGBColor(41, 128, 185)
    
    # Key metrics dashboard
    dashboard_table = doc.add_table(rows=2, cols=4)
    dashboard_table.style = 'Table Grid'
    
    # Headers
    headers = ['Total Vulnerabilities', 'Critical/High Risk', 'Patchable Issues', 'Affected Resources']
    critical_high = severity_counts.get('CRITICAL', 0) + severity_counts.get('HIGH', 0)
    patchable = fix_available_counts.get('YES', 0)
    
    for i, header in enumerate(headers):
        cell = dashboard_table.cell(0, i)
        cell.text = header
        # Blue background for headers
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), '2980B9')
        cell._tc.get_or_add_tcPr().append(shading_elm)
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.bold = True
    
    # Values
    values = [f"{total_findings:,}", f"{critical_high:,}", f"{patchable:,}", f"{len(top_resources)}"]
    for i, value in enumerate(values):
        cell = dashboard_table.cell(1, i)
        cell.text = value
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.size = Pt(18)
                run.bold = True
                run.font.color.rgb = RGBColor(231, 76, 60) if i == 1 else RGBColor(41, 128, 185)
    
    update_table_content_font(dashboard_table, 'TH SarabunPSK', 14)
    dashboard_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Risk assessment summary
    risk_level = "HIGH" if critical_high > 10 else "MEDIUM" if critical_high > 0 else "LOW"
    risk_color = RGBColor(231, 76, 60) if risk_level == "HIGH" else RGBColor(241, 196, 15) if risk_level == "MEDIUM" else RGBColor(46, 204, 113)
    
    risk_para = doc.add_paragraph()
    risk_para.add_run('Overall Security Risk Level: ')
    risk_run = risk_para.add_run(f'{risk_level}')
    risk_run.bold = True
    risk_run.font.color.rgb = risk_color
    risk_run.font.size = Pt(16)
    set_thai_font(risk_para, 'TH SarabunPSK', 14)
    risk_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Modern Severity Distribution Table
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Risk Level'
    hdr_cells[1].text = 'Count'
    hdr_cells[2].text = 'Percentage'
    hdr_cells[3].text = 'Risk Impact'
    
    # Apply modern header styling
    for cell in hdr_cells:
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), '34495E')  # Dark blue-gray
        cell._tc.get_or_add_tcPr().append(shading_elm)
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
    
    set_table_thai_font(table, 'TH SarabunPSK', 12)
    
    severity_colors = {
        'CRITICAL': ('E74C3C', 'Immediate Action Required'),
        'HIGH': ('F39C12', 'Priority Remediation'),
        'MEDIUM': ('F1C40F', 'Scheduled Patching'),
        'LOW': ('27AE60', 'Monitor & Update'),
        'INFORMATIONAL': ('95A5A6', 'Awareness Only')
    }
    
    for severity, count in severity_counts.items():
        if count > 0:
            percent = (count / total_findings) * 100
            color_hex, impact = severity_colors.get(severity, ('95A5A6', 'Review Required'))
            
            row_cells = table.add_row().cells
            row_cells[0].text = severity
            row_cells[1].text = f"{count:,}"
            row_cells[2].text = f"{percent:.1f}%"
            row_cells[3].text = impact
            
            # Color code the severity level
            for paragraph in row_cells[0].paragraphs:
                for run in paragraph.runs:
                    run.bold = True
                    # Convert hex to RGB values
                    hex_val = color_hex.lstrip('#')
                    r, g, b = tuple(int(hex_val[i:i+2], 16) for i in (0, 2, 4))
                    run.font.color.rgb = RGBColor(r, g, b)
            
            # Center align numeric columns
            for i in [1, 2]:
                row_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Apply alternating row colors
    add_table_style(table, RGBColor(52, 73, 94), RGBColor(250, 250, 250))
    update_table_content_font(table, 'TH SarabunPSK', 12)
    
    # Fix Available Summary
    fix_heading = doc.add_heading('Remediation Status', level=3)
    set_thai_font(fix_heading, 'TH SarabunPSK', 14)
    yes_fix = fix_available_counts.get('YES', 0)
    
    fix_para1 = doc.add_paragraph()
    fix_para1.add_run('Fix Available: ')
    fix_run1 = fix_para1.add_run(f"{yes_fix:,}")
    fix_run1.bold = True
    fix_para1.add_run(' vulnerabilities')
    set_thai_font(fix_para1, 'TH SarabunPSK', 14)
    
    fix_para2 = doc.add_paragraph()
    fix_para2.add_run('No Fix Available: ')
    fix_run2 = fix_para2.add_run(f"{fix_available_counts.get('NO', 0):,}")
    fix_run2.bold = True
    fix_para2.add_run(' vulnerabilities')
    set_thai_font(fix_para2, 'TH SarabunPSK', 14)
    
    # 2. Asset Risk Analysis
    res_heading = doc.add_heading('CRITICAL ASSET ANALYSIS', level=1)
    set_thai_font(res_heading, 'TH SarabunPSK', 16)
    for run in res_heading.runs:
        run.font.color.rgb = RGBColor(231, 76, 60)  # Red for attention
    
    res_desc = doc.add_paragraph('High-risk assets requiring immediate security attention:')
    set_thai_font(res_desc, 'TH SarabunPSK', 14)
    
    resource_table = doc.add_table(rows=1, cols=3)
    resource_table.style = 'Table Grid'
    resource_hdr = resource_table.rows[0].cells
    resource_hdr[0].text = 'Asset / Resource'
    resource_hdr[1].text = 'Vulnerability Count'
    resource_hdr[2].text = 'Risk Status'
    
    # Modern header styling
    for cell in resource_hdr:
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), 'E74C3C')  # Red header
        cell._tc.get_or_add_tcPr().append(shading_elm)
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
    
    set_table_thai_font(resource_table, 'TH SarabunPSK', 12)
    
    for name, count in top_resources.items():
        row_cells = resource_table.add_row().cells
        row_cells[0].text = str(name)
        row_cells[1].text = str(count)
        
        # Determine risk status based on count
        if count > 50:
            risk_status = "CRITICAL"
            risk_color = RGBColor(231, 76, 60)
        elif count > 20:
            risk_status = "HIGH"
            risk_color = RGBColor(241, 196, 15)
        else:
            risk_status = "MEDIUM"
            risk_color = RGBColor(52, 152, 219)
        
        row_cells[2].text = risk_status
        row_cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row_cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Color code risk status
        for run in row_cells[2].paragraphs[0].runs:
            run.bold = True
            run.font.color.rgb = risk_color
    
    add_table_style(resource_table, RGBColor(231, 76, 60), RGBColor(254, 245, 245))
    update_table_content_font(resource_table, 'TH SarabunPSK', 12)
    
    # 3. Top Vulnerabilities
    cve_heading = doc.add_heading('3. Top 5 Common Vulnerabilities', level=1)
    set_thai_font(cve_heading, 'TH SarabunPSK', 16)
    
    cve_table = doc.add_table(rows=1, cols=2)
    cve_table.style = 'Table Grid'
    cve_hdr = cve_table.rows[0].cells
    cve_hdr[0].text = 'CVE / Title'
    cve_hdr[1].text = 'Occurrence Count'
    
    for hdr_cell in cve_hdr:
        for paragraph in hdr_cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
    
    set_table_thai_font(cve_table, 'TH SarabunPSK', 12)
    
    for title, count in top_cves.items():
        short_title = (title[:70] + '..') if len(title) > 70 else title
        row_cells = cve_table.add_row().cells
        row_cells[0].text = short_title
        row_cells[1].text = str(count)
    
    # อัปเดตฟอนต์หลังจากเพิ่มข้อมูล
    update_table_content_font(cve_table, 'TH SarabunPSK', 12)
    
    # 4. Executive Action Plan
    action_heading = doc.add_heading('EXECUTIVE ACTION PLAN', level=1)
    set_thai_font(action_heading, 'TH SarabunPSK', 16)
    for run in action_heading.runs:
        run.font.color.rgb = RGBColor(46, 204, 113)  # Green for action
    
    # Priority matrix box
    priority_para = doc.add_paragraph()
    priority_run = priority_para.add_run('PRIORITY 1: ')
    priority_run.bold = True
    priority_run.font.color.rgb = RGBColor(231, 76, 60)
    priority_para.add_run('Critical & High severity vulnerabilities with immediate patches available')
    set_thai_font(priority_para, 'TH SarabunPSK', 14)
    
    action_desc = doc.add_paragraph('Recommended immediate remediation actions for executive approval:')
    set_thai_font(action_desc, 'TH SarabunPSK', 14)
    
    if not urgent_fixes.empty:
        action_table = doc.add_table(rows=1, cols=5)
        action_table.style = 'Table Grid'
        action_hdr = action_table.rows[0].cells
        action_hdr[0].text = 'Resource'
        action_hdr[1].text = 'Severity'
        action_hdr[2].text = 'CVE'
        action_hdr[3].text = 'Package / Component'
        action_hdr[4].text = 'Fixed Version'
        
        for hdr_cell in action_hdr:
            for paragraph in hdr_cell.paragraphs:
                for run in paragraph.runs:
                    run.bold = True
        
        set_table_thai_font(action_table, 'TH SarabunPSK', 11)
        
        def get_resource_name(row):
            tags = str(row.get('Resource Tags', ''))
            if 'Name:' in tags:
                try:
                    return tags.split('Name:')[1].split(',')[0]
                except:
                    return row.get('Resource ID', 'Unknown')
            return row.get('Resource ID', 'Unknown')
        
        for _, row in urgent_fixes.iterrows():
            res_name = get_resource_name(row)
            cve = row['Title'].split(' ')[0] if ' ' in row['Title'] else row['Title']
            pkg = row.get('Affected Packages', '-')
            fixed_ver = row.get('Fixed in Version', '-')
            
            row_cells = action_table.add_row().cells
            row_cells[0].text = str(res_name)
            row_cells[1].text = str(row['Severity'])
            row_cells[2].text = str(cve)
            row_cells[3].text = str(pkg)
            row_cells[4].text = str(fixed_ver)
        
        # อัปเดตฟอนต์หลังจากเพิ่มข้อมูล
        update_table_content_font(action_table, 'TH SarabunPSK', 11)
    else:
        no_items_para = doc.add_paragraph('No Critical/High severity vulnerabilities with available patches found at this time.')
        set_thai_font(no_items_para, 'TH SarabunPSK', 12)
    
    # 5. Complete Vulnerability Details
    detail_heading = doc.add_heading('5. Complete Vulnerability Details with Remediation', level=1)
    set_thai_font(detail_heading, 'TH SarabunPSK', 16)
    
    intro_para = doc.add_paragraph(f'Complete list of {total_findings:,} vulnerabilities with remediation guidance:')
    set_thai_font(intro_para, 'TH SarabunPSK', 14)
    
    # Summary information
    summary_para = doc.add_paragraph()
    summary_run = summary_para.add_run('This report provides detailed information for all identified vulnerabilities, including: ')
    summary_run.bold = True
    set_thai_font(summary_para, 'TH SarabunPSK', 14)
    
    bullet1 = doc.add_paragraph('• Severity levels and vulnerability types')
    set_thai_font(bullet1, 'TH SarabunPSK', 12)
    bullet2 = doc.add_paragraph('• Affected resources and systems')
    set_thai_font(bullet2, 'TH SarabunPSK', 12)
    bullet3 = doc.add_paragraph('• Vulnerable packages and versions')
    set_thai_font(bullet3, 'TH SarabunPSK', 12)
    bullet4 = doc.add_paragraph('• Patch availability and update procedures')
    set_thai_font(bullet4, 'TH SarabunPSK', 12)
    bullet5 = doc.add_paragraph('• Reference links and additional information')
    set_thai_font(bullet5, 'TH SarabunPSK', 12)
    doc.add_paragraph('')    # Group vulnerabilities by severity level
    severity_order = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL']
    
    for severity_level in severity_order:
        severity_vulnerabilities = df[df['Severity'] == severity_level]
        if len(severity_vulnerabilities) == 0:
            continue
            
        sev_heading = doc.add_heading(f'{severity_level} Severity Vulnerabilities ({len(severity_vulnerabilities)} items)', level=2)
        set_thai_font(sev_heading, 'TH SarabunPSK', 15)
        
        def get_resource_name_func(row):
            tags = str(row.get('Resource Tags', ''))
            if 'Name:' in tags:
                try:
                    return tags.split('Name:')[1].split(',')[0]
                except:
                    return row.get('Resource ID', 'Unknown')
            return row.get('Resource ID', 'Unknown')
        
        # Display details for each vulnerability
        for index, (_, row) in enumerate(severity_vulnerabilities.iterrows(), 1):
            # Vulnerability title
            vuln_title = str(row.get('Title', 'N/A'))
            cve_id = vuln_title.split(' ')[0] if ' ' in vuln_title else vuln_title
            
            vuln_heading = doc.add_heading(f'{index}. {cve_id}', level=3)
            set_thai_font(vuln_heading, 'TH SarabunPSK', 14)
            
            # Basic information table
            info_table = doc.add_table(rows=6, cols=2)
            info_table.style = 'Table Grid'
            set_table_thai_font(info_table, 'TH SarabunPSK', 11)
            
            # Affected Resource
            resource_name = get_resource_name_func(row)
            info_table.cell(0, 0).text = 'Affected Resource'
            info_table.cell(0, 1).text = str(resource_name)
            
            # Affected Package
            packages = str(row.get('Affected Packages', 'N/A'))
            info_table.cell(1, 0).text = 'Affected Package'
            info_table.cell(1, 1).text = packages
            
            # Current Version
            current_version = str(row.get('Package Installed Version', 'N/A'))
            info_table.cell(2, 0).text = 'Current Version'
            info_table.cell(2, 1).text = current_version
            
            # Patch Status
            fix_available = row.get('Fix Available', 'N/A')
            patch_status = 'Patch Available' if fix_available == 'YES' else 'No Patch Available' if fix_available == 'NO' else 'Unknown Status'
            info_table.cell(3, 0).text = 'Patch Status'
            info_table.cell(3, 1).text = patch_status
            
            # Fixed Version
            fixed_version = str(row.get('Fixed in Version', 'N/A'))
            info_table.cell(4, 0).text = 'Fixed Version'
            info_table.cell(4, 1).text = fixed_version if fixed_version != 'nan' and fixed_version != '-' else 'Not Available'
            
            # Remediation
            remediation_cmd = str(row.get('Package Remediation', ''))
            if fix_available == 'YES':
                if remediation_cmd and remediation_cmd != 'nan' and remediation_cmd != '-':
                    remedy_text = remediation_cmd
                else:
                    remedy_text = 'Update package to the fixed version'
            else:
                remedy_text = 'Wait for vendor patch or apply workaround. Check reference URLs for additional information'
            
            info_table.cell(5, 0).text = 'Remediation'
            info_table.cell(5, 1).text = remedy_text
            
            # Make table headers bold and update font
            for i in range(6):
                for paragraph in info_table.cell(i, 0).paragraphs:
                    for run in paragraph.runs:
                        run.bold = True
            
            # Update table font
            update_table_content_font(info_table, 'TH SarabunPSK', 11)
            
            # Vulnerability Description
            description = str(row.get('Description', ''))
            if description and description != 'nan' and description != '-' and len(description) > 10:
                desc_para = doc.add_paragraph()
                desc_run1 = desc_para.add_run('Description: ')
                desc_run1.bold = True
                desc_run2 = desc_para.add_run(description[:300] + '...' if len(description) > 300 else description)
                set_thai_font(desc_para, 'TH SarabunPSK', 11)
            
            # Risk Score
            score = str(row.get('Inspector Score', ''))
            if score and score != 'nan' and score != '-':
                score_para = doc.add_paragraph()
                score_run1 = score_para.add_run('Risk Score: ')
                score_run1.bold = True
                score_run2 = score_para.add_run(f'{score}/10')
                set_thai_font(score_para, 'TH SarabunPSK', 11)
            
            # Reference URLs
            ref_urls = str(row.get('Reference Urls', ''))
            if ref_urls and ref_urls != 'nan' and ref_urls != '-':
                ref_para = doc.add_paragraph()
                ref_run1 = ref_para.add_run('References: ')
                ref_run1.bold = True
                urls = ref_urls.split(', ')[:3]  # Show first 3 URLs only
                ref_run2 = ref_para.add_run(', '.join(urls))
                set_thai_font(ref_para, 'TH SarabunPSK', 10)
            
            # Add spacing between vulnerabilities
            doc.add_paragraph('')
        
        # Add spacing between severity levels
        doc.add_paragraph('')
    
    # Add note
    doc.add_paragraph()
    note_para = doc.add_paragraph()
    note_run1 = note_para.add_run('Note: ')
    note_run1.bold = True
    note_run2 = note_para.add_run('Prioritize remediation by severity level (CRITICAL > HIGH > MEDIUM > LOW) and focus on vulnerabilities with available patches first.')
    set_thai_font(note_para, 'TH SarabunPSK', 12)
    
    # Modern Footer
    doc.add_page_break()  # Ensure footer is on clean space
    
    footer_table = doc.add_table(rows=3, cols=1)
    footer_table.style = 'Table Grid'
    
    # Main footer
    footer_cell = footer_table.cell(0, 0)
    footer_p = footer_cell.paragraphs[0]
    footer_p.text = 'CYBERSECURITY ASSESSMENT REPORT'
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in footer_p.runs:
        run.bold = True
        run.font.color.rgb = RGBColor(41, 128, 185)
        run.font.size = Pt(14)
    
    # Generation info
    gen_cell = footer_table.cell(1, 0)
    gen_p = gen_cell.paragraphs[0]
    gen_p.text = f'Generated on {datetime.datetime.now().strftime("%B %d, %Y")} | Automated Security Analysis'
    gen_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Confidentiality notice
    conf_cell = footer_table.cell(2, 0)
    conf_p = conf_cell.paragraphs[0]
    conf_p.text = 'CONFIDENTIAL - For Executive Review Only'
    conf_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in conf_p.runs:
        run.bold = True
        run.font.color.rgb = RGBColor(231, 76, 60)
    
    # Style footer table
    for row in footer_table.rows:
        for cell in row.cells:
            shading_elm = OxmlElement('w:shd')
            shading_elm.set(qn('w:fill'), 'F8F9FA')
            cell._tc.get_or_add_tcPr().append(shading_elm)
    
    update_table_content_font(footer_table, 'TH SarabunPSK', 10)
    footer_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # บันทึกไฟล์
    doc.save(OUTPUT_FILE_DOCX)

def generate_report():
    try:
        # 1. อ่านข้อมูลจาก CSV
        print(f"กำลังอ่านไฟล์ {INPUT_FILE}...")
        df = pd.read_csv(INPUT_FILE)

        # แปลงวันที่ให้เป็น format ที่อ่านง่าย
        if 'Last Updated' in df.columns:
            df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

        # 2. คำนวณสถิติเบื้องต้น
        total_findings = len(df)
        severity_counts = df['Severity'].value_counts().reindex(['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL'], fill_value=0)
        
        # แยกตาม Fix Available
        fix_available_counts = df['Fix Available'].value_counts()
        
        # หา Resource ที่มีปัญหาเยอะที่สุด (Top 5)
        # พยายามใช้ Resource Name ถ้ามี (Resource Tags) ถ้าไม่มีใช้ Resource ID
        def get_resource_name(row):
            tags = str(row.get('Resource Tags', ''))
            if 'Name:' in tags:
                try:
                    return tags.split('Name:')[1].split(',')[0]
                except:
                    return row.get('Resource ID', 'Unknown')
            return row.get('Resource ID', 'Unknown')

        df['Display_Name'] = df.apply(get_resource_name, axis=1)
        top_resources = df['Display_Name'].value_counts().head(5)

        # หา Top CVE
        top_cves = df['Title'].value_counts().head(5)

        # Action Items (Critical/High & Fix Available) - moved here for both functions
        urgent_fixes = df[
            (df['Severity'].isin(['CRITICAL', 'HIGH'])) & 
            (df['Fix Available'] == 'YES')
        ].head(10) # แสดงแค่ 10 รายการแรกเพื่อไม่ให้ยาวเกินไป

        # 3. สร้างไฟล์ Word Document
        generate_docx_report(total_findings, severity_counts, fix_available_counts, top_resources, top_cves, urgent_fixes, df)

        # 4. เริ่มเขียนลงไฟล์ Markdown
        print(f"กำลังสร้างรายงาน {OUTPUT_FILE_MD}...")
        with open(OUTPUT_FILE_MD, 'w', encoding='utf-8') as f:
            # Header
            f.write(f"# รายงานสรุปผลการตรวจสอบช่องโหว่ (Vulnerability Assessment Report)\n")
            f.write(f"**วันที่ออกรายงาน:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**ไฟล์ข้อมูลต้นฉบับ:** {INPUT_FILE}\n\n")
            f.write(f"---\n\n")

            # Executive Summary
            f.write(f"## 1. บทสรุปผู้บริหาร (Executive Summary)\n\n")
            f.write(f"จากการตรวจสอบข้อมูล VA Scan พบช่องโหว่ทั้งหมด **{total_findings:,}** รายการ โดยมีรายละเอียดความเสี่ยงดังนี้:\n\n")
            
            # Severity Table
            f.write(f"| ระดับความรุนแรง (Severity) | จำนวนที่พบ (Count) | สัดส่วน (%) |\n")
            f.write(f"| :--- | :---: | :---: |\n")
            for severity, count in severity_counts.items():
                if count > 0:
                    percent = (count / total_findings) * 100
                    icon = "🔴" if severity in ['CRITICAL', 'HIGH'] else "🟠" if severity == 'MEDIUM' else "🔵"
                    f.write(f"| {icon} {severity} | {count:,} | {percent:.1f}% |\n")
            f.write(f"\n")

            # Fix Available Summary
            f.write(f"### สถานะการแก้ไข (Remediation Status)\n")
            yes_fix = fix_available_counts.get('YES', 0)
            f.write(f"- ✅ มีแพตช์แก้ไขแล้ว (Fix Available): **{yes_fix:,}** รายการ\n")
            f.write(f"- ⚠️ ยังไม่มีแพตช์ (No Fix): **{fix_available_counts.get('NO', 0):,}** รายการ\n\n")

            # Top Resources
            f.write(f"## 2. ทรัพยากรที่มีความเสี่ยงสูงสุด (Top 5 Vulnerable Resources)\n\n")
            f.write(f"เครื่องคอมพิวเตอร์หรืออินสแตนซ์ที่พบช่องโหว่จำนวนมากที่สุด:\n\n")
            f.write(f"| ชื่อ Resource / ID | จำนวนช่องโหว่ |\n")
            f.write(f"| :--- | :---: |\n")
            for name, count in top_resources.items():
                f.write(f"| **{name}** | {count} |\n")
            f.write(f"\n")

            # Top Vulnerabilities
            f.write(f"## 3. ช่องโหว่ที่พบบ่อยที่สุด (Top 5 Common Vulnerabilities)\n\n")
            f.write(f"| CVE / Title | จำนวนที่พบ |\n")
            f.write(f"| :--- | :---: |\n")
            for title, count in top_cves.items():
                # ตัดคำถ้ายาวเกินไป
                short_title = (title[:70] + '..') if len(title) > 70 else title
                f.write(f"| {short_title} | {count} |\n")
            f.write(f"\n")

            # Action Items (Critical/High & Fix Available)
            f.write(f"## 4. สิ่งที่ต้องดำเนินการเร่งด่วน (Immediate Action Items)\n\n")
            f.write(f"รายการช่องโหว่ระดับ **CRITICAL** หรือ **HIGH** ที่ **มีแพตช์แก้ไขแล้ว** (แนะนำให้แก้ไขทันที):\n\n")

            if not urgent_fixes.empty:
                f.write(f"| Resource | Severity | CVE | Package / Component | Fixed Version |\n")
                f.write(f"| :--- | :---: | :--- | :--- | :--- |\n")
                for _, row in urgent_fixes.iterrows():
                    res_name = get_resource_name(row)
                    cve = row['Title'].split(' ')[0] if ' ' in row['Title'] else row['Title']
                    pkg = row.get('Affected Packages', '-')
                    fixed_ver = row.get('Fixed in Version', '-')
                    f.write(f"| {res_name} | **{row['Severity']}** | {cve} | {pkg} | {fixed_ver} |\n")
                f.write(f"\n*(แสดงรายการสูงสุด 10 อันดับแรก)*\n")
            else:
                f.write(f"> ไม่พบรายการ Critical/High ที่มีแพตช์แก้ไขในขณะนี้ หรือข้อมูลไม่เพียงพอ\n")
            
            f.write(f"\n---\n")
            f.write(f"*Generated by AI Assistant*")

        print(f"เสร็จสิ้น! บันทึกไฟล์เรียบร้อยแล้วที่: {OUTPUT_FILE_MD} และ {OUTPUT_FILE_DOCX}")

    except FileNotFoundError:
        print(f"Error: ไม่พบไฟล์ {INPUT_FILE} กรุณาตรวจสอบว่าไฟล์อยู่ในโฟลเดอร์เดียวกัน")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_report()
