import openai

openai.api_key = 'the_openai_api_key'

def generate_email(profile_info, reason):
    # Send a prompt based on the profile info and reason
    prompt  = (f"Write a personalized email to {profile_info['name']}, "
              f"a {profile_info['title']} at {profile_info['company']}. "
              f"The reason for contact is: {reason}.")
    
    # Generate email using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    email_comtent = response.choices[0].text.strip()
    return email_comtent