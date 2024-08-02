<h1 align="center">
MangaRealm Authenticator
</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/fastapi-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL Badge"/></a>
  <a href="#"><img src="https://img.shields.io/badge/redis-%23DC382D.svg?style=for-the-badge&logo=redis&logoColor=white" alt="Redis Badge"/></a>
</p>

<p align="center">
  <a href="#" target="_blank">
    <img src="https://thullydev.github.io/thullyDevStatics/images/mangarealm-logo.png" alt="Logo" width="200"/>
  </a>
</p>

## What is MangaRealm Authenticator?

The **MangaRealm Authenticator** is a crucial component of the MangaRealm ecosystem, handling user authentication, registration, and password management. Built with FastAPI, this service ensures secure and efficient user operations for the MangaRealm platform.

## Features

- User registration with email verification
- User login with token generation
- Password reset functionality
- Email-based verification and password renewal
- Integration with Redis for caching and rate limiting
- Secure token generation and management

## API Endpoints and Usage Guide

### 1. Sign Up
- **Route**: `/auth/signup/`
- **Method**: POST
- **Parameters**: 
  - `username`: User's chosen username
  - `email`: User's email address
  - `password`: User's password (must be at least 10 characters)
  - `confirm`: Password confirmation
- **Description**: Registers a new user and sends a verification email.

### 2. Verify Email
- **Route**: `/auth/verify/`
- **Method**: POST
- **Parameters**:
  - `code`: Verification code sent to user's email
- **Description**: Verifies the user's email and completes the registration process.

### 3. Login
- **Route**: `/auth/login/`
- **Method**: POST
- **Parameters**:
  - `email`: User's email address
  - `password`: User's password
- **Description**: Authenticates the user and returns a token for subsequent requests.

### 4. Forgot Password
- **Route**: `/auth/forgot_password/`
- **Method**: POST
- **Parameters**:
  - `email`: User's registered email address
- **Description**: Sends a password reset link to the user's email.

### 5. Renew Password
- **Route**: `/auth/renew_password/`
- **Method**: POST
- **Parameters**:
  - `code`: Reset code from the email
  - `password`: New password
  - `confirm`: New password confirmation
- **Description**: Allows the user to set a new password after requesting a reset.

## Security Features

- Password length validation (minimum 10 characters)
- Email format validation
- Unique token generation for authentication
- Time-limited verification and password reset codes
- Email-based verification for sensitive operations


This Authenticator service is designed to provide robust and secure user management for the MangaRealm platform, ensuring that user data and access are protected while offering a smooth authentication experience.