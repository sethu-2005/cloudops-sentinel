pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sethu-2005/cloudops-sentinel.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloudops-sentinel:1.0 .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop cloudops-sentinel || true'
                sh 'docker rm cloudops-sentinel || true'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d --name cloudops-sentinel -p 5000:5000 cloudops-sentinel:1.0'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
                sh 'curl -f http://localhost:5000 || exit 1'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}