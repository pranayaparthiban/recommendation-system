
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
                    echo Required files are present.
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
                    docker --version
                    docker info
                '''
            }
        }
    }

    post {
        success {
            echo 'Project checks and Docker access succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
