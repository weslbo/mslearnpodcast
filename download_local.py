import requests

# Define a list of URLs
urls = [
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-app-service/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/configure-web-app-settings/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/scale-apps-app-service/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/understand-app-service-deployment-slots/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/explore-azure-functions/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/develop-azure-functions/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/explore-azure-blob-storage/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/manage-azure-blob-storage-lifecycle/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/work-azure-blob-storage/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/explore-azure-cosmos-db/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/work-with-cosmos-db/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/publish-container-image-to-azure-container-registry/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/create-run-container-images-azure-container-instances/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/implement-azure-container-apps/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/explore-microsoft-identity-platform/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/implement-authentication-by-using-microsoft-authentication-library/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/implement-shared-access-signatures/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/microsoft-graph/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/implement-azure-key-vault/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/implement-managed-identities/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/implement-azure-app-configuration/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/explore-api-management/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/azure-event-grid/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/azure-event-hubs/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/discover-azure-message-queue/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/monitor-app-performance/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/develop-for-azure-cache-for-redis/",
    "https://prod-23.eastus.logic.azure.com/workflows/1dd4e45a92de41fc8e0cf0044980577d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rjYWaYRnIWe4qh84C-Qwg7gxyJ9O5gBJHmgCrYwDmRQ&url=https://learn.microsoft.com/en-us/training/modules/develop-for-storage-cdns/"
]

# Download each URL
i=1
for url in urls:

    filename = "az-204-" + str(i).zfill(3) + "-" + url.split("/")[-2] + ".mp3"
    print(filename)

    response = requests.get(url)
    if response.status_code == 200:
        # Save the file
        
        with open("C:\\_cleanup\\az-204-podcast\\" + filename, "wb") as file:
            file.write(response.content)
        print(f"- Downloaded {filename}")
    else:
        print(f"- Failed to download {url}")

    i = i + 1
