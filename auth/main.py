from fastapi import FastAPI, Header

app = FastAPI()

@app.route("/login")
def login(request: str = Header(None)):
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    return createJWT(auth.username, "fake_key")


@app.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "missing credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(
            encoded_jwt, "fake_key", algorithms=["HS256"]
        )
    except:
        return "not authorized", 403

    return decoded, 200


def createJWT(username, secret):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )
    

