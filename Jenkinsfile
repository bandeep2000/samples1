pipeline {
    agent any
     parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    environment {
       PATH=$PATH:/var/jenkins_home/.local/bin/'
   }
    stages {
        stage('terraform init') {
            steps {
                sh 'export PATH=$PATH:/var/jenkins_home/.local/bin/'
                sh 'echo Hello'
                sh 'env'
                //sh '/var/jenkins_home/.local/bin/pylint'
                sh 'pylint'
            }
        }
          
    }
}
