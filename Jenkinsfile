
pipeline {
    agent {
        label 'linux-docker'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    .venv/bin/flake8 app.py tests
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    .venv/bin/pytest -v
                '''
            }
        }

        stage('Build image') {
            steps {
                sh '''
                    docker build -t finance-portal:${BUILD_NUMBER} .
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the stage and console output.'
        }
    }
}
