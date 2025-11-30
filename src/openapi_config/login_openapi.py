from src.dto import LoginResponse


response_login_controller = {
    200: {"model": LoginResponse,
          "description": "Login Success",
          "content": {
                "application/json": {
                    "example": {"status": 200, "msg": "Login Success", "token": "PLACEHOLDER_JWT_TOKEN"}
                }}
        },

    404: {"model": LoginResponse,
          "description": "Login Failed",
          "content": {
                "application/json": {
                    "example": {"status": 404, "msg": "Wrong username or password", "token": "null"}
                }}
        }
}