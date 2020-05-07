pipeline {
    agent any
     parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

    }

    }
    stages {
        stage('terraform init') {
            steps {
                sh 'terraform init'
            }
        }
          
        stage('terraform apply') {
            steps {
                sh 'pwd'
                dir('terraform') {
                   sh 'terraform init'
                   script {
                     if (params.PERSON == 'apply' ) {
                        sh 'terraform apply --auto-approve'
                     }
                     sh 'terraform destroy --auto-approve'
                     sh 'pwd'
                   }
                }
                sh 'pwd'
            }
        }
    }
}
