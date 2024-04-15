# CMS-Web-developement-1

## Overview

This CMS (Content Management System) is designed to provide a streamlined, user-friendly interface for managing web content. Built with Flask, this system allows for easy content creation, editing, and management. It's ideal for small businesses, bloggers, and anyone needing a simple yet powerful tool to handle their digital content.

## Features

User Authentication: Secure login system to ensure that only authorized users can manage content.  
Content Management: Users can create, edit, and delete content using a simple web-based interface.  
Dynamic Content Display: All content is displayed on the homepage, with individual detail views.  
Responsive Design: Uses Bootstrap for a responsive layout that works on desktops, tablets, and mobiles.  

## Future Enhancements

Rich Text Editing: Integration of a WYSIWYG editor for rich content formatting.  
Media Management: Ability to upload and manage media files such as images and videos.  
Multi-Language Support: Options for publishing content in multiple languages.  
SEO Tools: Enhanced features to improve search engine optimization for content.  
User Roles and Permissions: More granular access control for different types of users.  
API Access: RESTful API for programmatic access to the CMS functionalities.  
Advanced Security Features: Enhanced security measures, including two-factor authentication and encrypted storage.  
Analytics Integration: Dashboard for tracking content engagement and user activity.  
Installation

## Prerequisites
Python 3.8 or later  
pip (Python package installer)  
Virtual environment (recommended)

## Setup Instructions  

Clone the repository:  
git clone https://github.com/gkirat20/CMS-Web-developement-1.git  
cd CMS-Web-developement-1

Set up a Python virtual environment (optional but recommended):  
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required Python packages:  
pip install -r requirements.txt

Initialize the database:  
python
>>> from app import db
>>> db.create_all()
>>> exit()
Run the application:  
>>> ./setup.sh  # Or `bash setup.sh` on Windows
Navigate to http://127.0.0.1:5000 in your web browser to see the application running.  

## Usage  

To log in and manage content: Access /login and use the credentials created during setup.  
Adding content: Click on 'Manage Content' after logging in to add or edit existing entries.  
Viewing content: All content is viewable on the homepage by default.  

## Contributing

We welcome contributions! If you're interested in helping improve this CMS, please fork the repository and submit a pull request with your enhancements. For major changes, please open an issue first to discuss what you would like to change.  

## License  

This project is licensed under the Apache License 2.0
