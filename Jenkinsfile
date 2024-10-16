pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app:latest'
        GITHUB_CREDENTIALS = 'github-credentials'
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/thejanmv/DeploymentActivity01', credentialsId: "${GITHUB_CREDENTIALS}"
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
        stage('Test') {
            when {
                expression {
                    return fileExists('tests') // Check if tests directory exists
                }
            }
            steps {
                echo 'Running tests...'
                bat 'docker run --rm ${DOCKER_IMAGE} pytest'
            }
        }
        stage('Push to Docker Hub') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' } // Proceed only if tests pass
            }
            steps {
                echo 'Pushing to Docker Hub...'
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        bat 'docker push ${DOCKER_IMAGE}'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
            echo 'Build or tests completed!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}