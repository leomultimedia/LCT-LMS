# LCT Learning Management System - Frontend Architecture

<div align="center">
  <img src="https://raw.githubusercontent.com/leomultimedia/LCT-LMS/main/assets/logo.png" alt="Lear Cyber Tech Logo" width="200"/>
</div>

[🏠 Home](../README.md) > [System Design Documentation](README.md) > Frontend Architecture

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


## Technology Stack

### Core Technologies
- React 18+ with TypeScript
- Next.js 14+ for server-side rendering and API routes
- Tailwind CSS for styling
- Redux Toolkit for state management
- React Query for data fetching and caching
- React Router for navigation
- Jest and React Testing Library for testing

### UI Component Libraries
- Headless UI for accessible components
- React Hook Form for form management
- React Icons for iconography
- React Toastify for notifications
- React Player for video content
- React PDF for document viewing

## Architecture Overview

### 1. Project Structure
```
src/
├── app/                    # Next.js app directory
├── components/            # Reusable components
│   ├── common/           # Shared components
│   ├── layout/           # Layout components
│   ├── course/           # Course-related components
│   ├── user/             # User-related components
│   └── admin/            # Admin-specific components
├── features/             # Feature-based modules
│   ├── auth/             # Authentication
│   ├── courses/          # Course management
│   ├── learning/         # Learning experience
│   ├── video/            # Video conferencing
│   └── gamification/     # Gamification features
├── hooks/                # Custom React hooks
├── services/             # API services
├── store/                # Redux store
├── types/                # TypeScript types
├── utils/                # Utility functions
└── styles/               # Global styles
```

### 2. State Management

#### Redux Store Structure
```typescript
interface RootState {
  auth: {
    user: User | null;
    token: string | null;
    loading: boolean;
    error: string | null;
  };
  courses: {
    list: Course[];
    current: Course | null;
    loading: boolean;
    error: string | null;
  };
  progress: {
    current: Progress | null;
    history: Progress[];
    loading: boolean;
  };
  ui: {
    theme: 'light' | 'dark';
    sidebarOpen: boolean;
    notifications: Notification[];
  };
}
```

#### API State Management
```typescript
// Using React Query for API state
const { data, isLoading, error } = useQuery({
  queryKey: ['courses'],
  queryFn: fetchCourses,
  staleTime: 5 * 60 * 1000, // 5 minutes
  cacheTime: 30 * 60 * 1000, // 30 minutes
});
```

### 3. Component Architecture

#### Atomic Design Pattern
1. Atoms
   - Buttons
   - Inputs
   - Icons
   - Typography

2. Molecules
   - Form groups
   - Cards
   - Navigation items
   - Search bars

3. Organisms
   - Headers
   - Sidebars
   - Course cards
   - Progress trackers

4. Templates
   - Dashboard layout
   - Course layout
   - Admin layout
   - Authentication layout

5. Pages
   - Home
   - Course details
   - Learning path
   - User profile

### 4. Performance Optimization

#### Code Splitting
```typescript
// Dynamic imports for large components
const VideoPlayer = dynamic(() => import('@/components/video/VideoPlayer'), {
  loading: () => <LoadingSpinner />,
  ssr: false
});
```

#### Image Optimization
```typescript
// Next.js Image component
<Image
  src={imageUrl}
  alt="Course thumbnail"
  width={400}
  height={225}
  priority={true}
  loading="lazy"
/>
```

#### Caching Strategies
1. Service Worker
   - Offline support
   - Asset caching
   - API response caching

2. Browser Storage
   - Local storage for user preferences
   - Session storage for temporary data
   - IndexedDB for larger datasets

### 5. Accessibility

#### ARIA Implementation
```typescript
// Accessible components
const AccessibleButton = ({ children, ...props }) => (
  <button
    role="button"
    aria-label={props['aria-label']}
    {...props}
  >
    {children}
  </button>
);
```

#### Keyboard Navigation
- Focus management
- Tab order
- Keyboard shortcuts
- Skip links

### 6. Internationalization

#### i18n Setup
```typescript
// Language configuration
const i18n = {
  locales: ['en', 'es', 'fr', 'de'],
  defaultLocale: 'en',
  messages: {
    en: require('./locales/en.json'),
    es: require('./locales/es.json'),
    // ...
  }
};
```

#### RTL Support
```typescript
// RTL-aware components
const RTLContainer = styled.div`
  direction: ${props => props.rtl ? 'rtl' : 'ltr'};
  text-align: ${props => props.rtl ? 'right' : 'left'};
`;
```

### 7. Testing Strategy

#### Component Testing
```typescript
// Example test
describe('CourseCard', () => {
  it('renders course information correctly', () => {
    render(<CourseCard course={mockCourse} />);
    expect(screen.getByText(mockCourse.title)).toBeInTheDocument();
  });
});
```

#### Integration Testing
```typescript
// API integration test
describe('Course Enrollment', () => {
  it('successfully enrolls user in course', async () => {
    const { result } = renderHook(() => useEnrollCourse());
    await act(async () => {
      await result.current.enroll('course-id');
    });
    expect(result.current.isSuccess).toBe(true);
  });
});
```

### 8. Error Handling

#### Global Error Boundary
```typescript
class ErrorBoundary extends React.Component {
  componentDidCatch(error, errorInfo) {
    logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback />;
    }
    return this.props.children;
  }
}
```

#### API Error Handling
```typescript
// Error handling middleware
const errorHandler = (error) => {
  if (error.response) {
    switch (error.response.status) {
      case 401:
        // Handle unauthorized
        break;
      case 403:
        // Handle forbidden
        break;
      // ...
    }
  }
};
```

### 9. Analytics Integration

#### Event Tracking
```typescript
// Analytics service
const trackEvent = (eventName, properties) => {
  analytics.track(eventName, {
    ...properties,
    userId: currentUser.id,
    tenantId: currentTenant.id
  });
};
```

#### Performance Monitoring
```typescript
// Performance metrics
const measurePerformance = () => {
  const metrics = {
    FCP: performance.getEntriesByName('first-contentful-paint')[0],
    LCP: performance.getEntriesByName('largest-contentful-paint')[0],
    // ...
  };
  reportMetrics(metrics);
};
``` 