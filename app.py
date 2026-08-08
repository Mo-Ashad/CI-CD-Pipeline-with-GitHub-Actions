import os
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = "Flask CI/CD Project"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")

@app.route("/")
def home():
    """Display the main DevOps project dashboard."""

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>{APP_NAME}</title>

        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e3a8a);
                color: white;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 25px;
            }}

            .container {{
                width: 100%;
                max-width: 850px;
            }}

            .header {{
                text-align: center;
                margin-bottom: 25px;
            }}

            .header h1 {{
                font-size: 40px;
                margin-bottom: 10px;
            }}

            .header p {{
                color: #cbd5e1;
                font-size: 18px;
            }}

            .status {{
                display: inline-block;
                background: #16a34a;
                padding: 8px 18px;
                border-radius: 25px;
                margin-top: 15px;
                font-weight: bold;
            }}

            .cards {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 18px;
                margin-top: 25px;
            }}

            .card {{
                background: rgba(255, 255, 255, 0.10);
                border: 1px solid rgba(255, 255, 255, 0.20);
                border-radius: 15px;
                padding: 22px;
                backdrop-filter: blur(10px);
            }}

            .card h2 {{
                font-size: 18px;
                margin-bottom: 10px;
                color: #93c5fd;
            }}

            .card p {{
                font-size: 17px;
                line-height: 1.5;
            }}

            .pipeline {{
                margin-top: 25px;
                background: rgba(255, 255, 255, 0.10);
                border-radius: 15px;
                padding: 25px;
            }}

            .pipeline h2 {{
                margin-bottom: 20px;
                text-align: center;
            }}

            .steps {{
                display: flex;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                gap: 10px;
            }}

            .step {{
                background: #2563eb;
                padding: 10px 15px;
                border-radius: 8px;
                font-weight: bold;
            }}

            .arrow {{
                font-size: 22px;
                color: #93c5fd;
            }}

            .links {{
                text-align: center;
                margin-top: 25px;
            }}

            .links a {{
                display: inline-block;
                color: white;
                text-decoration: none;
                background: #0284c7;
                padding: 10px 16px;
                border-radius: 8px;
                margin: 5px;
            }}

            .links a:hover {{
                background: #0369a1;
            }}

            footer {{
                text-align: center;
                margin-top: 25px;
                color: #cbd5e1;
            }}
        </style>
    </head>

    <body>
        <div class="container">

            <div class="header">
                <h1>🚀 Flask CI/CD Project</h1>

                <p>Hello! My CI/CD Project is Working.</p>

                <div class="status">
                    ● Application Healthy
                </div>
            </div>

            <div class="cards">

                <div class="card">
                    <h2>Developer</h2>
                    <p>Mo Ashad</p>
                </div>

                <div class="card">
                    <h2>Application Version</h2>
                    <p>{APP_VERSION}</p>
                </div>

                <div class="card">
                    <h2>Environment</h2>
                    <p>{APP_ENVIRONMENT}</p>
                </div>

                <div class="card">
                    <h2>Technology</h2>
                    <p>Python, Flask, GitHub Actions and Docker</p>
                </div>

            </div>

            <div class="pipeline">
                <h2>CI/CD Pipeline</h2>

                <div class="steps">
                    <div class="step">Code</div>
                    <div class="arrow">→</div>

                    <div class="step">GitHub</div>
                    <div class="arrow">→</div>

                    <div class="step">Test</div>
                    <div class="arrow">→</div>

                    <div class="step">Docker</div>
                    <div class="arrow">→</div>

                    <div class="step">Deploy</div>
                </div>
            </div>

            <div class="links">
                <a href="/health">Health API</a>
                <a href="/api/info">Application Info</a>
                <a href="/api/pipeline">Pipeline API</a>
            </div>

            <footer>
                Developed by Mo Ashad | DevOps Learning Project
            </footer>

        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    """Return application health information."""

    return jsonify(
        {
            "status": "healthy",
            "application": APP_NAME,
            "version": APP_VERSION,
            "environment": APP_ENVIRONMENT,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    ), 200


@app.route("/api/info")
def application_info():
    """Return general application information."""

    return jsonify(
        {
            "application": APP_NAME,
            "developer": "Mo Ashad",
            "version": APP_VERSION,
            "environment": APP_ENVIRONMENT,
            "technologies": [
                "Python",
                "Flask",
                "Git",
                "GitHub Actions",
                "Docker",
            ],
        }
    ), 200


@app.route("/api/pipeline")
def pipeline_info():
    """Return the CI/CD pipeline stages."""

    return jsonify(
        {
            "pipeline": "Flask CI/CD Pipeline",
            "stages": [
                {
                    "number": 1,
                    "name": "Code",
                    "status": "completed",
                },
                {
                    "number": 2,
                    "name": "GitHub Push",
                    "status": "completed",
                },
                {
                    "number": 3,
                    "name": "Automated Testing",
                    "status": "completed",
                },
                {
                    "number": 4,
                    "name": "Docker Build",
                    "status": "completed",
                },
                {
                    "number": 5,
                    "name": "Deployment",
                    "status": "pending",
                },
            ],
        }
    ), 200


@app.errorhandler(404)
def page_not_found(error):
    """Return a JSON response for an unknown URL."""

    return jsonify(
        {
            "status": "error",
            "message": "Requested page was not found.",
            "available_routes": [
                "/",
                "/health",
                "/api/info",
                "/api/pipeline",
            ],
        }
    ), 404


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
    )
