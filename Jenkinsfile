pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app' // Ensure this follows the pattern '^[a-zA-Z0-9]+((\.|_|__|-+)[a-zA-Z0-9]+)*$'
        DOCKER_REGISTRY = 'https://index.docker.io/v1/' // Docker Hub registry URL
        DOCKER_CREDENTIALS_ID = 'your-docker-credentials-id' // Jenkins credentials ID for Docker Hub
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
                    docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").inside {
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