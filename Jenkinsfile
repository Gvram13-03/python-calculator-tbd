pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest'
            }
        }
    }
}