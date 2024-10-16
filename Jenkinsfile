pipeline {
    agent {
        docker {
            image 'python:3.8-slim'
            label 'docker-agent'
            args '-v /tmp:/tmp' // Optional: mount volume if needed
        }
    }
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
                sh 'docker build -t thejanmv/python-todo-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm thejanmv/python-todo-app:latest pytest test_app.py'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials-id', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                        sh 'docker push thejanmv/python-todo-app:latest'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
