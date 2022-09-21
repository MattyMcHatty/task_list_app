from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from controllers.tasks_controller import tasks_blueprint # NEW

# Register the blueprint with the Flask app
app.register_blueprint(tasks_blueprint) # NEW