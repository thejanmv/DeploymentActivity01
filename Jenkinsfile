pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/to-do-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'  // The Jenkins credentials ID for DockerHub
        GITHUB_CREDENTIALS_ID = 'github-credentials'     // The Jenkins credentials ID for GitHub
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: "${GITHUB_CREDENTIALS_ID}", url: 'https://github.com/thejanmv/DeploymentActivity01.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'pytest --version'
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        // Push the Docker image with the build number tag
                        dockerImage.push("${env.BUILD_NUMBER}")
                        // Push the Docker image with the 'latest' tag
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up the workspace after the build
        }
    }
}
