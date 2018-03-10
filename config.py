class BaseConfig:
    pass


class DevConfig(BaseConfig):
    COURSE_MODULES_FILENAME = 'course_modules.csv'


class PilotConfig(BaseConfig):
    COURSE_MODULES_FILENAME = 'course_modules_pilot.csv'


class ProdConfig(BaseConfig):
    COURSE_MODULES_FILENAME = 'course_modules.csv'
    TEST_CONFIG_PARAMETER = "Delete me"


class UnitTestConfig(BaseConfig):
    COURSE_MODULES_FILENAME = 'course_modules.csv'
    WTF_CSRF_ENABLED = False
