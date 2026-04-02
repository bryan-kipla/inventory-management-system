from app import create_app

# Create app using factory
app = create_app()

if __name__ == "__main__":
    # Run Flask app in debug mode
    app.run(debug=True)
