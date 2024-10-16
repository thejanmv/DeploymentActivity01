pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/thejanmv/DeploymentActivity01.git', credentialsId: 'github-credentials'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t lithmiseneviratne/python-todo-app:65 .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat 'docker run -d -p 0:5000 lithmiseneviratne/python-todo-app:65'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%"
                        bat "docker push lithmiseneviratne/python-todo-app:65"
                    }
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
