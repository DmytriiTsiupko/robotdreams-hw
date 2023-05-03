from robot_app import app
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    app.run(host=app.config.get("HOST"),
            port=app.config.get("PORT"),
            debug=app.config.get("DEBUG"))
