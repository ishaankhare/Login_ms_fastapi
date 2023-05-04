# Login_ms_fastapi

A simple service to authenticate users.

A client whose credentials are validated via postgres is given a token and that is stored as a cookie in the client.

This cookie is then decrypted by the middleware in every subsequent requests to this service and any other linked service, 
which requires similar authentication.


Goal of the project: 
Dockerize an app
Authentication via token
Authenticate requests via tokens obtained via cookies
Communication between two services


Note: Error handling is not done for reponse!=200 is not done. 

