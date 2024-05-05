# Flask Tweet Recommendation System

This is a Flask application for a simple tweet recommendation system. It allows users to submit tweets, extracts hashtags from the tweet content, and recommends related tweets based on those hashtags.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies:**

    ```bash
    pip install Flask neo4j flask_session
    ```

3. **Set Up Neo4j:**

    - Make sure you have Neo4j installed and running on your machine.
    - Update the Neo4j connection details (URL, username, and password) in the `driver` initialization in `app.py`.

4. **Set Up Environment (Mac):**

    - Ensure you have Python installed. You can install it via Homebrew by running:
      ```bash
      brew install python
      ```

    - Make sure you have pip, Python's package manager, installed. You can install it using the following command:
      ```bash
      sudo easy_install pip
      ```

    - Install Flask and necessary dependencies using pip:
      ```bash
      pip install Flask neo4j flask_session
      ```

5. **Run the Application:**

    ```bash
    python app.py
    ```

## Usage

- Visit `http://localhost:5006` in your browser to access the application.
- Submit tweets using the form provided on the homepage.
- The system will recommend related tweets based on the hashtags in the submitted tweet.

## File Structure

- **app.py:** Contains the main Flask application code.
- **templates/index.html:** HTML template for the homepage.
- **README.md:** Documentation for the application.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
