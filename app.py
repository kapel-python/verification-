import os
import logging
import random
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from forms import EmailForm
from utils import send_verification_code

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "email_verification_secret_key")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route for the application that handles email form submission."""
    form = EmailForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        verification_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        
        success, message = send_verification_code(email, verification_code)
        
        if success:
            flash('Verification code sent successfully!', 'success')
            logging.debug(f"Verification code {verification_code} sent to {email}")
            return jsonify({"status": "success", "message": message})
        else:
            flash(f'Failed to send verification code: {message}', 'danger')
            logging.error(f"Failed to send verification code to {email}: {message}")
            return jsonify({"status": "error", "message": message})
            
    return render_template('index.html', form=form)

# Add other routes as needed


