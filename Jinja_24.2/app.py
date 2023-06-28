from flask import Flask, render_template, request
from stories import story


app = Flask(__name__)


@app.route("/")
def form():
    """Generate and show form to ask for prompts."""
    prompts = story.prompts

    return render_template("prompts.html", prompts=prompts)


@app.route("/story")
def create_story():
    created_story = story.generate(request.args)
    return render_template("story.html", created_story=created_story)
