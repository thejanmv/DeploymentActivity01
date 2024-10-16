pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-dockerhub-username/to-do-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        GITHUB_CREDENTIALS_ID = 'github-credentials'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: "${GITHUB_CREDENTIALS_ID}", url: 'https://github.com/your-repo/DeploymentActivity01.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    // Use the Docker image v1.0 for running tests
                    bat "docker run --rm ${DOCKER_IMAGE}:v1.0 pytest --version"
                    bat "docker run --rm ${DOCKER_IMAGE}:v1.0 pytest"
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
