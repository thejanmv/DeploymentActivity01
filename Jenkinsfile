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
        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push thejanmv/python-todo-app:65'
                }
            }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push thejanmv/python-todo-app:65'
                }
            }
        }

        stage('Deploy to EC2') {
    steps {
        sshagent(credentials: ['aws-ec2-credentials']) {
            sh '''
                ssh -o StrictHostKeyChecking=no ec2-user@184.73.143.93 << 'EOF'
                docker pull thejanmv/python-todo-app:65 || exit 1
                
                # Stop the running container, if any
                RUNNING_CONTAINER=$(docker ps -q --filter ancestor=thejanmv/python-todo-app:65)
                if [ -n "$RUNNING_CONTAINER" ]; then
                    docker stop $RUNNING_CONTAINER
                fi
                
                # Run the new container
                docker run -d -p 5000:5000 thejanmv/python-todo-app:65
                EOF
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
