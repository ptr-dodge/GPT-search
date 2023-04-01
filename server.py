import openai
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='static')

# Define the OpenAI API endpoint and your API key
openai.api_key = "YOUR_API_KEY_HERE"
engine_name = "text-davinci-002"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the value of the 'q' parameter from the form data
        q_value = request.form['q']

        # Define the prompt and parameters for the OpenAI API call
        prompt_text = q_value
        model_params = {
            "max_tokens": 500,
            "temperature": 0.5
        }

        try:
            print("Before API call")
            # Make a completion request using the openai.Completion API
            response = openai.Completion.create(
                engine=engine_name,
                prompt=prompt_text,
                **model_params
            )
            print("After API call")

            # Get the response text from the API response
            response_text = response.choices[0].text
            return response_text
        except Exception as e:
            # Handle errors and return an error message to the user
            return f"Error: {str(e)}"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=6969)