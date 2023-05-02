# Login_ms_fastapi

A simple service to authenticate users.

A client whose credentials are validated via postgres is given a token and that is stored as a cookie in the client.

This cookie is then decrypted by the middleware in every subsequent requests to this service and any other linked service, 
which requires similar authentication.



