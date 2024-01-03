# Local Project Execution

To run the project locally, follow these steps:

1. If you don't have a virtual environment, create one using the following commands:
   - `python -m venv venv`
   - `venv\Scripts\activate` **(Windows)**
   - `source venv/bin/activate` **(MacOs/Linux)**

2. If project dependencies are not installed yet, execute:
   - `pip install -r requirements.txt`

3. Create a `.env` file in the project root and add environment variables based on the provided `.env.example`.

4. In the project's root folder, run the following command to start the server:
   - `uvicorn api.app:app --reload`

5. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) **(Project Swagger documentation)**.

# Dockerized Execution

To run the project using Docker, execute the following command:

```bash
docker-compose up
```
This will set up and run the project within a Docker container.
