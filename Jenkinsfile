pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thejanmv/python-todo-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        GITHUB_CREDENTIALS_ID = 'github-credentials'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: "${GITHUB_CREDENTIALS_ID}", url: 'https://github.com/thejanmv/DeploymentActivity01.git'
            }
        }

    stage('Test') {
        steps {
            script {
                dockerImage.inside {
                    // Ensure pytest runs inside the 'tests' directory
                    sh 'pytest tests/'
                }
            }
        }
    }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace after the build
        }
    }
}
