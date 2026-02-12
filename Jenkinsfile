pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'venv\\Scripts\\activate && python train.py'
            }
        }

        stage('Test Model') {
            steps {
                bat 'venv\\Scripts\\activate && python test.py'
            }
        }
    }
}
