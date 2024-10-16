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
                bat 'docker build -t thejanmv/python-todo-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside('-w //app') {
                        bat 'pytest tests/'
                    }
                }
            }
        }




        stage('Push to Docker Hub') {
            when {
                expression {
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Pushing to Docker Hub...'
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        bat 'docker push thejanmv/python-todo-app:latest'
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
