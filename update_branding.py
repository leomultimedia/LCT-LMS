import os
import re

# Branding template
BRANDING_TEMPLATE = """# LCT Learning Management System - {title}

<div align="center">
  <img src="https://raw.githubusercontent.com/leomultimedia/LCT-LMS/main/assets/logo.png" alt="Lear Cyber Tech Logo" width="200"/>
</div>

[🏠 Home](../README.md) > [System Design Documentation](README.md) > {title}

[← Back to Main Documentation](../README.md)

## Company Information
- **Company**: [Lear Cyber Tech](https://www.linkedin.com/company/leartech/)
- **Author**: [Dr. Libin Pallikunnel Kurian](https://www.linkedin.com/in/dr-libin-pallikunnel-kurian-88741530/)
- **GitHub**: [leomultimedia](https://github.com/leomultimedia)
- **Position**: Principal Consultant - ICT & Cyber Security
- **Expertise**: Cloud Digital Leader | Ethical Hacker | OT | IoT | ICS/SCADA | IT Audit | RPA | AI | ML | Analytics

## Company Vision & Mission
- **Vision**: To be a global leader in cybersecurity and technology solutions, empowering organizations with innovative and secure digital transformation.
- **Mission**: To provide cutting-edge cybersecurity solutions and technology services that protect and enhance our clients' digital assets while fostering a culture of continuous learning and innovation.

## Core Values
1. **Integrity**: Upholding the highest standards of ethical conduct and transparency
2. **Customer Focus**: Delivering exceptional value and service to our clients
3. **Innovation**: Driving technological advancement and creative solutions
4. **Teamwork**: Fostering collaboration and mutual respect
5. **Excellence**: Striving for the highest quality in all our endeavors

"""

def get_title_from_filename(filename):
    """Extract title from filename."""
    base_name = os.path.splitext(filename)[0]
    return base_name.replace('_', ' ').title()

def update_file_branding(file_path):
    """Update branding in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the original title
    title_match = re.match(r'# LCT Learning Management System - (.*?)\n', content)
    if not title_match:
        return
    
    title = title_match.group(1)
    
    # Create new content with branding template
    new_content = BRANDING_TEMPLATE.format(title=title)
    
    # Find the first section after the branding
    sections = content.split('---')
    if len(sections) > 1:
        new_content += '---\n' + sections[1]
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    # Process all markdown files in the LCT-SystemDesign directory
    system_design_dir = 'LCT-SystemDesign'
    for filename in os.listdir(system_design_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(system_design_dir, filename)
            print(f"Updating branding in {filename}...")
            update_file_branding(file_path)
    
    # Update the main README.md
    print("Updating branding in README.md...")
    update_file_branding('README.md')

if __name__ == '__main__':
    main() 