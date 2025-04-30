# LCT Learning Management System (LMS)

<div align="center">
  <img src="https://raw.githubusercontent.com/leomultimedia/LCT-LMS/main/assets/logo.png" alt="Lear Cyber Tech Logo" width="200"/>
</div>

[🏠 Home](README.md)

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

A comprehensive Learning Management System designed for LCT, featuring a modern web frontend, mobile application, and robust backend services.

## Project Structure

```
LCT-LMS/
├── frontend/           # React/Next.js frontend application
├── mobile/            # React Native mobile application
├── backend/           # Python FastAPI backend services
└── docs/             # Project documentation
```

## Documentation

- [System Design Documentation](LCT-SystemDesign/README.md)
- [System Architecture Diagrams](LCT-SystemDesign/System_Architecture_Diagrams.md)
- [Frontend Architecture](LCT-SystemDesign/Frontend_Architecture.md)

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.9+
- Docker (optional)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-org/LCT-LMS.git
cd LCT-LMS
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Development

1. Start the frontend development server:
```bash
cd frontend
npm run dev
```

2. Start the backend development server:
```bash
cd backend
uvicorn main:app --reload
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
