from flask import Flask, render_template, request, jsonify
from scarping import scrape_linkedin_profile
from openai_client import generate_email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_email', methods=['POST'])
def generate_email_route():

    # Get data from request
    data = request.json
    linkedin_url = data['linkedin_url']
    reason = data['reason']

    # Scrape LinkedIn profile
    profile_info = scrape_linkedin_profile(linkedin_url)
    
    # Generate email using OpenAI
    email = generate_email(profile_info, reason)


    return jsonify({'email_content': email})

if __name__ == '__main__':
    app.run(debug=True)