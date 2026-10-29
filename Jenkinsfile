
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Verify Project Files') {
            steps {
                bat '''
                    if not exist app.py exit /b 1
                    if not exist requirements.txt exit /b 1
                    if not exist Dockerfile exit /b 1
                    echo Required project files are present.
                '''
            }
        }

        stage('Python Syntax Check') {
            steps {
                bat '''
                    python --version
                    python -m py_compile app.py
                '''
            }
        }

        stage('Check Docker Access') {
            steps {
                bat '''
                    set "PATH=C:\\Users\\prana\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%"
                    docker --version
                    docker info
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    set "PATH=C:\\Users\\prana\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%"
                    docker build -t pranayaparthiban/recommendation-system:v3 .
                    docker images pranayaparthiban/recommendation-system
                '''
            }
        }
    }

    post {
        success {
            echo 'Recommendation System pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for the first error.'
        }
    }
}
