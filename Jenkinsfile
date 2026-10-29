
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
                    if errorlevel 1 exit /b 1
                    docker images pranayaparthiban/recommendation-system
                '''
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    bat '''
                        @echo off
                        set "PATH=C:\\Users\\prana\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%"

                        powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -Command "$env:DOCKERHUB_TOKEN | docker login --username $env:DOCKERHUB_USER --password-stdin"
                        if errorlevel 1 exit /b 1

                        docker push pranayaparthiban/recommendation-system:v3
                        if errorlevel 1 exit /b 1

                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Recommendation System v3 built and pushed to Docker Hub!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for the first error.'
        }
    }
}
