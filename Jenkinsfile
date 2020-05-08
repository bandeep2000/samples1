pipeline {
    //agent any
    //agent {
    //    docker { image 'node:7-alpine' }
    //}
     //parameters {
    //  string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    //}
    stages {
        stage('terraform init') {
            steps {
               withEnv(["PATH_BIN=/var/jenkins_home/.local/bin"]) {
                
                sh 'env'
                //sh '/var/jenkins_home/.local/bin/pylint'
                //sh '$PATH_BIN/pylint test1.py'
                //sh 'python -m pytest isReverse.py --junitxml=path'
                sh 'python  isReverse.py'
                sh 'docker ps'
               }
            }
        }
          
    }
}
