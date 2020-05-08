pipeline {
    agent none
    environment {
       
       DOCKER_PASSWD = credentials('docker-passwd')
    }
    //agent {
    //    docker { image 'node:7-alpine' }
    //}
     //parameters {
    //  string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    //}
    stages {
        stage('test local') {
            agent {docker 'python:2.7' }
            steps {
               
               withEnv(["PATH_BIN=/var/jenkins_home/.local/bin"]) {
                
                sh 'env'
                //sh '/var/jenkins_home/.local/bin/pylint'
                //sh '$PATH_BIN/pylint test1.py'
                //sh 'python -m pytest isReverse.py --junitxml=path'
                sh 'python  isReverse.py'
                sh 'docker ps'
                sh 'docker build -t python-test .'
                sh 'docker run --rm  python-test python -m pytest isReverse.py'
               }
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t bandeep2000/python-test .'
                 
            }
        }

        stage('Test Docker') {
            steps {
                sh 'docker run --rm  bandeep2000/python-test python -m pytest isReverse.py'
                sh "docker login -u bandeep2000 -p  $DOCKER_PASSWD"
                sh 'docker push bandeep2000/python-test' 
            }
        }
          
    }
}
