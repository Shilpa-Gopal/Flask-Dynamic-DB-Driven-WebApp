# Flask-Dynamic-DB-Driven-WebApp

Welcome! This project showcases a Flask web applicationvand provides guides and tutorials to help beginners start with Flask and Python.

## Project Overview

This web application is built using Flask and Bootstrap. It includes:
- A navigation bar with a logo and title.
- A home page displaying a list of job openings.
- An API endpoint to fetch job listings in JSON format.

## Features

- **Home Page**: Intro part.
- **API Endpoint**: Provides a JSON response with job listings.
- **Responsive Design**: Uses Bootstrap for a responsive layout.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/Flask-Dynamic-DB-Driven-WebApp.git
    cd Flask-Dynamic-DB-Driven-WebApp

    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**:

    ```sh
    pip install Flask
    ```

## Usage

1. **Run the Flask application**:

    ```sh
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000` to see the home page.

3. **API Endpoint**: You can access the course listings in JSON format at `http://127.0.0.1:5000/api/course`.

## Project Structure
```
Flask-Dynamic-DB-Driven-WebApp/
│
├── app.py # Main Flask application
├── static/
│ ├── logo.png # Logo image
│ └── # Additional images
├── templates/
│ ├── home.html # Home page template
│ ├── courseitem.html # course item template
│ ├── nav.html # Navigation bar template
│ └── footer.html # Footer template
└── README.md # Project documentation
```
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact Shilpa at [dev.shilpag@gmail.com](mailto:dev.shilpag@gmail.com).
