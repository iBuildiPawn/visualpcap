# VisualPCAP

A web-based packet capture analysis tool designed for security analysts and network administrators. VisualPCAP transforms complex PCAP files into intuitive visualizations and actionable security insights.

## Features

- Secure PCAP file upload and management
- Automated packet analysis and protocol breakdown
- Interactive visualizations of network traffic
- Security analysis tools for threat detection
- Customizable reporting system

## Tech Stack

- **Frontend**: React.js, Material-UI, D3.js
- **Backend**: Python FastAPI
- **Database**: PostgreSQL
- **Cache**: Redis
- **Container**: Docker

## Prerequisites

- Docker and Docker Compose
- Git

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd visualpcap
   ```

2. Create a .env file in the root directory:
   ```bash
   cp .env.example .env
   ```

3. Start the application:
   ```bash
   docker-compose up -d
   ```

4. Access the application:
   - Frontend: http://localhost:3000
   - API Documentation: http://localhost:8000/docs

## Development Setup

1. Frontend Development:
   ```bash
   cd frontend
   npm install
   npm start
   ```

2. Backend Development:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

## Project Structure

```
visualpcap/
├── frontend/           # React frontend application
├── backend/           # FastAPI backend application
│   ├── app/          # Application code
│   └── tests/        # Test files
├── database/         # Database initialization scripts
├── config/           # Configuration files
└── docker-compose.yml
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
