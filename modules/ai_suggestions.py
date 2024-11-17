import openai
import yaml

def generate_content_idea(prompt):
    """Use OpenAI API to generate content ideas."""
    with open("config/settings.yaml", "r") as file:
        config = yaml.safe_load(file)

    openai.api_key = config["openai_api_key"]

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    if response.choices:
        idea = response.choices[0].text.strip()
        print("AI-generated idea:", idea)
        return idea
    else:
        print("Failed to generate idea.")
