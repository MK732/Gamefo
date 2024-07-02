# GameFo

## Demo of GameFo

https://www.gamefo.net/docs

## Introduction
GameFo is an open-source API dedicated to video games, offering access to a comprehensive dataset that includes information on more than 14,000 video game titles.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. We welcome all contributions that improve the functionality and usability of GameFo. 

### Missing Games
If a game is missing, you can request to add it by submitting this form here: [FORM](https://docs.google.com/forms/d/e/1FAIpQLSfHOAAvBX4ze0k-e3X5LEgwb_TQwgeK_BovzFyIUGQXzK7NPw/viewform?usp=sf_link). Once approved it will be added to the database.


## Project Structure

Below is an overview of the files and directories in this project, excluding the `.env` file for security reasons.

### Files and Directories
**app/** 
- **routers/**: Contains the different route modules for the API.
  - **__init__.py**: Initializes the routers module.
  - **developers.py**: Contains routes to grab games by developer name.
  - **games.py**: Contains routes to grab games by game name.
  - **genres.py**: Contains routes to grab games by game genre.
  - **platforms.py**: Contains routes to grab games by game platform.
  - **publishers.py**: Contains routes to grab games by game publishers.
  - **release_dates.py**: Contains routes to grab games by game release dates.
- **db_connection.py**: Handles the database connection.
- **main.py**: The main application file that sets up the FastAPI app and includes the routes.




## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL database

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Fulosophy/Gamefo.git
   cd gamefo

2. Create a virtual environment and activate it
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

    ```
3. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
4. Set up your environment variables in the '.env' file:
   
   ```bash
   POSTGRES_HOST=host
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DATABASE=db
   ```
5. Import Sample_dataset.csv into db
# Running the application
1. Start the FastAPI server:
    ```bash
    fastapi dev main.py
    ```
    or
    ```bash
    uvicorn main:app --reload
    ```
2. Access the API documentation at 'localhost:80/docs'

## API Endpoints

### Games

- **GET /games/{game_name}**: Retrieve games with a name similar to the specified query.
- **GET /games**: Retrieve all games.
### Genres

- **GET /genre/action**: Retrieve games in the action genre.
- **GET /genre/fps**: Retrieve games in the first-person shooter (FPS) genre.
- **GET /genre/rpg**: Retrieve games in the role-playing game (RPG) genre.
- **GET /genre/adventure**: Retrieve games in the adventure genre.
- **GET /genre/shooter**: Retrieve games in the shooter genre.
- **GET /genre/sports**: Retrieve games in the sports genre.
- **GET /genre/fighting**: Retrieve games in the fighting genre.
- **GET /genre/survival**: Retrieve games in the survival genre.
- **GET /genre/racing**: Retrieve games in the racing genre.
- **GET /genre/puzzle**: Retrieve games in the puzzle genre.
- **GET /genre/simulation**: Retrieve games in the simulation genre.

### Platforms

- **GET /platforms/{platform}**: Retrieve games available on a specific platform.

### Publishers

- **GET /publishers**: Retrieve a list of publishers and their associated games.


### Developers

- **GET /developers**: Retrieve a list of developers and their associated games.

## Database Connection

The `db_connection.py` file contains the function to connect to the PostgreSQL database using `psycopg2`. Ensure your database connection details are correctly set up in the `.env` file.

## Error Handling

All routes include error handling to manage database connection issues and query execution errors, returning appropriate HTTP status codes and messages.



## License

This project is licensed under the GNU General Public License v2.0. See the [LICENSE](LICENSE) file for more details.

