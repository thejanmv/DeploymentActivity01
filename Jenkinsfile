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
                sshagent(credentials: ['ec2-jenkins']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ec2-user@<EC2-PUBLIC-IP> << EOF
                        docker stop $(docker ps -q)
                        docker pull lithmiseneviratne/python-todo-app:latest
                        docker run -d -p 80:5000 lithmiseneviratne/python-todo-app:latest
                        EOF
                    '''
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
