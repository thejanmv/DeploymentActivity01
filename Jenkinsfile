pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "lithmiseneviratne/python-todo-app"
        DOCKER_TAG = "latest"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
        SSH_CREDENTIALS = "ec2-key"
        EC2_HOST = "ec2-user@ec2-54-145-210-17.compute-1.amazonaws.com"
        CONTAINER_NAME = 'python-todo-app'
        PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git url: 'https://github.com/thejanmv/DeploymentActivity01.git', credentialsId: 'github-credentials'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Use bat for Windows and sh for Linux
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run the Docker container in detached mode
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:${PORT} ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Use withCredentials for Docker Hub login
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%"
                        bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
        }
    }
    post {
        always {
            // Cleanup workspace after the build
            script {
                // Stop and remove the Docker container after the build
                bat "docker stop ${CONTAINER_NAME} || true"
                bat "docker rm ${CONTAINER_NAME} || true"
            }
            cleanWs() // Clean the workspace
        }
    }
}
