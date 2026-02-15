print("Starting deployment...")
environment = "dev"

if environment == "prod":
    print("Deploying to Production")
else:
    print("Deploying to Development")

print("Deployment completed!")