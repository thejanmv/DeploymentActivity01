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
                    bat 'docker run --rm -d -p 5000:5000 lithmiseneviratne/python-todo-app:65'
                    // Add any test commands you need here
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
