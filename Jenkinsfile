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
                git branch: 'main', url: 'https://github.com/thejanmv/DeploymentActivity01', credentialsId: "${GIT_CREDENTIALS_ID}"
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    bat "docker run --rm ${DOCKER_IMAGE} pytest"
                }
            }
        }
        stage('Push to Docker Hub') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        bat "docker push ${DOCKER_IMAGE}"
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
