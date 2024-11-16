from enum import IntEnum


class ObservableActionType(IntEnum):
    ACTION_DELETE = 1,
    ACTION_UPDATE = 2,
    ACTION_CREATE = 3,
    ACTION_DUMP = 4,
    ACTION_LOAD_DUMP = 5
