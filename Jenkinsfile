pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app:latest'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') 
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/thejanmv/DeploymentActivity01'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm -w /app ${DOCKER_IMAGE} pytest'
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { return currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat 'docker push ${DOCKER_IMAGE}'
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
