# DRF

Drf is a Django REST Framework example project that serves as an API backend for products. It provides a set of endpoints to handle creation, listing, details, updating, deleting and searching of products.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Client Applications](#client-applications)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mcjosh-sys/drf.git
   ```

2. Change into the project directory:

   ```bash
   cd drf
   ```

3. Create a virtual environment for the backend:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment for the backend:

   - For Windows:

     ```bash
     call .venv\Scripts\activate
     ```

   - For Unix/macOS:

     ```bash
     source .venv/bin/activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the backend directory.

2. Define the required environment variables in the `.env` file. For example:

   ```plaintext
   DEBUG=True
   ALGOLIA_API_SECRETS
   ```

3. Update the project settings in `backend/settings.py` to suit your needs.

## Usage

1. Apply the database migrations for the backend:

   ```bash
   python backend/manage.py migrate
   ```

2. Start the backend development server:

   ```bash
   python backend/manage.py runserver
   ```

3. The backend API endpoints will be accessible at `http://localhost:8000/`.


## API Endpoints

The following API endpoints are available in the backend:

- `GET /api/products/?limit=10&offset=10`: Retrieve the list of 10 products.
- `POST /api/prodcuts/`: Create a new prodcut.
- `GET /api/prodcut/{id}/`: Retrieve a specific prodcut.
- `PUT /api/update/{id}/`: Update a specific update.
- `DELETE /api/product/{id}/`: Delete a specific product.

## Client Applications

The project includes two client applications:

1. Python Client:
   - Location: `py_client`
   - Use this client to interact with the backend API programmatically using Python.

2. JavaScript Client:
   - Location: `js_client`
   - This client is a web application that provides a user interface to interact with the backend API.
