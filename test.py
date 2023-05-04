import subprocess

def convert_html_to_pdf(html_file, output_pdf):
    subprocess.call(['wkhtmltopdf', html_file, output_pdf])

# Replace 'input.html' with the path to your HTML file
# Replace 'output.pdf' with the desired output PDF file path
convert_html_to_pdf('flaskblog/templates/recapProject.html', 'output.pdf')
