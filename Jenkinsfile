pipeline {
    agent any
    environment {
       
       DOCKER_PASSWD = credentials('docker-passwd')
       GIT_PASSWD = credentials('github-passwd')
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
                sh 'python -m pytest isReverse.py --junitxml=path'
                junit 'path'
                sh 'python  isReverse.py'
                
               }
            }
        }

        stage('Build Docker') {
            steps {

                //git credentialsId: '22cea117-6a3d-42ba-8e99-1a654c5ba61a', url: 'https://github.com/bandeep2000/kubernetes-ban.git'
                //Test bandeep
                git credentialsId: '22cea117-6a3d-42ba-8e99-1a654c5ba61a', url: 'https://github.com/bandeep2000/kubernetes-ban.git'
                sh 'touch hello-del3'
                sh 'git add hello-del3'
              
                sh 'git config --global user.email "bandeep2000@gmail.com"'
                sh  'git config --global user.name "bandeep2000"'

                //sed "s/COMMIT_SHA/123/g" test1.yml.tpl > test1.yml

                sh 'git commit -m "test1"'
                //sh 'git push origin master'
                sh "git remote set-url origin https://bandeep2000:$GIT_PASSWD@github.com/bandeep2000/kubernetes-ban.git"
                //https://github.com/bandeep2000/kubernetes-ban.git
                sh 'git push origin master'

                sh 'docker ps'
                sh 'docker build -t python-test .'
                sh 'docker run --rm  python-test python -m pytest isReverse.py'
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
