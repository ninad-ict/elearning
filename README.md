# MyWebApp: A Django Project for Content Upload

## Description

**MyWebApp** is a Django-based web application designed to manage user accounts, handle content uploads, and provide validation for email addresses and content size. This application allows users to register, log in, and upload content while ensuring that the content does not exceed 1000 characters and that the email provided is valid and not from restricted domains like Yahoo.

## Features
- User login and registration
- Content upload with size validation (max 1000 characters)
- Email format and domain validation (no Yahoo emails)
- Admin panel for managing users and content

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- pip (Python package installer)

### Step-by-Step Guide

1. Clone the repository:
   ```bash
   git clone https://github.com/ninad-ict/elearning.git
   

2. Navigate to the project directory:

cd elearning

3. Set up a virtual environment:

python -m venv myenv

4. Activate environment
source myenv/bin/activate

5. Install dependencies
pip install -r requirements.txt


6. Make the migrations

python manage.py makemigrations
python manage.py migrate





My Reflections - https://olivine-lion-f05.notion.site/Reflections-and-Documentation-1736bcb432a8806eb4a6ca4020da48f4?pvs=4