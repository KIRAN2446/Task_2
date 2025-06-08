import pandas as pd
from fpdf import FPDF

# Read CSV file
data = pd.read_csv('data.csv')

# Analyze data
average_score = data['Score'].mean()
max_score = data['Score'].max()
min_score = data['Score'].min()
total_entries = len(data)

# Prepare PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Automated Report: Student Scores', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add summary
pdf.cell(0, 10, f'Total entries: {total_entries}', ln=1)
pdf.cell(0, 10, f'Average Score: {average_score:.2f}', ln=1)
pdf.cell(0, 10, f'Max Score: {max_score}', ln=1)
pdf.cell(0, 10, f'Min Score: {min_score}', ln=1)
pdf.ln(10)

# Add table header
pdf.set_font("Arial", 'B', 12)
pdf.cell(50, 10, "Name", 1)
pdf.cell(50, 10, "Subject", 1)
pdf.cell(30, 10, "Score", 1)
pdf.ln()

# Add table rows
pdf.set_font("Arial", size=12)
for i, row in data.iterrows():
    pdf.cell(50, 10, row['Name'], 1)
    pdf.cell(50, 10, row['Subject'], 1)
    pdf.cell(30, 10, str(row['Score']), 1)
    pdf.ln()

# Save PDF
pdf.output("student_score_report.pdf")
print("✅ Report generated as 'student_score_report.pdf'")
