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
                    sh 'docker build -t thejanmv/python-todo-app:65 .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        docker run --rm -d -p 5000:5000 --name test-container thejanmv/python-todo-app:65
                        docker stop test-container
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                            echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                            docker push thejanmv/python-todo-app:65
                        '''
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['aws-ec2-credentials']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ec2-user@184.73.143.93 << 'EOF'
                        docker pull thejanmv/python-todo-app:65
                        docker stop $(docker ps -q --filter ancestor=thejanmv/python-todo-app:65)
                        docker run -d -p 5000:5000 thejanmv/python-todo-app:65
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
