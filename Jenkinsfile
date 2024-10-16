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
                bat 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                bat 'docker push thejanmv/python-todo-app:latest'
            }
        }
    }
    post {
        always {
            node('any') {  // Ensure a valid node context for post actions
                cleanWs()  // Workspace cleanup
            }
        }
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
