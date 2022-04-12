from Website import (
    create_app,
)  ## We can do this because website is a pyhton package since we addded the __init__.py file

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
