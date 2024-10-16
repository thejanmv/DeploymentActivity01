pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app' // Image name
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
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Ensure we run tests inside the built Docker image
                    docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").inside {
                        // Change to the correct working directory using Unix-style path
                        sh 'pytest'  // Execute your tests here
                    }
                }
            }
        }

        stage('Push Docker Image') {
            when {
                branch 'main'  // Only push if we are on the main branch
            }
            steps {
                script {
                    // Login and push the Docker image
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
            cleanWs()  // Clean the workspace after the build
        }
        failure {
            echo 'Build or tests failed!'
        }
        success {
            echo 'Build and tests succeeded!'
        }
    }
}
