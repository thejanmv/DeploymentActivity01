pipeline {
    agent any
    environment {
        // Ensure the Docker image name follows the naming conventions
        DOCKER_IMAGE = 'thejanmv/python-todo-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        GIT_CREDENTIALS_ID = 'github-credentials'
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Use the BUILD_ID for tagging to ensure unique tags for each build
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").inside {
                        // Use 'sh' for shell commands on Unix-like systems
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
                        // Push the image with the latest tag
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push('latest')
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Build or tests failed!'
        }
        success {
            echo 'Build and tests succeeded!'
        }
    }
}
