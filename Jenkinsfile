pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/thejanmv/DeploymentActivity01'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t thejanmv/python-todo-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'docker run --rm thejanmv/python-todo-app:latest pytest test_app.py'
            }
        }
        stage('Push to Docker Hub') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                bat 'docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}'
                bat 'docker push thejanmv/python-todo-app:latest'
            }
        }
    }
    post {
        always {
            cleanWs()  // Cleanup after build
        }
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
