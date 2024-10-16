pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app:latest'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        GIT_CREDENTIALS_ID = 'github-credentials'
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
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
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
