# Biodiversity App Backend

A Flask-based REST API for a biodiversity tracking application that allows users to log species observations with photos and detailed questionnaires.

## Features

- **User Authentication**: Registration, login with JWT tokens
- **Species Management**: CRUD operations for species data
- **Dynamic Questionnaire**: Configurable questions for species observations
- **Photo Uploads**: Optional photo attachments for observations
- **Location Tracking**: GPS coordinates and location names
- **User History**: Personal observation history for users
- **Admin Dashboard**: Admin can view all data and export to CSV
- **Data Export**: CSV export functionality for research purposes

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
FLASK_ENV=development
FLASK_DEBUG=True
```

### 3. Initialize Database

```bash
# Run the application (this will create tables and seed data)
python app.py
```

### 4. Default Admin Account

- **Username**: admin
- **Email**: admin@biodiversity.com
- **Password**: admin123

**⚠️ Important**: Change the admin password after first login in production!

## API Endpoints

### Authentication
- `POST /api/register` - User registration
- `POST /api/login` - User login

### Species Management
- `GET /api/species` - Get all species (authenticated)
- `POST /api/species` - Create new species (admin only)

### Questions
- `GET /api/questions` - Get all questions (authenticated)
- `POST /api/questions` - Create new question (admin only)

### Species Observations
- `POST /api/species-logs` - Create new observation log
- `GET /api/species-logs` - Get user's observation history
- `GET /api/species-logs/<id>` - Get specific observation details

### Admin Routes
- `GET /api/admin/all-logs` - Get all observations (admin only)
- `GET /api/admin/export-csv` - Export data to CSV (admin only)
- `GET /api/admin/users` - Get all users (admin only)

### Utility
- `GET /api/profile` - Get current user profile
- `GET /api/stats` - Get user statistics
- `GET /api/uploads/<filename>` - Serve uploaded images

## API Usage Examples

### 1. User Registration

```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "naturelover",
    "email": "user@example.com",
    "password": "securepassword"
  }'
```

### 2. User Login

```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "naturelover",
    "password": "securepassword"
  }'
```

### 3. Create Species Observation

```bash
curl -X POST http://localhost:5000/api/species-logs \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "species_id=1" \
  -F "location_latitude=40.7128" \
  -F "location_longitude=-74.0060" \
  -F "location_name=Central Park, NYC" \
  -F "notes=Beautiful robin spotted in the morning" \
  -F "photo=@path/to/image.jpg" \
  -F 'answers=[
    {"question_id": 1, "answer_text": "Small (5-20cm)"},
    {"question_id": 2, "answer_text": "Red"},
    {"question_id": 5, "answer_text": "1"}
  ]'
```

### 4. Get User's Observation History

```bash
curl -X GET http://localhost:5000/api/species-logs \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 5. Admin: Export Data to CSV

```bash
curl -X GET http://localhost:5000/api/admin/export-csv \
  -H "Authorization: Bearer ADMIN_JWT_TOKEN" \
  --output biodiversity_data.csv
```

## Database Schema

### Users Table
- id, username, email, password_hash, is_admin, created_at

### Species Table
- id, name, scientific_name, category, description, created_at

### Questions Table
- id, question_text, question_type, options, is_required, order_index, created_at

### Species_Logs Table
- id, user_id, species_id, location_latitude, location_longitude, location_name, photo_path, notes, created_at

### Answers Table
- id, species_log_id, question_id, answer_text, created_at

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