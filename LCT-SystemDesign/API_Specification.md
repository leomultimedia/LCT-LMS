# API Specification

## Base URL
```
https://api.lms.example.com/v1
```

## Authentication
All API requests require authentication using JWT tokens.

### Headers
```
Authorization: Bearer <token>
X-Tenant-ID: <tenant_id>
```

## API Endpoints

### 1. Authentication

#### POST /auth/register
Register a new user.

Request:
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "firstName": "John",
  "lastName": "Doe",
  "role": "student"
}
```

Response:
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "role": "student",
  "status": "active"
}
```

#### POST /auth/login
Authenticate a user.

Request:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

Response:
```json
{
  "token": "jwt_token",
  "expiresIn": 3600,
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "firstName": "John",
    "lastName": "Doe",
    "role": "student"
  }
}
```

### 2. User Management

#### GET /users/profile
Get user profile.

Response:
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "profilePicture": "url",
  "bio": "User bio",
  "skills": ["skill1", "skill2"],
  "preferences": {
    "notifications": true,
    "language": "en"
  }
}
```

#### PUT /users/profile
Update user profile.

Request:
```json
{
  "firstName": "John",
  "lastName": "Doe",
  "bio": "Updated bio",
  "skills": ["skill1", "skill2", "skill3"]
}
```

### 3. Course Management

#### GET /courses
List all courses.

Query Parameters:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10)
- `category`: Filter by category
- `level`: Filter by level

Response:
```json
{
  "total": 100,
  "page": 1,
  "limit": 10,
  "courses": [
    {
      "id": "uuid",
      "title": "Course Title",
      "description": "Course description",
      "category": "Programming",
      "level": "Beginner",
      "duration": 120,
      "status": "published"
    }
  ]
}
```

#### POST /courses
Create a new course.

Request:
```json
{
  "title": "Course Title",
  "description": "Course description",
  "category": "Programming",
  "level": "Beginner",
  "duration": 120
}
```

#### GET /courses/{courseId}
Get course details.

Response:
```json
{
  "id": "uuid",
  "title": "Course Title",
  "description": "Course description",
  "category": "Programming",
  "level": "Beginner",
  "duration": 120,
  "content": [
    {
      "id": "uuid",
      "title": "Module 1",
      "type": "video",
      "duration": 30,
      "order": 1
    }
  ]
}
```

### 4. Learning Paths

#### GET /learning-paths
List all learning paths.

Response:
```json
{
  "total": 20,
  "paths": [
    {
      "id": "uuid",
      "title": "Full Stack Development",
      "description": "Path description",
      "courses": [
        {
          "id": "uuid",
          "title": "Course 1",
          "order": 1
        }
      ]
    }
  ]
}
```

### 5. Progress Tracking

#### GET /progress
Get user's learning progress.

Response:
```json
{
  "enrolledCourses": [
    {
      "courseId": "uuid",
      "title": "Course Title",
      "progress": 75,
      "lastAccessed": "2024-03-20T10:00:00Z"
    }
  ],
  "completedCourses": 5,
  "totalTimeSpent": 3600
}
```

#### POST /progress/{courseId}/content/{contentId}
Update content progress.

Request:
```json
{
  "status": "completed",
  "progress": 100
}
```

### 6. Video Conferencing

#### POST /sessions
Create a new session.

Request:
```json
{
  "title": "Session Title",
  "description": "Session description",
  "startTime": "2024-03-20T10:00:00Z",
  "endTime": "2024-03-20T11:00:00Z",
  "participants": ["user1", "user2"]
}
```

#### GET /sessions/{sessionId}
Get session details.

Response:
```json
{
  "id": "uuid",
  "title": "Session Title",
  "description": "Session description",
  "startTime": "2024-03-20T10:00:00Z",
  "endTime": "2024-03-20T11:00:00Z",
  "status": "scheduled",
  "participants": [
    {
      "userId": "uuid",
      "name": "John Doe",
      "role": "instructor"
    }
  ]
}
```

### 7. Gamification

#### GET /gamification/points
Get user's points and level.

Response:
```json
{
  "points": 1000,
  "level": 5,
  "nextLevelPoints": 1500,
  "achievements": [
    {
      "id": "uuid",
      "name": "First Course",
      "description": "Completed first course",
      "badgeUrl": "url"
    }
  ]
}
```

### 8. Certificates

#### GET /certificates
List user's certificates.

Response:
```json
{
  "certificates": [
    {
      "id": "uuid",
      "courseId": "uuid",
      "courseTitle": "Course Title",
      "issueDate": "2024-03-20",
      "expiryDate": "2025-03-20",
      "certificateNumber": "CERT-12345",
      "downloadUrl": "url"
    }
  ]
}
```

### 9. AI Integration

#### GET /ai/recommendations
Get personalized recommendations.

Response:
```json
{
  "recommendations": [
    {
      "type": "course",
      "id": "uuid",
      "title": "Recommended Course",
      "score": 0.95,
      "reason": "Based on your learning history"
    }
  ]
}
```

#### POST /ai/chat
Interact with AI assistant.

Request:
```json
{
  "message": "What should I learn next?",
  "context": {
    "currentCourse": "uuid",
    "completedCourses": ["uuid1", "uuid2"]
  }
}
```

Response:
```json
{
  "response": "Based on your progress, I recommend...",
  "suggestions": [
    {
      "type": "course",
      "id": "uuid",
      "title": "Suggested Course"
    }
  ]
}
```

## Error Responses

### 400 Bad Request
```json
{
  "error": "Bad Request",
  "message": "Invalid input data",
  "details": {
    "field": "error message"
  }
}
```

### 401 Unauthorized
```json
{
  "error": "Unauthorized",
  "message": "Invalid or expired token"
}
```

### 403 Forbidden
```json
{
  "error": "Forbidden",
  "message": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "error": "Not Found",
  "message": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```

## Rate Limiting
- 100 requests per minute per user
- 1000 requests per minute per tenant
- Headers included in response:
  ```
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 95
  X-RateLimit-Reset: 1620000000
  ``` 