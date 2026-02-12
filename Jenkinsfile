pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Test Model') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Deploy') {
            steps {
                bat 'start /B python app.py'
            }
        }
    }
}
