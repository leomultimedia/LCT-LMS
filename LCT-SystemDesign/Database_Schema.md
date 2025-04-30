# LCT Learning Management System - Database Schema

<div align="center">
  <img src="https://raw.githubusercontent.com/leomultimedia/LCT-LMS/main/assets/logo.png" alt="Lear Cyber Tech Logo" width="200"/>
</div>

[🏠 Home](../README.md) > [System Design Documentation](README.md) > Database Schema

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

---


# Database Schema Documentation

## Relational Database (PostgreSQL)

### 1. Tenant Management
```sql
CREATE TABLE tenants (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255) UNIQUE NOT NULL,
    logo_url VARCHAR(255),
    theme_config JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tenant_settings (
    tenant_id UUID REFERENCES tenants(id),
    setting_key VARCHAR(255) NOT NULL,
    setting_value JSONB NOT NULL,
    PRIMARY KEY (tenant_id, setting_key)
);
```

### 2. User Management
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenants(id),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    profile_picture_url VARCHAR(255),
    role VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_profiles (
    user_id UUID REFERENCES users(id),
    bio TEXT,
    skills JSONB,
    preferences JSONB,
    PRIMARY KEY (user_id)
);

CREATE TABLE user_sessions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    token VARCHAR(255) NOT NULL,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Course Management
```sql
CREATE TABLE courses (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenants(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    level VARCHAR(50),
    duration INTEGER,
    status VARCHAR(50) NOT NULL,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE learning_paths (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenants(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    courses JSONB,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE course_content (
    id UUID PRIMARY KEY,
    course_id UUID REFERENCES courses(id),
    title VARCHAR(255) NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    content_url VARCHAR(255),
    content_text TEXT,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Progress Tracking
```sql
CREATE TABLE enrollments (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    course_id UUID REFERENCES courses(id),
    status VARCHAR(50) NOT NULL,
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE progress (
    id UUID PRIMARY KEY,
    enrollment_id UUID REFERENCES enrollments(id),
    content_id UUID REFERENCES course_content(id),
    status VARCHAR(50) NOT NULL,
    progress_percentage INTEGER,
    last_accessed TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### 5. Gamification
```sql
CREATE TABLE points (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    points INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE achievements (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    points_value INTEGER NOT NULL,
    badge_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_achievements (
    user_id UUID REFERENCES users(id),
    achievement_id UUID REFERENCES achievements(id),
    earned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, achievement_id)
);
```

### 6. Video Conferencing
```sql
CREATE TABLE sessions (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenants(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(50) NOT NULL,
    recording_url VARCHAR(255),
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE session_participants (
    session_id UUID REFERENCES sessions(id),
    user_id UUID REFERENCES users(id),
    role VARCHAR(50) NOT NULL,
    joined_at TIMESTAMP WITH TIME ZONE,
    left_at TIMESTAMP WITH TIME ZONE,
    PRIMARY KEY (session_id, user_id)
);
```

### 7. Certificates
```sql
CREATE TABLE certificates (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    course_id UUID REFERENCES courses(id),
    certificate_number VARCHAR(255) UNIQUE NOT NULL,
    issue_date TIMESTAMP WITH TIME ZONE NOT NULL,
    expiry_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE certificate_templates (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenants(id),
    name VARCHAR(255) NOT NULL,
    template_html TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## NoSQL Database (MongoDB)

### 1. Content Metadata
```javascript
{
  contentId: String,
  tenantId: String,
  type: String,
  metadata: {
    duration: Number,
    format: String,
    size: Number,
    resolution: String,
    tags: [String],
    language: String
  },
  analytics: {
    views: Number,
    averageRating: Number,
    completionRate: Number
  },
  createdAt: Date,
  updatedAt: Date
}
```

### 2. Session Recordings
```javascript
{
  sessionId: String,
  tenantId: String,
  recording: {
    url: String,
    duration: Number,
    size: Number,
    format: String,
    quality: String
  },
  participants: [{
    userId: String,
    joinTime: Date,
    leaveTime: Date,
    role: String
  }],
  events: [{
    timestamp: Date,
    type: String,
    data: Object
  }],
  createdAt: Date
}
```

### 3. Analytics Data
```javascript
{
  userId: String,
  tenantId: String,
  metrics: {
    coursesCompleted: Number,
    totalTimeSpent: Number,
    averageScore: Number,
    lastActive: Date
  },
  learningPatterns: {
    preferredTime: String,
    preferredContentType: String,
    completionRate: Number
  },
  recommendations: [{
    type: String,
    contentId: String,
    score: Number,
    timestamp: Date
  }],
  updatedAt: Date
}
```

## Cache Layer (Redis)

### Key Patterns
1. Session Management
   - `session:{sessionId}` - Session data
   - `user:{userId}:sessions` - User's active sessions

2. Content Caching
   - `content:{contentId}` - Course content
   - `course:{courseId}:metadata` - Course metadata

3. User Data
   - `user:{userId}:profile` - User profile
   - `user:{userId}:progress` - User progress
   - `user:{userId}:points` - User points and level

4. System Configuration
   - `tenant:{tenantId}:settings` - Tenant settings
   - `system:config` - System-wide configuration

### Cache Expiration
- Session data: 24 hours
- Content data: 1 hour
- User data: 30 minutes
- System configuration: 1 day 