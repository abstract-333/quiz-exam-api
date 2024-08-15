from fastapi_users.openapi import OpenAPIResponseType
from fastapi_users.router.common import ErrorModel
from starlette import status

from api.rating.rating_docs import SERVER_ERROR_AUTHORIZED_RESPONSE
from utilties.error_code import ErrorCode

GET_QUIZ_RESPONSES: OpenAPIResponseType = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    ErrorCode.QUESTIONS_NUMBER_INVALID: {
                        "summary": "Invalid number of questions",
                        "value": {"detail": ErrorCode.QUESTIONS_NUMBER_INVALID},
                    }
                }
            },
        },
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    ErrorCode.EMPTY_LIST: {
                        "summary": "Empty list returned",
                        "value": {"detail": ErrorCode.EMPTY_LIST},
                    }
                }
            },
        },
    },
}

GET_QUIZ_RESPONSES.update(SERVER_ERROR_AUTHORIZED_RESPONSE)
