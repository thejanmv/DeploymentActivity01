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
        stage('Deploy to EC2') {
            steps {
                sshagent(['aws-ec2-credentials']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ec2-user@184.73.143.93 << EOF
                    docker pull your-dockerhub-username/your-app-image:latest
                    docker run -d -p 5000:5000 your-dockerhub-username/your-app-image
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
