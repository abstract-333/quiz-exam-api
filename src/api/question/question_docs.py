from fastapi_users.openapi import OpenAPIResponseType
from fastapi_users.router.common import ErrorModel
from starlette import status

from api.rating.rating_docs import SERVER_ERROR_AUTHORIZED_RESPONSE
from utilties.error_code import ErrorCode

ADD_QUESTION_RESPONSES: OpenAPIResponseType = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.ANSWER_NOT_INCLUDED_IN_CHOICES: {
                    "summary": "Not valid question formula",
                    "value": {"detail": ErrorCode.ANSWER_NOT_INCLUDED_IN_CHOICES},
                },
                    ErrorCode.NUMBER_OF_CHOICES_NOT_FOUR: {
                        "summary": "Number of choices not equal to four",
                        "value": {"detail": ErrorCode.NUMBER_OF_CHOICES_NOT_FOUR},
                    },
                }
            },
        },
    },
    status.HTTP_405_METHOD_NOT_ALLOWED: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.USER_NOT_ADMIN_SUPERVISOR: {
                    "summary": "Only supervisor or admin_panel can enter or patch quizzes",
                    "value": {"detail": ErrorCode.USER_NOT_ADMIN_SUPERVISOR},
                }
                }
            },
        },
    },
    status.HTTP_409_CONFLICT: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.QUESTION_DUPLICATED: {
                    "summary": "Quiz duplicated, you've entered same question with same choices and answer",
                    "value": {"detail": ErrorCode.QUESTION_DUPLICATED},
                }
                }
            }
        }
    },
}
PATCH_QUESTION_RESPONSES: OpenAPIResponseType = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.ANSWER_NOT_INCLUDED_IN_CHOICES: {
                    "summary": "Not valid question formula",
                    "value": {"detail": ErrorCode.ANSWER_NOT_INCLUDED_IN_CHOICES},
                },
                    ErrorCode.NUMBER_OF_CHOICES_NOT_FOUR: {
                        "summary": "Number of choices not equal to four",
                        "value": {"detail": ErrorCode.NUMBER_OF_CHOICES_NOT_FOUR},
                    },
                }
            },
        },
    },
    status.HTTP_405_METHOD_NOT_ALLOWED: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.NOT_QUESTION_OWNER: {
                    "summary": "Only question writer can patch it",
                    "value": {"detail": ErrorCode.NOT_QUESTION_OWNER},
                }, ErrorCode.USER_NOT_ADMIN_SUPERVISOR: {
                    "summary": "Only supervisor or admin_panel can enter or patch quizzes",
                    "value": {"detail": ErrorCode.USER_NOT_ADMIN_SUPERVISOR},
                },
                    ErrorCode.QUESTION_NOT_EDITABLE: {
                        "summary": "You can't edit question now",
                        "value": {"detail": "You can edit the question for 30 minutes after you sent it"},
                    }
                }
            },
        },
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.QUESTION_NOT_FOUND: {
                    "summary": "Question not exists",
                    "value": {"detail": ErrorCode.QUESTION_NOT_FOUND},
                }
                }
            }
        }
    },
    status.HTTP_409_CONFLICT: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.QUESTION_DUPLICATED: {
                    "summary": "Quiz duplicated, you've entered same question with same choices and answer",
                    "value": {"detail": ErrorCode.QUESTION_DUPLICATED},
                }
                }
            }
        }
    },
}

GET_QUESTION_RESPONSES: OpenAPIResponseType = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    ErrorCode.INVALID_PAGE: {
                        "summary": "Invalid page",
                        "value": {"detail": ErrorCode.INVALID_PAGE},
                    }
                }
            },
        },
    },
}

GET_QUESTION_SECTION_RESPONSES: OpenAPIResponseType = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.OUT_OF_SECTION_ID: {
                    "summary": "Wrong section_id entered",
                    "value": {"detail": ErrorCode.OUT_OF_SECTION_ID},
                },
                    ErrorCode.INVALID_PAGE: {
                        "summary": "Invalid page",
                        "value": {"detail": ErrorCode.INVALID_PAGE},
                    }
                }
            },
        },
    },
}

DELETE_QUESTION_RESPONSES: OpenAPIResponseType = {

    status.HTTP_401_UNAUTHORIZED: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    ErrorCode.USER_INACTIVE: {
                        "summary": "Missing token or inactive user.",
                        "value": {"detail": "Unauthorized"
                                  },
                    }
                }
            },
        },
    },
    status.HTTP_403_FORBIDDEN: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    ErrorCode.USER_NOT_AUTHENTICATED: {
                        "summary": "Not authenticated",
                        "value": {"detail": "Not authenticated"},
                    },
                    ErrorCode.FORBIDDEN: {
                        "summary": "Not superuser",
                        "value": {"detail": ErrorCode.FORBIDDEN},
                    }
                }
            },
        },
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.QUESTION_NOT_FOUND: {
                    "summary": "Question not exists",
                    "value": {"detail": ErrorCode.QUESTION_NOT_FOUND},
                }
                }
            }
        }
    },
    status.HTTP_429_TOO_MANY_REQUESTS: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {ErrorCode.TOO_MANY_REQUESTS: {
                    "summary": "Too many requests",
                    "value": {"detail": ErrorCode.TOO_MANY_REQUESTS},
                }
                }
            },
        },
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Internal sever error.",
    }
}

ADD_QUESTION_RESPONSES.update(SERVER_ERROR_AUTHORIZED_RESPONSE)
PATCH_QUESTION_RESPONSES.update(SERVER_ERROR_AUTHORIZED_RESPONSE)
GET_QUESTION_RESPONSES.update(SERVER_ERROR_AUTHORIZED_RESPONSE)
GET_QUESTION_SECTION_RESPONSES.update(SERVER_ERROR_AUTHORIZED_RESPONSE)
