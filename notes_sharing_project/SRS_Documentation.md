# Software Requirements Specification (SRS)
# Online Notes Sharing Platform

## 1. Introduction
### 1.1 Purpose
Web-based platform for students/educators to upload, share, and manage academic notes (PDF/DOCX format).

### 1.2 Scope
- User registration/authentication
- Note upload/download functionality
- Public/private note management
- Search and categorization

## 2. Overall Description
### 2.1 Product Perspective
- Standalone web application
- Django backend with SQLite database
- Bootstrap-based responsive frontend

### 2.2 User Classes
- Students (primary users)
- Educators
- Administrators

## 3. System Features
### 3.1 Authentication System
- User registration
- Login/logout
- Password reset

### 3.2 Note Management
- Upload notes (PDF/DOCX)
- Edit note metadata
- Delete notes
- Toggle public/private status

### 3.3 Dashboard
- Personal note repository
- Search/filter functionality
- Quick access to recent notes

### 3.4 Public Notes
- Browse all public notes
- Filter by subject/category
- Download functionality

## 4. Technical Requirements
### 4.1 Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 5 framework
- Responsive design

### 4.2 Backend
- Django 4.x
- SQLite database
- File storage system

### 4.3 Security
- CSRF protection
- Password hashing
- File type validation

## 5. Interface Requirements
### 5.1 User Interfaces
- Login/Registration screens
- Dashboard view
- Note upload/edit forms
- Public notes browser

## 6. Non-Functional Requirements
### 6.1 Performance
- Support 50+ concurrent users
- <2s page load times

### 6.2 Security
- Role-based access control
- Secure file uploads
- Data encryption

## 7. Future Enhancements
- Note versioning
- Collaborative editing
- Mobile application
- API for integrations
