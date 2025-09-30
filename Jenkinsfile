pipeline {
    agent any  // Run on any available agent (Jenkins master for now)

    stages {
        stage('Checkout') {
            steps {
                // Pulls code from GitHub
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest -v --junit-xml=test-results.xml'  // -v for verbose, JUnit for reports
            }
            post {
                always {
                    // Archive test results for Jenkins UI
                    junit 'test-results.xml'
                }
                success {
                    echo 'Tests passed! Trunk is releasable.'
                }
                failure {
                    echo 'Tests failed—check errors before merging to trunk.'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline complete. Review for trunk merge.'
        }
    }
}