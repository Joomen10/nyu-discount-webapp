# nyu-discount-webapp
Discount Finder Application for NYU students


https://github.com/user-attachments/assets/12e6866e-dbc3-4106-ab61-f570edfab85e


## NYU Dining Deals Locator 🍎
A full-stack Django web app that helps NYU students discover and compare campus-area restaurant discounts in seconds. Using Google Maps & Places APIs, the app plots over 30 eateries on an interactive map and companion list view, with real-time hours, price ranges, and student-only offers behind a NetID-gated login.
  
## Highlights
Interactive Map + List View: Easily find nearby restaurants and student deals.  

Real-time Data: Get up-to-the-minute hours, price range, and basic details directly from Google Places.  
  
Secure Access: NetID-gated login for student-only deals, with email/password support for local development.  

User-Generated Content: A simple workflow for submitting reviews and ratings.  

Robust Development Practices: CI with GitHub Actions, task tracking in Jira, and specs in Confluence.  

Reproducible Environment: Docker-containerized MySQL on AWS EC2; local Django apps are securely networked via ZeroTier.  

## Tech Stack
Backend: Python, Django, Django ORM  

Database: MySQL (Docker in production/staging), SQLite (default for local development)  

Frontend: Django templates, vanilla JavaScript, Google Maps JS SDK  

Authentication: NetID/SSO (production), local email/password (development)  

Infrastructure: AWS EC2 (MySQL container), ZeroTier for secure development networking  

## CI/CD: 
GitHub Actions (lint, test, build)

## Repository Structure  
nyu-discount-webapp/  
├─ nyudiscount/        # Project settings/urls  
├─ restaurant/         # Deals, restaurants, reviews, list/detail views, APIs  
├─ map/                # Map pages, zone endpoints, front-end glue  
├─ users/              # Auth (NetID/SSO ready), local dev login  
├─ static/js/          # Front-end JS (e.g., map.js)  
├─ manage.py  
├─ requirements.txt  
└─ README.md  


## Split-Domain Architecture
To accelerate development and prevent merge conflicts, the codebase is separated into two functional domains:  
Restaurant Service: Handles restaurants, deals, and reviews.  
Branches: feature/restaurant-*  
Map Service: Manages the map page, markers, and zone utilities.  
Branches: feature/map-*  
This setup enables two sub-teams to work in parallel, with weekly PR reviews and quick inte gration.  

## Core URLs  
Map: /map/  
Restaurants: /restaurants/ and /restaurants/<id>/  
Auth: /login/, /logout/, /signup/ (local development)  
Data Model (High-Level)  
Restaurant: name, location, hours, price level, tags  
Deal: description, discount type, start/end dates, foreign key to restaurant  
Review: user, rating, comment, created_at  
For the definitive data model, refer to restaurant/models.py.  

## Development Workflow
Work on domain-specific branches: feature/map-* or feature/restaurant-*.  
Submit small, focused pull requests with screenshots or short clips for UI changes.  
Conduct weekly PR reviews to ensure shared code quality across domains.  
Keep views thin; move shared logic into helpers or services.  
Run tests locally using python manage.py test.  

## CI/CD
GitHub Actions automatically runs linting and tests on every push and pull request.  

## Notes
NetID/SSO: The app supports NetID-gated access in production. Use local auth during development.    

ZeroTier: This tool is used by the development team for secure networking of local instances and is optional for most contributors.    

Google APIs: You must provide valid API keys for both Maps and Places to render the map and fetch restaurant details.  

License
All rights reserved.

