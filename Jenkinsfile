pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/to-do-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        GITHUB_CREDENTIALS_ID = 'github-credentials'
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
                    // Set the working directory explicitly to /app (Unix-style path) to avoid Windows path issues
                    dockerImage.inside('-w /app') {
                        sh 'pytest --version'
                        sh 'pytest'  // Run your tests inside the container
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace after the build
        }
    }
}
