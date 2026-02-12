pipeline {
    agent any

    tools {
        python 'Python311'
    }

    stages {

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

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

        stage('Success') {
            steps {
                echo 'ML Pipeline Completed Successfully!'
            }
        }
    }
}
