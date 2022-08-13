from url_shortner import create_app
import os


def main():
    port = int(os.environ.get('PORT', 5000))
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
