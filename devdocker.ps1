# Define variables
$imageName = "gamefo-dev-image"
$containerName = "gamefo-dev-container"
$dockerfilePath = "C:\Users\Micha\Desktop\Github\Gamefo"

# Check if Dockerfile exists
$dockerfile = Join-Path -Path $dockerfilePath -ChildPath "Dockerfile"
if (-Not (Test-Path -Path $dockerfile)) {
    Write-Host "Error: Dockerfile not found at path $dockerfilePath"
    exit 1
}

# Build the Docker image
Write-Host "Building Docker image..."
docker build -t $imageName $dockerfilePath
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to build Docker image"
    exit 1
}

# Stop and remove any existing container with the same name
if (docker ps -a --format "{{.Names}}" | Select-String -Pattern $containerName) {
    Write-Host "Stopping and removing existing container..."
    docker stop $containerName
    docker rm $containerName
}

# Run the Docker container
Write-Host "Running Docker container..."
docker run -d -p 80:80 --name $containerName $imageName
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to run Docker container"
    exit 1
}

Write-Host "Container is up and running!"
