from app_api import create_app


# Creating app instance
app = create_app('development')


if __name__ == '__main__':
    app.run(port=4000)