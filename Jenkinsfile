pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')  // Jenkins DockerHub credentials
        DOCKER_IMAGE = 'thejanmv/python-todo-app'  // Docker image name
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/thejanmv/DeploymentActivity01'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'docker run $DOCKER_IMAGE ./run_tests.sh'  // Example: replace with your test command
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Login to DockerHub and push image
                    sh 'echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}
