pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app:latest'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        GITHUB_CREDENTIALS_ID = 'github-credentials'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/thejanmv/DeploymentActivity01',
                                               credentialsId: "${GITHUB_CREDENTIALS_ID}"]]
                ])
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running test...'
                bat 'docker run --rm ${DOCKER_IMAGE} pytest --maxfail=1 --disable-warnings -q'
            }
        }
        stage('Push to Docker Hub') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        bat 'docker push ${DOCKER_IMAGE}'
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
