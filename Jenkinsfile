pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/thejanmv/DeploymentActivity01', credentialsId: 'github-credentials'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t "thejanmv/python-todo-app:65" .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat 'docker run -d -t -w /app -v C:/ProgramData/Jenkins/.jenkins/workspace/CI-Pipeline:/app thejanmv/python-todo-app:65'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    bat 'docker push thejanmv/python-todo-app:65'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
