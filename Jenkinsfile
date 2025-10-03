pipeline {
         agent {
             label 'python313'
         }
         stages {
             stage('Checkout') {
                 steps {
                     checkout scm
                 }
             }
             stage('Install Dependencies') {
                 steps {
                     bat '''
                         python --version
                         pip install -r requirements.txt
                     '''
                 }
             }
             stage('Run Tests') {
                 steps {
                     bat 'python -m pytest -v --junit-xml=test-results.xml'
                 }
                 post {
                     always {
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