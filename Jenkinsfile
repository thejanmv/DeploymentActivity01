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
                    sh 'docker build -t thejanmv/python-todo-app:latest .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        docker run --rm -d -p 5000:5000 --name test-container thejanmv/python-todo-app:latest
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
                            docker push thejanmv/python-todo-app:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to New EC2') {
            steps {
                sshagent(credentials: ['new-ec2-credentials']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@204.236.244.250 "
                            docker pull thejanmv/python-todo-app:latest || exit 1

                            # Stop the running container, if any
                            RUNNING_CONTAINER=\$(docker ps -q --filter ancestor=thejanmv/python-todo-app:latest)
                            if [ -n \"\$RUNNING_CONTAINER\" ]; then
                                docker stop \$RUNNING_CONTAINER
                                docker rm \$RUNNING_CONTAINER
                            fi

                            # Run the new container
                            docker run -d -p 5000:5000 thejanmv/python-todo-app:latest
                        "
                    """
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
