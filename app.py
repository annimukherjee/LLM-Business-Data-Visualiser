from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize GPT-Neo pipeline
# generator = pipeline("text-generation", model="distilgpt2")
generator = pipeline("text2text-generation", model="mrm8488/t5-base-finetuned-wikiSQL")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/generate_sql", methods=["POST"])  # Ensure this matches the JavaScript fetch URL
def generate_sql():
    data = request.json
    query = data["query"]
    print(query)
    try:
        # Generate SQL using GPT-Neo
        # The prompt should guide the model to generate SQL.
        prompt = f"translate English to SQL: {query}"
        print(prompt)
        response = generator(prompt, max_length=100, do_sample=True)
        print(response)
        generated_sql = response[0]["generated_text"].split(prompt)[-1].strip()

        # Return the generated SQL
        return jsonify({"sql": generated_sql})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask server
