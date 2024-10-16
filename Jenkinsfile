pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app' // Docker image name
        DOCKER_REGISTRY = 'https://index.docker.io/v1/' // Docker Hub registry URL
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials' // Jenkins credentials ID for Docker Hub
        GIT_CREDENTIALS_ID = 'github-credentials' // Jenkins credentials ID for GitHub
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with the build ID as a tag
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Use the correct path for the Docker container
                    docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").inside("-w /app") {
                        // Run tests inside the Docker container
                        sh 'pytest'  // Assuming pytest is installed in the Docker image
                    }
                }
            }
        }

        stage('Push Docker Image') {
            when {
                branch 'main'  // Push only if on the main branch
            }
            steps {
                script {
                    // Push the Docker image to the Docker registry
                    docker.withRegistry("${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
                        echo "Pushing Docker image: ${DOCKER_IMAGE}:${env.BUILD_ID}"
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace after the build
        }
        failure {
            echo 'Build or tests failed!'
        }
        success {
            echo 'Build and tests succeeded!'
        }
    }
}
