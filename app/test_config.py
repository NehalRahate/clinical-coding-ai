from app.core.config import settings


print("Application:", settings.APP_NAME)
print("Version:", settings.APP_VERSION)
print("Debug:", settings.DEBUG)

print("Database configured:", bool(settings.DATABASE_URL))
print("AWS Region:", settings.AWS_REGION)