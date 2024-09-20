from fastapi import FastAPI
from app.routers import games, genres, publishers, developers, platforms, release_dates
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse

load_dotenv(dotenv_path="/code/app/.env")

# Create a FastAPI instance
app = FastAPI(swagger_ui_parameters={"displayRequestDuration": True, "syntaxHighlight.activated" : False },
              
              title="GameFo API",
              description="An API to get information about games, genres, publishers, developers, and platforms.",
              openapi_url="/api/v2/openapi.json",
              
              )


# Inlcude all the routers
app.include_router(games.router)
app.include_router(genres.router)
app.include_router(publishers.router)
app.include_router(developers.router)
app.include_router(platforms.router)
app.include_router(release_dates.router)

# Root route
@app.get("/",response_class=HTMLResponse)
def home_route():
    return """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GameFo API</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f3f4f6;
            color: #333;
            line-height: 1.6;
        }

        header {
            background: linear-gradient(135deg, #4CAF50, #2E7D32);
            padding: 10px 20px;
            text-align: center;
            color: white;
        }

        header h1 {
            font-size: 3em;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }

        .container {
            max-width: 1200px;
            margin: 50px auto;
            padding: 0 20px;
        }

        .card {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            padding: 30px;
            margin-bottom: 40px;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-10px);
        }

        .card h2 {
            color: #2E7D32;
            margin-bottom: 15px;
            font-size: 2em;
            border-bottom: 3px solid #4CAF50;
            display: inline-block;
            padding-bottom: 8px;
        }

        .card p {
            font-size: 1.15em;
            margin-bottom: 20px;
        }

        .highlight {
            color: #ff9800;
            font-weight: bold;
        }

        .btn {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.1em;
            transition: background-color 0.3s ease;
        }

        .btn:hover {
            background-color: #388E3C;
        }

        .center {
            text-align: center;
        }

        .btn-container {
            margin-top: 20px;
            display: flex;
            justify-content: center;
        }
        
        @media (max-width: 768px) {
            .card h2 {
                font-size: 1.8em;
            }

            .card p {
                font-size: 1.05em;
            }
        }
    </style>
</head>
<body>

<header>
    <h1>GameFo API</h1>
</header>

<div class="container">
    <div class="card">
        <h2>Introduction</h2>
        <p>
            <span class="highlight">GameFo</span> is an open-source API dedicated to video games, offering access to a comprehensive dataset of more than 14,000 titles. Whether you're a developer, gamer, or a data enthusiast, GameFo provides a vast amount of data across various platforms and genres.
        </p>
    </div>

    <div class="card">
        <h2>Contributing</h2>
        <p>
            Want to contribute to GameFo? It's easy! Fork the repository on GitHub and submit your pull request. We appreciate all contributions that help improve the functionality and user experience of GameFo.
        </p>
        <div class="btn-container">
            <a href="https://github.com/MK732/Gamefo" class="btn">Contribute on GitHub</a>
        </div>
    </div>

    <div class="card">
        <h2>Missing a Game?</h2>
        <p>
            If a game is missing from our database, simply submit a request using our form, and once approved, it will be added to the GameFo database.
        </p>
    </div>

    <div class="card">
        <h2>Why GameFo?</h2>
        <p>
            GameFo is designed with developers in mind, offering an easy-to-use API that lets you retrieve data on games, genres, platforms, and much more. Best of all, it's completely free and open-source.
        </p>
    </div>
</div>

</body>
</html>
    """


