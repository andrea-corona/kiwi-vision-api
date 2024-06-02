class DefaultDevelopmentConfiguration():
    DEBUG = True
    CORS_HEADERS = 'Content-Type'

class DeploymentConfiguration():
    DEBUG = False
    CORS_HEADERS = 'Content-Type'

configuration = {
    'development' : DefaultDevelopmentConfiguration,
    'deployment' : DeploymentConfiguration
}