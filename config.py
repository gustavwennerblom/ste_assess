class BaseConfig:
    pass

class DevConfig(BaseConfig):
    pass

class UnitTestConfig(BaseConfig):
    WTF_CSRF_ENABLED = False
