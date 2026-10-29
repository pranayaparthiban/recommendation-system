
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
                    echo All required project files are present.
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
    }

    post {
        success {
            echo 'Recommendation System pipeline passed!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
