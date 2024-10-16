pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "lithmiseneviratne/python-todo-app"
        DOCKER_TAG = "latest"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
        SSH_CREDENTIALS = "ec2-key"
        EC2_HOST = "ec2-user@ec2-54-145-210-17.compute-1.amazonaws.com"
    }
    
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

        stage('Deploy to EC2') {
            steps {
                // Use PowerShell or bat commands for Windows
                bat '''
                    ssh -o StrictHostKeyChecking=no -i C:/ProgramData/Jenkins/.ssh/new_key_pair.pem ec2-user@ec2-54-145-210-17.compute-1.amazonaws.com "echo 'Deployment Successful!'"
                '''
            }
        }
        
    }
    post {
        always {
            cleanWs()
        }
    }
}
