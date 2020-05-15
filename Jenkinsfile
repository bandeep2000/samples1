pipeline {
    agent any
    environment {
       
       DOCKER_PASSWD = credentials('docker-passwd')
       GIT_PASSWD = credentials('github-passwd')
       GIT_SHA = `git log -1 --pretty=%h`
    }
    //agent {
    //    docker { image 'node:7-alpine' }
    //}
     //parameters {
    //  string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    //}
    stages {
        stage('test local') {
            //agent {docker 'python:2.7' }
            steps {
               
               withEnv(["PATH_BIN=/var/jenkins_home/.local/bin"]) {
                
                sh 'env'
                
                sh 'python -m pytest isReverse.py --junitxml=path'
                junit 'path'
                
                sh 'python  isReverse.py'
                
               }
            }
        }

        stage('Build Docker') {
            steps {

                sh 'docker ps'
                sh 'docker build -t bandeep2000/python-test:`git log -1 --pretty=%h` .'
                echo $GIT_SHA
                 
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
