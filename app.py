import random
from flask import Flask, render_template

app = Flask(__name__)

# Mock AI / Motivational quotes list
quotes = [
    "Believe in yourself! Every expert was once a beginner. 🚀",
    "Code, commit, deploy, repeat! You've got this. 💻",
    "Small daily progress adds up to huge results. 🌟",
    "Errors are just proof that you are trying and learning. 🛠️",
    "Keep pushing forward. Success is just one git push away! 🔥"
]

@app.route('/')
def home():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
print("thankyou")
