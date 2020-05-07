pipeline {
    agent any
     parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    stages {
        stage('terraform init') {
            steps {
                sh 'export PATH=$PATH:~/.local/bin/'
                sh 'echo Hello'
                sh 'env'
                sh 'pylint'
            }
        }
          
    }
}
