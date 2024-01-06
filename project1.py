from transformers import pipeline
import wikipedia

def processor(question, text):
    # Create a question answering pipeline
    qa = pipeline("question-answering")

    # Get the answer from the pipeline
    answer = qa(question=question, context=text)

    # Print the answer
    print(answer)

wikipedia.set_lang("en")

print("Welcome! Ask me anything.")

# get user input
user_input = "what causes precipitation to fall"

# search for query on Wikipedia
try:
    page = wikipedia.page(user_input)
    text = page.summary
    question = user_input
    processor(question, text)
except wikipedia.exceptions.DisambiguationError as e:
    print("Can you please be more specific?")
except wikipedia.exceptions.PageError as e:
    print("Sorry, I could not find any information on that topic.")
