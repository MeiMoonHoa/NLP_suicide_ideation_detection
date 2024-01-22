# Suicide Ideation Detection

This project is to predict suicide ideation.

## Overview

This repository contains the files necessary for deploying a Flask application on PythonAnywhere. The application is designed to detect suicide ideation. You may test the application on https://meimoonhoa.pythonanywhere.com/

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have a PythonAnywhere account. (you might need a paid account if the basic package isn't sufficient.)
* You have developed the model, and extracted them into pytorch_model.bin, config.json, special_tokens_map.json, tokenizer_config.json, tokenizer.json and vocab.json
* For assets in used for this application were saved in https://drive.google.com/drive/folders/1thRiaOBBXFTYkpRX3NThmbuRUqyNTuT1?usp=sharing

## Files Description

Here's a brief description of the files included in this repository:

- `flask_app.py`: The Flask application configuration file.
- `home.py`: The module that handles the homepage logic.
- `applications.py`: The main entry point for the Flask application.
- `resources.py`: Contains additional resources and utilities for the application.
- `contacts.py`: A module for managing contact information.
- `meimoonhoa_pythonanywhere_com_wsgi.py`: The WSGI file used by PythonAnywhere to serve the application.

## Deployment

To deploy this project on PythonAnywhere, follow these steps:

1. Upload the files to your PythonAnywhere account.
2. Set up your web app using the PythonAnywhere interface.
3. Configure the WSGI file to point to your Flask application.


## Contact

Name - Hoa Mei Moon

Project Link: https://github.com/MeiMoonHoa/NLP_suicide_ideation_detection
