# LCT Learning Management System (LMS)

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
