# Biodiversity App Backend (FastAPI)

A FastAPI-based REST API for biodiversity tracking that allows users to log species observations with photos, location data, and structured questionnaires.

# 🚀 Features

JWT Authentication : Secure user registration & login
Role-Based Access : Admin privileges for managing data
Species Management : Add/edit species records
Dynamic Questionnaire : Configurable question types (multiple choice, text, number, yes/no)
Photo Uploads : Optional image attachments for observations
Location Tracking : GPS coordinates + location name
Answer Storage : Structured responses to predefined questions
CSV Export : Admin-only export of all observation data
Interactive Docs : Swagger UI at /docs and ReDoc at /redoc

## Installation & Setup

### 1. Clone and Setup Environment

```bash
# Create project directory
mkdir biodiversity_backend
cd biodiversity_backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file with your configuration:

```bash
SECRET_KEY=your-super-secret-key-change-this-in-production
JWT_SECRET_KEY=your-jwt-secret-key-change-this-too
DATABASE_URL=sqlite:///biodiversity.db
UPLOAD_FOLDER=uploads
ALLOWED_EXTENSIONS=png,jpg,jpeg,gif
```

### 3. Initialize Database

```bash
# Run the application (this will create tables and seed data)
python app.py
```



**⚠️ Important**: Change the admin password after first login in production!

## 🌐 API Endpoints

📋 Authentication
POST /register - Create user (admin requires secret)
POST /login - Get JWT token
GET /profile - View current user
GET /stats - Observation stats

🐦 Species Management
GET /species - Get all species
POST /species - Create new species (admin only)

❓ Question Management
GET /questions - List all questions
POST /questions - Create new question (admin only)

📝 Observation Logs
POST /species-logs - Submit observation with answers
GET /species-logs - View user's logs
GET /species-logs/{log_id} - View specific log

👤 Admin Dashboard
GET /admin/users - List all users
GET /admin/all-logs - View all observations
GET /admin/export-csv - Download CSV export



## File Upload Configuration

- **Max file size**: 16MB
- **Allowed formats**: PNG, JPG, JPEG, GIF
- **Upload directory**: `uploads/`
- **File naming**: UUID-based unique filenames

## Sample Questions Included

1. Specimen size (multiple choice)
2. Primary color (multiple choice)
3. Habitat type (multiple choice)
4. Weather conditions (multiple choice)
5. Number of specimens (number input)
6. Activity level (multiple choice)
7. Additional observations (text)
8. Common in area (yes/no)
9. Time of observation (multiple choice)
10. Observation quality rating (multiple choice)

## Security Features

- Password hashing with bcrypt
- JWT token authentication
- File upload validation
- Input sanitization
- Admin role-based access control

## Production Deployment Notes

1. **Change default secrets** in `.env` file
2. **Use PostgreSQL** instead of SQLite for production
3. **Configure proper CORS** settings
4. **Set up SSL/HTTPS** for secure token transmission
5. **Implement rate limiting** for API endpoints
6. **Set up proper logging** and monitoring
7. **Configure file storage** (AWS S3, etc.) for scalability

## Development

```bash
# Run in development mode
python app.py

# The server will start on http://localhost:5000
```

## Testing the API

You can test the API using tools like:
- **Postman** - Import the endpoints and test interactively
- **curl** - Command line testing (examples above)
- **Thunder Client** (VS Code extension)
- **Insomnia** REST client

## Support

For issues or questions:
1. Check the API endpoint documentation above
2. Verify JWT token authentication
3. Ensure proper request formatting
4. Check server logs for detailed error information